from seperation import seperate

#vriski to pinaka A and C, pairnei to arxeio kai to analyei se grammes
#stelnei tin kathe seira sto seperation kai auto to gyrnaei se pinaka X
#analogos pou vriskomaste p.x. stin grammi 1 oi pinakes C=X
#gia ton pinaka A , stelnoyme kathe grammi sto seperation kai otan gyrnaei pisw kanoume to exis
#A[grammi]=X kai synthetoume etsi ton pinaka A

def find_arrays_A_C(filename,number_of_rows,number_of_variables,error_counter):
    #filename="LP02.LTX"
    counter_of_line=0
    #number_of_variables=4#tha pernaei ws orisma apo to kyrio programma
    #number_of_rows=4#tha pernaei ws orisma to kyrio programma
    C=[0]*number_of_variables#dimiourgw ton pinaka C
    A=[[0]*number_of_variables]*number_of_rows#dimiourgw ton pinaka A
    X=[0]*number_of_variables#tha xrisimopoiithis wste na gemisoume ton A

    with open(filename, "r") as f:
            data = f.readlines()
            for line in data:
                words = line.split()
                counter_of_line=counter_of_line+1
                counter_of_sentece=0 #midenizw tin stili kathe fora poy allazw grammi, giati xekinaw apo tin arxi
                if('end' in words):
                    break
                if(counter_of_line==1):
                    if("max" in words):
                        words.remove("max")
                    elif("min" in words):
                        words.remove("min")
                    #print(words)
                    error_counter,C=seperate(words,number_of_variables,counter_of_line,error_counter)
                    #print(C)
                    #print(seperate(words))
                if(counter_of_line==2):
                    #print(words)
                    if('s.t.' in words):
                        words.remove('s.t.')
                    elif('st' in words):
                        words.remove('st')
                    elif('subject' in words):
                        words.remove('subject')
                    error_counter,X=seperate(words,number_of_variables,counter_of_line,error_counter)
                    #print(X)
                    A[counter_of_line-2]=X
                    #print(A)
                #print(words,'apod')
                if(counter_of_line >= 3 ):
                    error_counter,X=seperate(words,number_of_variables,counter_of_line,error_counter)
                    j=0
                    #print(X)
                    #print('counter of line=',counter_of_line)
                    try:
                        A[counter_of_line-2]=X
                    except IndexError:
                        print('')
                    """
                    for i in X:
                        A[counter_of_line-1][j]=i
                        j=j+1 """

    return error_counter,C  ,A
    