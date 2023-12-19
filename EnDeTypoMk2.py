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
    if (Type == 1): #Encrypt
        i,j = 0,0
        print("i=",i,"j=",j)


    keyFile.close

Cesar(1,1)