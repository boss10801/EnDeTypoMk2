# Welcome to EnDeTypoMk2
EnDeTypoMk2 is a Python-based encryption and decryption tool which transforms normal text into base64 and then applies a modified Caesar cipher.
## About this program
The EnDeTypoMk2 is design based on Caesar cipher(substitution cipher) which is shifting letter just like the first EnDeTypo that written in C language. But in this Mk2 variation, I design it to work with hbase64 encoder and my modified Caesar cipher.  
I have modified the Caesar cipher from shifting by just one number in plain text to shifting it with many random number in the key.txt file.  So let's say you have a word "Hello" and the key has the number "1534672" so the cipher text should be like this 
```
Plain text:  Hello
keys:        1534672
cipher text: Ijopu
```
In this program I will shift the plain text using ASCII as a reference but will only use it in range from 32 to 126 to ensure that it work properly in other operating systeam.  
Ref
![alt text](https://github.com/boss10801/EnDeTypoMk2/blob/main/ref/ascii-table.jpg?raw=true)  
But this might cause a little trouble since sometime the encrypted message can be cracked by using frequency analysis to map with the average frequency of occurrence in alphabet. So I add Hbase64 Encoder to encode all plain text before sendding to cipher in to base64 first.  
Ref
![alt text](https://github.com/boss10801/EnDeTypoMk2/blob/main/ref/base64_with_padding.png?raw=true)  
![alt text](https://github.com/boss10801/EnDeTypoMk2/blob/main/ref/1_1pdlgVGk55PMx8wLQiQl_g.png?raw=true)
By doing the encodeing process before encrpty the message it will make both Brute force and frequency analysis harder to crack it.
## How to use it
You just have to run it and make sure the the key.txt file is in the same location as this program file. You can also change the directory of the key file by editing the code in line 4
```
keyFilePath = 'key.txt'
```
It hase some basic UI for user to use it. press 1 to encrypt and press 2 to decrypt. if you input it already just copy and paste the plain text or cipher text and press enter.
## From Dev
Since it is a Symmetric encryption which uses a single key (Also know as secret key) to encrypt and decrypt the data. It can add more randomness in it to make sure that the data is safe. so if possible when You using this program you should find a good random generator and start random long enough number() which will be used in the encryption.  
This program still has flaw like can only shift from 0 to 9 but I'll improve it in the future.
