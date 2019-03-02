import random, time, os

number = input()

passHistory = []

x = True

os.mkdir('pass')
os.chdir('pass')
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

    time.sleep(0.1)

    if (len("".join(passHistory)) == number * 6):
        x = False

os.mknod("passwords.txt")

with open('passwords.txt', 'w') as f:
    for item in passHistory:
        f.write("%s\n" % item)

print('\nNumbers of genereted keys: ' + str(number))
    