# -*- coding: utf-8 -*-
import random, time, os, datetime
from hurry.filesize import size 

###################################

isRunning = True

while isRunning:

    print('----------------------------------------------------------')
    print('1. Сгенерировать новый сборник паролей.')
    print('2. Сравнить два файла.')
    print('...')
    print('0. Выход')
    print('----------------------------------------------------------')


    generalInput = input()

   

    def passwordGenerator():

        number = input('\nКоличество паролей: ')
        keySize = input('Длина паролей: ')

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
        print('Количество паролей : \t\t' + str(number) + '\n' + '\nПервый пароль в файле : \t' + passHistory[0] + '\n' + '\nПримерный размер файла : \t' + str(sizeFile) + ' байт или ' + str(size(sizeFile)))
        print('----------------------------------------------------------\n')
        print('Пароли сохранены в папке со скриптом!\n')




###################################
 
    if generalInput == 0:

        exit()

    elif generalInput == 1:

        passwordGenerator()

    elif generalInput == 2:

        print('2')