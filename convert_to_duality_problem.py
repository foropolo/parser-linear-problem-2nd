

MinMax=-1 #1 = Max , -1=Min
E= [-1, 1, 0,1] #-1 = "<=" or "=<" , 1 = ">=" or "=>" , 0 = "="
A= [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12],[13,14,15,16]]
B= [9, 2, 4,100] 
X= [2 ,4 ,5,123] # o pinakas C pou exw dimiourgisei einai 1 stili me 3 grammes, auto me diskoleuei apo to na einai 3 stiles kai 1 grammi, giati mporw na to xeiristw pio eukola
#print(len(A))

text_for_variables="    "
if(MinMax == 1):#conversion from Max to Min
    text_for_objective_function="Min "
    for x in range(len(E)):
        if(E[x] == -1):
            text_for_variables=text_for_variables+"w"+str(x+1)+">=0 ,"
        elif(E[x] == 1):
            text_for_variables=text_for_variables+"w"+str(x+1)+"<=0 ,"
        elif(E[x] == 0):
            text_for_variables=text_for_variables+"w"+str(x+1)+" free,"
elif(MinMax == -1):#conversion from Min to Max
    text_for_objective_function="Max "
    for x in range(len(E)):
        if(E[x] == -1):
            text_for_variables=text_for_variables+"w"+str(x+1)+"<=0 ,"
        elif(E[x] == 1):
            text_for_variables=text_for_variables+"w"+str(x+1)+">=0 ,"
        elif(E[x] == 0):
            text_for_variables=text_for_variables+"w"+str(x+1)+" free,"


#create the objective function
for x in range(len(E)):
    if(B[x] >= 0 and x>0):
        text_for_objective_function=text_for_objective_function+" + "+str(B[x])+"w"+str(x+1)
    elif(B[x] < 0):
        text_for_objective_function=text_for_objective_function+"  "+str(B[x])+"w"+str(x+1)
    else:
        text_for_objective_function=text_for_objective_function+"  "+str(B[x])+"w"+str(x+1)
    



#print(A[1])
duality_A=[0]*len(E)
a_row=""
for x in range(len(E)):
    for j in range(len(E)):
        #print("A[",j,"][",x,"]=",A[j][x])
        if(A[j][x] >=0 and j>0):
            a_row=a_row+" + "+str(A[j][x])+"w"+str(j+1)
        elif(A[j][x] < 0):
            a_row=a_row+"  "+str(A[j][x])+"w"+str(j+1)
        else:
            a_row=a_row+"  "+str(A[j][x])+"w"+str(j+1)
    duality_A[x]=a_row
    a_row=""

#print(duality_A)
#print(A)

for x in range(len(E)):
    if(MinMax == 1):#1 = Max
        duality_A[x]=duality_A[x]+" >= "+str(X[x])
    elif(MinMax == -1):#1=Min
        duality_A[x]=duality_A[x]+" <= "+str(X[x])

print(text_for_objective_function)
print(duality_A)
print(text_for_variables)