#eleghei an leipei kapoio symvolo >,<,=


def check_if__miss_symbol (filename):
    #filename='LP02.LTX'
    keeptheprevious_number_in_string=None
    counter_of_line=0
    i=0
    with open(filename, "r") as f:
                    data = f.readlines()

                    for line in data:
                        counter_of_line=counter_of_line+1
                        for letter in line:
                            if(letter=='\n' ):
                                if(keeptheprevious_number_in_string == '>'  or keeptheprevious_number_in_string =='=' or keeptheprevious_number_in_string == '<'):
                                    print("Error there is no number after >,=,< in line:",counter_of_line)
                                    i=1
                                    
                            
                                    

                            if( letter.isspace() == False):
                                keeptheprevious_number_in_string=letter
    if(i==1):
        return False
    else:
        return True