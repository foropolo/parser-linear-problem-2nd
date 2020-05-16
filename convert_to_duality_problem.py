

MinMax=1 #1 = Max , -1=Min
E= [-1, 1, 0] #-1 = "<=" or "=<" , 1 = ">=" or "=>" , 0 = "="
A= [[1, 1, 2], [1, 0, -1], [-1, 1, 5]]

print(len(A))

text_for_variables="    "
if(MinMax == 1):#conversion from Max to Min
    for x in range(len(E)):
        if(E[x] == -1):
            text_for_variables=text_for_variables+"w"+str(x+1)+">=0 ,"
        elif(E[x] == 1):
            text_for_variables=text_for_variables+"w"+str(x+1)+"<=0 ,"
        elif(E[x] == 0):
            text_for_variables=text_for_variables+"w"+str(x+1)+" free,"
elif(MinMax == -1):#conversion from Min to Max
    for x in range(len(E)):
        if(E[x] == -1):
            text_for_variables=text_for_variables+"w"+str(x+1)+"<=0 ,"
        elif(E[x] == 1):
            text_for_variables=text_for_variables+"w"+str(x+1)+">=0 ,"
        elif(E[x] == 0):
            text_for_variables=text_for_variables+"w"+str(x+1)+" free,"


print(text_for_variables)