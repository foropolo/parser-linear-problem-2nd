#dimiourgw to pinaka B me perasmata to arxeio kai to megethos twn periorismwn
#xrisimopoiw tin texniki opou xekinaw meta apo kapoio ta parakatw symbola =,=>,=<,<=,>=
#ama ta prospelasi meta apo kei krataw ton arithmo(ws string) ews tou teliwsei i grammi \n
#apo kei kai pera ton metatrepw sto telos apo string se integer kai ton gyrnaw pisw


def B_array_creator(filename,counter_of_restrinctions,error_counter):

    #filename='LP02.LTX'

    flag_for_B_array=0
    result_of_restrictions=''
    keeptheprevious_number_in_string=None

    with open(filename, "r") as f:
                data = f.readlines()

                for line in data:
                    #print(line)
                    for letter in line:
                        
                        #print(letter)
                        if(flag_for_B_array == 1):
                                result_of_restrictions=result_of_restrictions+letter

                        if((keeptheprevious_number_in_string == '>' or keeptheprevious_number_in_string =='=' or keeptheprevious_number_in_string == '<') and letter== '\n' ):
                            print("Error there is no number after restriction")
                            error_counter=error_counter+1
                            
                        if(letter == '\n' and flag_for_B_array == 1):
                            flag_for_B_array=0
                            result_of_restrictions=result_of_restrictions+" "

                        if (letter == '=' and keeptheprevious_number_in_string == '>'): #eleghos >=
                            flag_for_B_array=1
                                
                        elif (letter == '=' and keeptheprevious_number_in_string == '<'): #eleghos <=
                            flag_for_B_array=1    
                                
                        elif (letter == '<' and keeptheprevious_number_in_string =='='):#eleghos =<
                            flag_for_B_array=1
                                
                        elif( letter == '>' and keeptheprevious_number_in_string =='='):#eleghos =>
                            flag_for_B_array=1 
                                                                        #eleghos = 
                        elif(letter == '='):
                            flag_for_B_array=1
                        
                        keeptheprevious_of_the_previous = keeptheprevious_number_in_string
                        keeptheprevious_number_in_string=letter

    keep_the_numbers_B=''#diwxnw tixon skoupidia > ,= ,>
    for j in result_of_restrictions:
        if(j=='>' or j=='<' or j=='='):
            continue
        keep_the_numbers_B=keep_the_numbers_B+j
    #print(keep_the_numbers_B )
    i=0
    B=[0]*counter_of_restrinctions
    for number_B in keep_the_numbers_B.split():
        try:
            B[i]=int(number_B)
            i=i+1
        except ValueError:
            print("")
        

    return error_counter,B



#print(B_array_creator("da",4))