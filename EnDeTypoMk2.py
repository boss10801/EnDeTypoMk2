import os
import base64

keyFilePath = 'key.txt'

def openKeyfile(keyFile):
    # Is Empty?
    if (os.path.getsize(keyFile) == 0):
        print("\nError can't open key file.(terminate Program)\n")
        exit(1)
    # Open part
    with open(keyFilePath) as keyFile:
        key = keyFile.read()
    lenght = len(key)
    keyFile.close
    return lenght, key # Return as tuple

def cesarEncrypt(Input):
    lenght, key = openKeyfile(keyFilePath) #Unpack tuple
    InputList = list(Input)  
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
    return Input


def cesarDecrypt(Input):
    lenght, key = openKeyfile(keyFilePath) #Unpack tuple
    InputList = list(Input)  
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
    return Input



def encode(Input):
    # Encode the string to base64
    encodedByte = base64.b64encode(Input.encode('utf-8')) #come as byte
    # Decode the base64-encoded string
    encodedString = encodedByte.decode('utf-8')
    return encodedString

def decode(Input):
    # Decode the base64-encoded string
    decodedBytes = base64.b64decode(Input) #come as byte
    # Convert the bytes to a string
    decodedString = decodedBytes.decode('utf-8')
    return decodedString


# # Test Flow
# Input = "Hi"

# encore = encode(Input)
# print('Encode as:',encore)
# encry = cesarEncrypt(encore)
# print('Encrpt as:',encry)

# decry = cesarDecrypt(encry)
# print('Decrpt as:',decry)
# decore = decode(decry)
# print('Decode as:',decore)
