#Inventory list is dictionary object, top level dictionary keys are categories of items
#with in each category is another dictionary which contains itemname as keys and list as values
#In each list value info arranged is in format of itemnum,price,discountamt
import os
import InventoryManagement
import ReceiptManagement
import UtilityFunctions

inventory = InventoryManagement.createInventory()

PRODUCTCODEINDEX = 0
PRODUCTPRICEINDEX = 1
PRODUCTDISCOUNTINDEX = 2

#memberID = "";
userPurchasedItems = {}

#Allow user to select category and items. There are two loops. Category loop and item loop. User first selects the 
#category. Based on category inner loop of selecting items triggers and user remains in selecting items unless user comes
#out of it by selection option '0' at which point user goes back to selecting category. While selecting category user can 
#choose option of '0' to come out of item selection flow. When user comes out of item selection workflow, user selected
#items are printed
def main():
	global memberID
	memberID = getMemberID()
	selectCategory = True
	while selectCategory:
		selectedcategory = acceptCategory()
		if (selectedcategory == "0"):
			selectCategory = False
		else:
			selectitem = True
			while selectitem:
				selectedItemAndQty = acceptItem(selectedcategory)
				selectedItem = selectedItemAndQty[0]
				selectedQty = selectedItemAndQty[1]
				
				if (selectedItem == "0"):
					selectitem = False
				else:
					addItemToUserPurchasedItems(userPurchasedItems, selectedcategory, selectedItem, selectedQty)
	#printUserPurchasedItems(userPurchasedItems)
	#print(f'Total number of Categories purchased {len(userPurchasedItems)}')

	if (len(userPurchasedItems) > 0):
		print("*" * 50)
		printReceipt(memberID, userPurchasedItems)
	
def acceptCategory():
	UtilityFunctions.cls()
	if (len(userPurchasedItems) > 0):
		printUserPurchasedItems(userPurchasedItems)
		print("*" * 50)

	categorynum = 1
	categoryList = []
#	print("-" * 50)
	print("Select Category of Item to Purchase")
	for category in inventory:
		print(str(categorynum) + ". " + category)
		categoryList.append(category)
		categorynum = categorynum + 1
	print ("0. Quit")
	selectedcategorynum = -1
	while True:
		invalidInput = False
		try:
			selectedcategorynum = int(input("Input : "))
		except Exception:
			invalidInput = True
		if (selectedcategorynum >= categorynum):
			invalidInput = True
		if (invalidInput):
			print ("Invalid selection")
		else:
			break
	if (selectedcategorynum == 0):
		selectedcategory = "0"
	else:
		selectedcategory = categoryList[selectedcategorynum - 1]
	return selectedcategory

def acceptItem(selectedcategory):
	UtilityFunctions.cls()
	if (len(userPurchasedItems) > 0):
		printUserPurchasedItems(userPurchasedItems)
		print("*" * 50)		
	itemnum = 1
	itemList = []
	items = inventory[selectedcategory]
#	print("-" * 50)
	print ("Select item from " + selectedcategory + " Category")
	for item in items:
		print(str(itemnum) + ". " + item)
		itemList.append(item)
		itemnum = itemnum + 1
	print ("0. Return")
	selecteditemnum = -1
	while True:
		invalidInput = False
		try:
			selecteditemnum = int(input("Input : "))
		except Exception:
			invalidInput = True
		if (selecteditemnum >= itemnum):
			invalidInput = True
		if (invalidInput):
			print ("Invalid selection")
		else:
			break
				
		
		
# 	while (selecteditemnum >= itemnum):
# 		print ("Invalid selection")
# 		selecteditemnum = int(input("Input : "))
	if (selecteditemnum != 0):
		selecteditem = itemList[selecteditemnum - 1]
		
		
		
		
		
		
		
		
		selectedqty = input("Quantity[1] : ")
		if (selectedqty==None or selectedqty == ""):
			selectedqty = "1"
	else:
		selecteditem = "0"
		selectedqty = "0"
	selectedItemAndQty = [0,0]
	selectedItemAndQty[0] = selecteditem
	selectedItemAndQty[1] = selectedqty;
	return selectedItemAndQty

