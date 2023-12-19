import os

keyFilePath = 'key.txt'

def isEmpty(keyFile):
    if (os.path.getsize(keyFile) == 0):
        print("Error can't open key file.(terminate Program)\n")
        exit(1)

def Cesar(Input, Type):
    # Check If the file is empty
    isEmpty(keyFilePath)
    with open(keyFilePath) as keyFile:
        key = keyFile.read()
    lenght = len(key)
    # For Testing
    # print(key)
    # print(lenght)
    InputList = list(Input)
    if (Type == 1): #Encrypt
        i,j = 0,0
        for i in range(len(InputList)):
            if(j == lenght):
                j = 0
            # Convert InputList to ASCII
            ascii_value = ord(InputList[i])
            #print("ascii of input:",ascii_value)

            # Make it in range of ASCII from 32 to 126 
            # which will be space to ~
            encrypted_value = (ascii_value + int(key[j])) % (126 - 32 + 1) + 32
            #print("Encrypted input:", encrypted_value)
            
            # Convert back to char
            InputList[i] = chr(encrypted_value)
            j += 1

        # Convert InputList(List) back to Input(string)
        Input = ''.join(InputList)
        print("<Encrypt>"+Input+"<Encrypt>")
        
    keyFile.close


Cesar("Sussy oil",1)
