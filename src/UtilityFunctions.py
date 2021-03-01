import os
def cls():
    print('Cls')
    osPlatform = os.system
    if osPlatform == "nt":
        os.system('cls')
    else:
        os.system('clear')

cls()
