# -*- coding: utf-8 -*-
import random, time, os, datetime
from hurry.filesize import size 

number = input('Number of generated keys: ')
keySize = input('Size of generated keys: ')

passHistory = []

for x in range(number):

    passBuffer = []

    for x in range(keySize):
        charGenerator = chr(random.randint(33, 122))
        passBuffer.append(charGenerator)

    passBufferJoined = "".join(passBuffer)
    passHistory.append(passBufferJoined)

file_name = "passwords " + str(datetime.datetime.now().time()) + " .txt"
os.mknod (file_name) 

with open(file_name, 'w') as f:
    for item in passHistory:
        f.write("%s\n" % item)

sizeFile = os.path.getsize(file_name)

print('----------------------------------------------------------')
print('Num of keys: \t' + str(number) + '\n' + '\nFirst key : \t' + passHistory[0] + '\n' + '\nFilesize : \t' + str(sizeFile) + ' bytes or ' + str(size(sizeFile)))
print('----------------------------------------------------------')
