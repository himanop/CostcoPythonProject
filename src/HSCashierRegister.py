costcoItems = {
	'Vegetable': { 
		'Red Potatoes':[83505,5.49,0],
		'Green Beans':[1089513,6.69,0],
		'Ham Rolls':[868210,0,0],
		'Carrots':[34567,3,0],
		'Tomato':[45672,2,0]
	},
	'Electronics':{
		'Speakers':[222256,100,10],
		'Google Home Hub':[45632, 249,0],
		'Acer chromebook':[34532, 300,0]
	},
	'Clothing':{
		'Shirt':[3334523,17,10],
		'Socks':[234456,8,0],
		'Pants':[445356,20,5],
		'Shoes':[324539,30,0],
	},
	'Toiletries':{
		'Toilet Paper':[23234,15,0],
		'Toothpaste':[20010,12,5],
		'Shaving Cream':[900023,20,0],
	}
}
x = 1
for key1 in costcoItems:
	print(str(x) + ".)" + key1)
	x = x+1

userChoice1 = int(input("Enter category to buy"))

if userChoice1 == 1:
	for key,value in costcoItems:
		