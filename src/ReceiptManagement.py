import os
import datetime
import UtilityFunctions

#filenameextension = '.txt'
DATETIMEFORMAT = "%m/%d/%Y %I:%M:%S %p"
RECEIPTDIRECTORY = "../receipts/"
RECEIPTFILEEXTENSION = ".txt"
numberChoice = 0
memberNum = 0
secondGo = 0
def main():
	finalCheck = False
#	global secondGo
	global numberChoice
	global memberNum
	while finalCheck == False:
		UtilityFunctions.cls()
		print("Receipt Options")
		print("1. Get all receipts")
	#	print("2. Get specific receipt")
		print("2. Get all receipts for member")
		print("0. Quit")
		numberChoice = int(input("Choose receipt option: "))
		if (numberChoice==0):
			finalCheck=True
			exit()
		if (numberChoice==1):
			print("All receipts")
			getAllReceipts()
			finalCheck=True
# 		if (numberChoice==2):
# 			print("Print specific receipt")
# 			filename = input("Enter filename")
# 			if os.path.isfile(filename):
# 				printDetailsOfReceipt(filename)
# 			else:
# 				print("Enter valid filename")
		if (numberChoice==2):
			print("Print all receipts for member")
			memberNum = input("Enter member number")	
			getAllReceiptsForMember(memberNum)
			
def printReceipt(filename):
	filename = filename
#	os.startfile(filename, "print")

def generateReceiptName(memberId):
	#receiptFileName = "./receipts/12345T20181225064422.txt"
	receiptFileName = str(memberId) +"T"+ (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace('-',"").replace(':',"").replace('.',"").replace(" ", ""))
	receiptFileName = RECEIPTDIRECTORY + receiptFileName + RECEIPTFILEEXTENSION
	return receiptFileName

#returns fileobject which can be used to write directly
def getReceiptFileToWrite(memberId):
	receiptFileName = generateReceiptName(memberId)
	#below 2 lines to be used during boiler plate code only till receipt file name is getting generated properly
	#remove the file if it's found by that name so that a new receipt can be generated. 
	if os.path.isfile(receiptFileName):
		os.remove(receiptFileName)
	receiptFile = open(receiptFileName,"w+")
	return receiptFile


def getAllReceipts():
	UtilityFunctions.cls()
	global DATETIMEFORMAT
	global secondGo
	checkFiles = len(os.listdir(RECEIPTDIRECTORY))
	print("Returns all receipts stored in the system")
	if checkFiles>0:
		print(f'{"SNo":4}' f'{"MemberID":12}' f'{"Receipt file name":<30}' f'{"Date and time of the receipt":48}')
	if checkFiles==0:
		print("There are no receipts")
		main()
	x = 1
	sortDictionary = {}
# 	time={}
#  	time1=[]
	for filename in os.listdir(RECEIPTDIRECTORY):
		beforeT = filename.find('T')
		lenfile = (len(filename) - 4)
		time = (filename[beforeT + 1:lenfile])
		timeYear = time[0:4]
		timeMonth = time[4:6]
		timeDay = time[6:8]
		timeHour = time[8:10]
		timeMin = time[10:12]
		timeSec = time[12:14]
		fmemberID = filename[0:beforeT]
		receiptdatetime = datetime.datetime(int(timeYear), int(timeMonth), int(timeDay), int(timeHour), int(timeMin), int(timeSec))
		sortDictionary[receiptdatetime]=filename
	sortedKeys=sorted(sortDictionary.keys(),reverse=True)
	x=1
	files=[]
	for key in range(0,len(sortedKeys)):
		strformattedDate = sortedKeys[key].strftime(DATETIMEFORMAT)
		printfilename = sortDictionary[sortedKeys[key]]
		files.append(printfilename)
		fmemberID = printfilename[0:printfilename.find('T')]
		strLineData = f'{x:<4}' + f'{fmemberID:12s}' + f'{printfilename:<30}' + f'{strformattedDate:50s}'
		print(strLineData)
		x = x + 1

# 	print(time)
# 	time.sort(reverse=True)
# 	print(time)
	check=False
	while check == False and checkFiles>0:
		if secondGo == 0 :
			viewReceipt=input("Would you like to view a receipt?(Y/N)")
		else:
			viewReceipt = "y"
		if viewReceipt.lower() == "n":
			break
		elif viewReceipt.lower() == "y":
			SNo=int(input("Enter SNo:"))
			if SNo < x and x > 0:
				printDetailsOfReceipt(files[SNo-1])
				check = True
			else:
				print("Please enter valid SNo")
		else:
			print("Please enter valid option")
