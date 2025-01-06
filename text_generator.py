import random
import os

print("Welcome to JP's random text generator!")
if not os.path.exists("setup.txt"):
    print("As this is your first setup, please provide the information requested below. After that, refer to 'setup.txt'.")
    modus = input("Should the file be refreshed or appended? ['w'/'a'] If unsure, type 'w'. ")
    count = int(input("How many characters should be generated? "))
    with open("setup.txt", mode="w") as file:
        file.write(f'mode:{modus}\ncount:{count}')
else:
    with open("setup.txt", mode="r") as file:
        content = file.readlines()
        modus = content[0].split(":")[1].strip()
        count = int(content[1].split(":")[1])

alphabet = "abcdefghijklmnopqrstuvwxyz "
with open("output.txt", mode=f'{modus}') as file:
    for i in range(count):
        file.write(alphabet[random.randint(0,len(alphabet)-1)])

