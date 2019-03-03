# -*- coding: utf-8 -*-
import random, time, os, datetime
from hurry.filesize import size

number = input('Number of generated keys: ') # Создаём переменную и помещаем в нее количество паролей для генерации

passHistory = [] # Создаём пустой массив, в который потом поместим все наши пароли




x = True # Создаём переменную для контроля нашего главного цикла

while x:
    upperOne = chr(random.randint(65, 90))
    upperTwo = chr(random.randint(65, 90))
    lowerOne = chr(random.randint(97, 122))
    lowerTwo = chr(random.randint(97, 122))
    digitOne = chr(random.randint(48, 57))
    digitTwo = chr(random.randint(48, 57))

    passList = [upperOne, upperTwo, lowerOne, lowerTwo, digitOne, digitTwo]

    random.shuffle(passList)

    password1 = "".join(passList)
    passHistory.append(password1)

    #print(passHistory)

    #time.sleep(0.1)

    if (len("".join(passHistory)) == number * 6):
        x = False

file_name = "passwords " + str(datetime.datetime.now().time()) + " .txt"
os.mknod (file_name) 

with open(file_name, 'w') as f:
    for item in passHistory:
        f.write("%s\n" % item)

sizeFile = os.path.getsize(file_name)

print('----------------------------------------------------------')
print('Num of keys: \t' + str(number) + '\n' + '\nFirst key : \t' + passHistory[0] + '\n' + '\nFilesize : \t' + str(sizeFile) + ' bytes or ' + str(size(sizeFile)))
print('----------------------------------------------------------')