# 	if check == True:			
# 		printResponse = input("Would you like to print this receipt(Y/N)")
# 		check = True
# 		while check == True:
# 			if printResponse.lower() == "y":
# 			 	printReceipt(files[SNo-1])
# 			 	check = False
# 			elif printResponse.lower()== "n":
# 			 	check = False
# 			 	break
# 			else:
# 			 	print("Please enter valid response")
	main()


def getAllReceiptsForMember(memberID):
	UtilityFunctions.cls()
	titleCheck = len(os.listdir(RECEIPTDIRECTORY))
	if titleCheck > 0:
		print(f'{"SNO":4}' f'{"MemberID":12}' f'{"Receipt file name":<30}' f'{"Date and time of the receipt":48}')
	sortDictionary = {}
	global memberNum
	global secondGo
	global DATETIMEFORMAT
	for filename in os.listdir(RECEIPTDIRECTORY):	
		beforeT = filename.find('T')
		fmemberID = filename[0:beforeT]
		if int(fmemberID) == int(memberID):
# 			files.append(filename)
			lenfile = (len(filename) - 4)
			time = (filename[beforeT + 1:lenfile])
			timeYear = time[0:4]
			timeMonth = time[4:6]
			timeDay = time[6:8]
			timeHour = time[8:10]
			timeMin = time[10:12]
			timeSec = time[12:14]
			receiptdatetime = datetime.datetime(int(timeYear), int(timeMonth), int(timeDay), int(timeHour), int(timeMin), int(timeSec))
			sortDictionary[receiptdatetime] = filename
	sortedKeys = sorted(sortDictionary.keys(),reverse=True)
	x = 1
	files = []
	for key in range(0,len(sortedKeys)):
 		strformattedDate = sortedKeys[key].strftime(DATETIMEFORMAT)
 		printfilename = sortDictionary[sortedKeys[key]]
 		files.append(printfilename)
 		fmemberID = printfilename[0:printfilename.find('T')]
 		strLineData = f'{x:<4}' + f'{fmemberID:12s}' + f'{printfilename:<30}' + f'{strformattedDate:50s}'
 		print(strLineData)
 		x = x + 1

	check = False
	printCheck = False
	if len(files) == 0:
		print("No receipts for member number " + memberNum)
		repeat = input("Would you like to check receipts for different member(Y/N)")
		if repeat.lower() == 'y':
			memberNum = input("Enter member number:")
			getAllReceiptsForMember(memberNum)
		if repeat.lower() == 'n':
			main()
	while check == False:
		if secondGo == 0:
			viewReceipt = input("Would you like to view a receipt?(Y/N)")
		else:
			viewReceipt = "y"
		if viewReceipt.lower() == "n":
			printCheck = False
			break
		elif viewReceipt.lower() == "y":
			SNo = int(input("Enter SNo:"))
			if SNo < x and x > 0:
				printDetailsOfReceipt(files[SNo - 1])
				check = True
				printCheck = True
			else:
				print("Please enter valid SNo")
	if printCheck == True:			
		printResponse = input("Would you like to print this receipt(Y/N)")
		check = True
		while check == True:
			if printResponse.lower() == "y":
			 	printReceipt(files[SNo - 1])
			 	check = False
			elif printResponse.lower() == "n":
			 	break
			else:
			 	print("Please enter valid response")
def printDetailsOfReceipt(receiptFile):
	UtilityFunctions.cls()
	receiptFile = RECEIPTDIRECTORY + receiptFile
	global memberNum
	global secondGo
#	path = './receipts'
	print("Prints the contents of receiptFileName")
	with open(receiptFile,'r') as file_object:
		for line in file_object:
			print(line)
	check = False
	while check == False:
		toPrint=input("Would you like to print this receipt(Y/N)")
		if toPrint.lower()=='y':
			printReceipt(receiptFile)
			check = True
		elif toPrint.lower()=='n':
			input("Press Enter to continue")
			UtilityFunctions.cls()
			check = True
		else:
			print("Please enter valid choice")
			check = False
	toView=input("Would you like to view another receipt(Y/N)")
	check = False
	while check == False:
		if toView.lower()=='y':
			secondGo = secondGo + 1
			if int(numberChoice)==1:
				check = True
				UtilityFunctions.cls()
				getAllReceipts()
			elif int(numberChoice)==2:
				UtilityFunctions.cls()
				memberCheck=input("Would you like to view receipts for the same member?(Y/N)")
				if memberCheck.lower() == 'y':
					getAllReceiptsForMember(memberNum)
					check=True
				elif memberCheck.lower() == 'n':
					memberNum=input("Enter member number:")
					getAllReceiptsForMember(memberNum)
					check=True
		elif toView.lower()=='n':
			main()
		else:
			print("Please enter valid choice")
			check = False
	