def addItemToUserPurchasedItems(userPurchasedItems, selectedcategory, selecteditem, selectedqty):
	#check if category already exists userPurchasedItems. If not add it and assign value of empty dictionary object
	if (userPurchasedItems.get(selectedcategory) == None):
		userPurchasedItems[selectedcategory] = {}
	categoryitems =  userPurchasedItems[selectedcategory]
	if categoryitems.get(selecteditem) != None:
		updatedQty = int(categoryitems[selecteditem]) + int(selectedqty)
	else:
		updatedQty = selectedqty
	categoryitems[selecteditem] = str(updatedQty)

def getMemberID ():
	UtilityFunctions.cls()
	memberID = input("Enter Member ID : ")
	return memberID

def printReceipt(memberID, userPurchasedItems):
	receiptFile = ReceiptManagement.getReceiptFileToWrite(memberID)
	strAddress1 = f'{"Costco Wholesale":^40s}'
	strAddress2 = f'{"Dedham #319":^40s}'
	strAddress3 = f'{"200 Legacy Blvd":^40s}'
	strAddress4 = f'{"Dedham, MA 02026":^40s}'
	print(strAddress1)
	print(strAddress2)
	print(strAddress3)
	print(strAddress4)
	print(" ")
	print("Member " + memberID)
	#write to receiptFile
	receiptFile.write(f'{strAddress1}\r\n')
	receiptFile.write(f'{strAddress2}\r\n')
	receiptFile.write(f'{strAddress3}\r\n')
	receiptFile.write(f'{strAddress4}\r\n')
	receiptFile.write("\r\nMember " + memberID + "\r\n")

	total = 0.00;
	for category in userPurchasedItems:
		items = userPurchasedItems[category]
		for item in items:
			itemList = inventory[category][item] 
			prdcode = itemList[PRODUCTCODEINDEX]
			prddesc = item
			prdqty = int(items[item])			
			prdprice = float(itemList[PRODUCTPRICEINDEX]) * prdqty
			prddiscount = float(itemList[PRODUCTDISCOUNTINDEX]) * prdqty
			total = total + prdprice
			strLineItem = f'{str(prdcode):10} {prddesc:20} {prdqty:<5} ${prdprice:7.2f}'
			print(strLineItem)
			receiptFile.write(f'{strLineItem}\r\n')
			if (prddiscount != 0.00):
				total = total - prddiscount
				strCouponLine = f'Coupon{"":31} ${prddiscount:7.2f}-'
				print(strCouponLine)
				receiptFile.write(f'{strCouponLine}\r\n')
	strTotalLine = f'{"*****TOTAL":37} ${total:7.2f}'
	print(strTotalLine)
	receiptFile.write(f'{strTotalLine}\r\n')
	input("\n\n Member Transaction Completed. Press Enter to Continue ")	
	
def printUserPurchasedItems(userPurchasedItems):
	categorynum = 1
	itemnum = 1
	print("*" * 50)
	print(f'User {memberID} Purchased Items')
	for category in userPurchasedItems:
		print(category)
		categorynum = categorynum + 1
		#reset itemnum to 1 to start printing items with numerical value of 1 when category changes
		itemnum=1
		items = userPurchasedItems[category]
		for item in items:
			itemList = inventory[category][item] 
			prdcode = itemList[PRODUCTCODEINDEX]
			prddesc = item			
			prdqty = int(items[item])			
			prdprice = float(itemList[PRODUCTPRICEINDEX]) * prdqty
			prddiscount = float(itemList[PRODUCTDISCOUNTINDEX]) * prdqty
			strLineItem = f'{str(prdcode):10} {prddesc:20} {prdqty:<5} ${prdprice:7.2f}'
			print(strLineItem)
			if (prddiscount != 0.00):
				strCouponLine = f'Coupon{"":31} ${prddiscount:7.2f}-'
				print(strCouponLine)
			itemnum = itemnum + 1
# def cls():
#     if os.system == "nt":
#         os.system('cls')
#     else:
#         os.system('clear')

		
#main()



