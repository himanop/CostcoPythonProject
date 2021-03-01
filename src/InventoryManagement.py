def createInventory():
	filename = '../masterdata/CostcoInventory.csv'
	inventory = {}
	with open(filename,'r') as file_object:
		x = 0
		for line in file_object:
			if x == 0:
				x = x+1
				continue
			if line.strip() == ',,,,' or line.strip()=="":
			   	continue
			item = line.split(',')
			catholder = item[0]
			if item[0] != catholder:
				catholder = item[0]
			if inventory.get(catholder) == None: 
				inventory[catholder] = {}
				subcatholder = inventory[catholder]
			subcatholder[item[1].strip()] = item[2].strip(),item[3].strip(),item[4].strip('\n')
	return inventory

