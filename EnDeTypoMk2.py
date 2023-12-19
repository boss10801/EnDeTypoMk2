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

            # Make it in range of ASCII from 32 to 126 
            # which will be space to ~
            encrypted_value = (ascii_value + int(key[j]))
            if (encrypted_value>126):
                temp = encrypted_value - 126    # Return as Possitive Number
                encrypted_value = 32 + temp     # from 127 to 1

            #print(ascii_value ,"->", encrypted_value)
            
            # Convert back to char
            InputList[i] = chr(encrypted_value)
            j += 1

        # Convert InputList(List) back to Input(string)
        Input = ''.join(InputList)
        print("<Encrypt>"+Input+"<Encrypt>")
    elif (Type == 2): #Decrypt
        i,j = 0,0
        for i in range(len(InputList)):
            if(j == lenght):
                j = 0
            # Convert InputList to ASCII
            ascii_value = ord(InputList[i])

            # Make it in range of ASCII from 32 to 126 
            # which will be space to ~
            decrypted_value = (ascii_value - int(key[j])) # change from + to -
            if (decrypted_value<32):
                temp = decrypted_value - 32     # Return as Negative Number
                decrypted_value = 126 + temp    # from -1 to 125

            #print(ascii_value ,"->", decrypted_value)
            
            # Convert back to char
            InputList[i] = chr(decrypted_value)
            j += 1

        # Convert InputList(List) back to Input(string)
        Input = ''.join(InputList)
        print("<Decrypt>"+Input+"<Decrypt>")
        
    keyFile.close


Cesar("As my mom said No SHOOTING IN OUR 101 Battlion",1)
Cesar("C{&t$$usn&uiok)Rw$TNQWZPWK(MO&Q]X':49$Cgv|rpxr",2)
#Sussy oil
#<En>u>:;CD8..<En>