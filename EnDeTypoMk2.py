def Cesar(Input, Type):
    with open('key.txt') as keyfile:
        key = keyfile.read()
    lenght = len(key)
    print(key)
    print(lenght)

Cesar(1,1)