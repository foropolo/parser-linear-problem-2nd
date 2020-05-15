from openfiles import opener
from size_checker_and_Eqin import size_function
from B_array import B_array_creator
from check_numbers_after_restrictions import check_if__miss_symbol
from C_A_finder import find_arrays_A_C

all_error=0 #mazeuei ola ta error apo kathe synartisi 
#filename=opener() #sinartisi opener zitaei apo ton xristi na balei to onoma tou fakelou kai eleghi an yparxei o fakelos
filename="LP01.LTX"

all_error,size_of_rows, size_of_column,Eqin=size_function(filename,all_error) #pernw piso to megethos twn pinakwn poy prepei na dimiourgisw
#print('size of rows',size_of_rows,"size of column",size_of_column,",E=",Eqin)

all_error,B=B_array_creator(filename,size_of_rows,all_error)
#print('B=',B)


    
A=[[0]*size_of_column]*size_of_rows #dimiourgw ton pinaka A
X=[0]*size_of_column #dimiourgw ton pinaka C
C=[[0]*1]*size_of_column

all_error,X,A=find_arrays_A_C(filename,size_of_rows,size_of_column,all_error)

pointer=0
for k in X:
    C[pointer]=[k]
    pointer=pointer+1




#print('C=',C,'A=',A)

MinMax=0

counter_of_quee_of_words=0 #metritis poy metraei kathe lexi , mexri to telos
counter_of_sentece=0 #metritis pou metraei tin stili poy briskomaste
counter_of_line=0 #metritis poy metraei tin grammi pou briskomaste
flag_for_st=0
flag_for_MinMax=0

flag_for_symbols=check_if__miss_symbol(filename)#gyrnaei FALSE an leipei kapoios arithmos gia ton pinaka B, 
if(flag_for_symbols==False):
    all_error=all_error+1
    filename=None

if(filename!=None and all_error==0):
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            counter_of_line=counter_of_line+1
            counter_of_sentece=0 #midenizw tin stili kathe fora poy allazw grammi, giati xekinaw apo tin arxi
            #print(words)
                
            for word in words:
                #print(word)
                counter_of_quee_of_words=counter_of_quee_of_words+1
                if( word=='max' and counter_of_quee_of_words==1):
                    MinMax=1
                    #print("forotzidis")
                elif (word=='min' and counter_of_quee_of_words==1):
                    MinMax=-1
                if (counter_of_quee_of_words>1 and MinMax==0 and counter_of_line==1):
                    flag_for_MinMax=1
                    break
                if(counter_of_quee_of_words>1 and( word == 'st' or word == 's.t.' or word == 'subject') and counter_of_line==2):
                    flag_for_st=1
                    #print(word)
                   # front,back=seperate(word)
                    #print (front,back)

            if(flag_for_st==0 and counter_of_line>2):#stamataei tin epexergasia molis dei oti den yparxei st, s.t. or subject
                break
            if(flag_for_MinMax==1 and counter_of_line > 1):# stamataei tin epexergasia molis dei oti den yparxei Min or Max
                break    
        
        if(MinMax==0):
            print("Error the problem doesn't write if the problem is Min or Max")
            all_error=all_error+1

        if (flag_for_st == 0 and flag_for_MinMax==0):
            print("Error there is no character of 's.t.' or 'st' or 'subject' in the your file " )
            all_error=all_error+1
            #print (words,end='')

print('MinMax=',MinMax)
print('C=',C,'A=',A)
print('B=',B)
print('size of rows',size_of_rows,"size of column",size_of_column,",E=",Eqin)

'''
if(all_error==0):
    f=open("analyze_"+filename,"x")
    f.write("MinMAx="+str(MinMax)+"\nC="+str(C)+"\nA="+str(A)+"\nB="+str(B)+"\nEqin="+str(Eqin))
    f.close
else:
    print("There exist at least ",all_error," and the program cannot create the analyze the ",filename)

'''

