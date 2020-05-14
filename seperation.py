from change_shape import give_the_right_form

#pairnei ws orisma mia grammi me alfarithmitiko kai tin epistrefei xwrismeni se pinaka 
#an i grammi poy erthei den einai xwrismeni se pinaka kai einai ena string
#tote tin stelnei sto change_shape kai ginetai kei ayto, wste na mporei na to epexergastei

def seperate(aword,size_of_array,row_of_context,error_counter):    
        #aword=['-233x1+434x2-4x3']

        
        if(len(aword)==1):
            aword=give_the_right_form(aword)
        
        
        #print(aword)



        if(aword==None or aword==""):
            return error_counter+1,None
        C=[0]*size_of_array
        #C=[0]*4
        keepbacknumber=''
        keepfrontnumber=""
        counterfor_analyse=0
        counter_of_variable=0
        counter_of_sumbols=0
        keeptheprevioussymbol=''
        flag_for_text_without_gap=0

        #print(aword)
        for letter in aword: #pernei kathe gramma tou word , p.x. word=32x3 tote to prwto letter=3 ,to deutero letter=2 etc.
            #print(letter)
            
            if (letter !='+' and letter !='-' ) :
                for symbol in letter:
                    
                    #print(symbol)
                    if(symbol == '>' or symbol == '<' or symbol == '='):
                        break
                    if(counterfor_analyse ==1 and symbol != 'x' ):
                        keepfrontnumber=keepfrontnumber+symbol
                    if(counterfor_analyse ==0 and symbol != 'x' ):
                        keepfrontnumber=symbol
                        if(keeptheprevioussymbol=='-'):#an einai arnitikos tou to vazei mprosta 
                            keepfrontnumber=keeptheprevioussymbol+keepfrontnumber
                        counterfor_analyse=1
                    if(counterfor_analyse == 3 and symbol != 'x' ):
                        keepbacknumber=keepbacknumber+symbol
                        counterfor_analyse=0
                    if(counterfor_analyse ==2 and symbol != 'x' ):
                        keepbacknumber=symbol
                        counterfor_analyse=3
                    if(symbol == 'x'):
                        counter_of_variable=counter_of_variable+1
                        counterfor_analyse=2
                        if(keepfrontnumber==''):#an den yparxei kapoios arithmos mprosta apo to x tote tou dinoume
                            keepfrontnumber="1"#tin timi 1
                            if(keeptheprevioussymbol=='-'):#an ypirxe p.x. -x5 tote to 1 prepei na ginei -1
                                keepfrontnumber='-1'
                        if(keepfrontnumber=='-'):
                            keepfrontnumber='-1'
                if(symbol=='x' ):
                    print("Error something is missing after ",counter_of_variable," variable ,in the ",row_of_context,'row')
                    error_counter=error_counter+1
                #print(keepfrontnumber+" poak "+keepbacknumber)
                
            counterfor_analyse=0
            if(keepbacknumber!=''):#se periptwsi pou einai keno , na min stamatisi
                if(int(keepbacknumber)>0):#elegw an o arithmos meta to x einai thetikos, an einai arnitikos einai sigoura lathos
                        try:
                            C[int(keepbacknumber)-1]=int(keepfrontnumber)
                        except IndexError:
                            print("")
            
            if(letter == "+" or letter == "-"):#metraw ta symbola + and - ,
                counter_of_sumbols=counter_of_sumbols+1
                keeptheprevioussymbol=letter #se periptwsi poy einai - , na to prosthesw ston pinaka
            keepbacknumber=''
            keepfrontnumber=""
        
        if(counter_of_sumbols != counter_of_variable-1):#eleghi an leipei kapoio + or - , eleghontas tin diafora
            if(row_of_context==1):
                print("Error there is missing a + or -, in Objective function")
                error_counter=error_counter+1
            else:
                print("Error there is missing a + or -, in A array of row",row_of_context-1)
                error_counter=error_counter+1
        
        #print(C)
        return error_counter,C


#print(seperate("adsf",3,3))
                    



