

MinMax=1 #1 = Max , -1=Min
E= [-1, 1, 0] #-1 = "<=" or "=<" , 1 = ">=" or "=>" , 0 = "="
A= [[1, 1, 2], [1, 0, -1], [-1, 1, 5]]
B= [9, 2, 4] 
X= [2 ,4 ,5] # o pinakas C pou exw dimiourgisei einai 1 stili me 3 grammes, auto me diskoleuei apo to na einai 3 stiles kai 1 grammi, giati mporw na to xeiristw pio eukola
#print(len(A))

text_for_variables="    "
if(MinMax == 1):#conversion from Max to Min
    text_for_objective_function="Max "
    for x in range(len(E)):
        if(E[x] == -1):
            text_for_variables=text_for_variables+"w"+str(x+1)+">=0 ,"
        elif(E[x] == 1):
            text_for_variables=text_for_variables+"w"+str(x+1)+"<=0 ,"
        elif(E[x] == 0):
            text_for_variables=text_for_variables+"w"+str(x+1)+" free,"
elif(MinMax == -1):#conversion from Min to Max
    text_for_objective_function="Min "
    for x in range(len(E)):
        if(E[x] == -1):
            text_for_variables=text_for_variables+"w"+str(x+1)+"<=0 ,"
        elif(E[x] == 1):
            text_for_variables=text_for_variables+"w"+str(x+1)+">=0 ,"
        elif(E[x] == 0):
            text_for_variables=text_for_variables+"w"+str(x+1)+" free,"

print(text_for_variables)
#create the objective function
for x in range(len(E)):
    if(B[x] >= 0 and x>0):
        text_for_objective_function=text_for_objective_function+" + "+str(B[x])+"w"+str(x+1)
    elif(B[x] < 0):
        text_for_objective_function=text_for_objective_function+"  "+str(B[x])+"w"+str(x+1)
    else:
        text_for_objective_function=text_for_objective_function+"  "+str(B[x])+"w"+str(x+1)

print(text_for_objective_function)

