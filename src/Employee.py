from passlib.hash import pbkdf2_sha256
import os

PASSWORDFILE = "../masterdata/pwds.txt"
pwdDictionary = {}
    
def mainScreen():
    print("1. Create User")
    print("2. Verify Credentials")    
    print("0. Quit")        
    userSelection = int(input("Input : "))
    if (userSelection == 1):
        createUser()
    if (userSelection == 2):
        verifyCredentials()

def createUser():
    userName = ""
    while (userName == ""):
        userName = input("Enter User Name : ")
    passwordsMatch = False
    while (passwordsMatch == False):
        userPassword = ""        
        while (userPassword == ""):
            userPassword = input("Enter User Password : ")
        userPasswordAgain = ""
        while (userPasswordAgain == ""):
            userPasswordAgain = input("Enter User Password Again: ")
        if (userPassword == userPasswordAgain):
            passwordsMatch = True
        else:
            print("Passwords do not match")
    storePassword(userName, userPassword)
    input("User Created. Press Enter to Continue")
    
            
def storePassword(userName, userPassword):
#     salt = os.urandom(16)
#     combo_password = userPassword + str(salt)
#    hashed_password = bcrypt.hashpw(combo_password, salt)
    hashed_password = pbkdf2_sha256.hash(userPassword)
    pwdfile = open(PASSWORDFILE, "a")
    #:: is separator between username and hashedpwd in the file
    pwdfile.write(f'{userName}::{hashed_password}')
    pwdfile.write('\n')
    pwdfile.close()
#     print(f'{userName:<30} {hashed_password:<30}')
#     verifyPassword(userPassword, hashed_password)
    
def verifyPassword(userPassword, hashed_password):
    passwordOK = pbkdf2_sha256.verify(userPassword, hashed_password)
    return passwordOK
    
def verifyCredentials():   
    if (len(pwdDictionary) == 0):
        loadPasswordFile()
    userName = ""
    while (userName == ""):
        userName = input("Enter User Name : ")
    userPassword = ""
    while (userPassword == ""):
        userPassword = input ("Enter User password :")
    passwordOK = False
    if (pwdDictionary.get(userName) != None):
        hashed_password = pwdDictionary[userName]
        passwordOK = verifyPassword(userPassword, hashed_password)
        if passwordOK == True:
            print ("Credentials Passed")
        else:
            print ("Credentials Failed")
    else:
        print("User not found")
    return passwordOK
        
def loadPasswordFile():
    global pwdDictionary
    if not os.path.isfile(PASSWORDFILE):
        pwdFile = open(PASSWORDFILE, "w")
        pwdFile.close()
    with open(PASSWORDFILE, "r") as pwdFile:
        for line in pwdFile:
            if (len(line) > 0):
                linedata = line.rstrip('\n').split("::")
                pwdDictionary[linedata[0]] = linedata[1]
    pwdFile.close()
        
def main():    
    loadPasswordFile()
    mainScreen()
    
#main()
#verifyPassword("x", "$pbkdf2-sha256$50$nTNGiJFSKiXkvHfOmdPamw$UOxS85m4SehbbwBpy0WSwyjAlhCD/9zji..IW4y0VCI")