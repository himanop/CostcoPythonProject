import GSCashierRegister
import Employee
import ReceiptManagement
import UtilityFunctions

loopCheck = True
print("Costco Employee Login Screen")
while loopCheck == True:
    x=Employee.verifyCredentials()
    print(x)
    if x == True:
        check=True
        while check == True:
            UtilityFunctions.cls()
            print("Costco Options")
            print("1.Cash Register")
            print("2.Receipts")
            print("3.New Employee")
            print("0.Quit")
            choice=int(input("Enter option: "))
            if choice==1:
                GSCashierRegister.main()
            if choice==2:
                ReceiptManagement.main()
            if choice==3:
                Employee.createUser()
            if choice==0:
                loopcheck=False
                exit()
    else:
        print("Incorrect Credentials. 1 to Retry or 0 to quit")
        userNum=int(input("Enter option: "))
        if (userNum==1):
            continue
        if (userNum==0):
            loopCheck=False
            exit()