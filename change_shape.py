#pairnei ena alfarithmitiko kai dimiourgei ena pinaka me ta stoixeia toy
#ta stoixeia einai p.x.[2x1+x2] kai dimiourgei ton pinaka ['2x1','+','x2']
#epeidi den xreiazomaste ta stoixeia meta ta >,=,< ta petame


def give_the_right_form(aword):
    
    #aword=['x1+32x2+2x>=231']
    sum_of_symbols=0
    keepletter=''

    if(len(aword)==1):
        counter_of_column=0
        for phrase in aword:
            for letter in phrase:
                #print(letter)
                if(letter=="-" and counter_of_column<=1):
                    continue
                if(letter=="+" or letter=="-"):
                    sum_of_symbols=sum_of_symbols+1
                counter_of_column=counter_of_column+1
                        
        #print(sum_of_symbols*2+1)
        new_word=[""]*(sum_of_symbols*2+1)
        l=0
        counter_of_column=0
        for phrase in aword:
            for letter in phrase:
                #print(letter)
                if(letter == '<' or letter == '=' or letter =='>' ):
                    break
                if(letter == '-' and counter_of_column<2):
                    keepletter=letter
                if(letter != '+' and letter != '-'):
                    keepletter=keepletter+letter
                if((letter == '+' or letter == '-')and counter_of_column>1):
                    #print(keepletter)
                    new_word[l]=keepletter
                    keepletter=''
                    try:
                        new_word[l+1]=letter
                    except IndexError:
                        print('')
                    l=l+2
                if(l==sum_of_symbols*2):
                    new_word[l]=keepletter
                counter_of_column=counter_of_column+1
               
                
            #print(counter_of_column)
            if(letter == '=' or letter == '>' or letter =='<'   ):
                break
    
    return new_word



#print(give_the_right_form("af"))