#eleghi an yparxi to arxeio , an oxi bgazei minima ston xristi
#an den yparxei to arxeio epanalmbani ston xristi kai dinei tin dinatotita 
#na xanavalei arxeio se periptwsi lathous

import os.path
from os import path

def opener():
    answerofuser=None
    while True:
        print("Enter a filename:")
        filename = input()

        if(path.exists(filename)==True):
            return filename
            '''with open(filename, "r") as f:
                data = f.readlines()
                for line in data:
                    words = line.split()
                    print(words)'''
        else:
            print("Wrong name of file or the file doesn't exist on the same folder,if you want to try again write Yes else put No")
            answerofuser=input()

        if (answerofuser != 'Yes' and answerofuser !='Y' and answerofuser !='y'):
            break


