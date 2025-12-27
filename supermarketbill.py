name = input("enter your name:")
lists = '''
rice      rs 10/kg
sugar     rs 8/kg
oil       rs 30/liter
salt      rs 25/kg
paneer    rs 40/kg
maggie    rs 12/pack
boost     rs 200/bottle
'''
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []
items = {'rice': 10,'sugar': 8,'oil': 30,'salt': 25,'paneer': 40,'maggie': 12,'boost': 200}
while True:
    option = input("press 1 for list or 2 to exit:")
if option == '2':
    print("thank you for shopping")
    break
elif option == '1':
    print(lists)
while True:
    inp1 = input("to buy press 1 or 2 to exit:")
    if inp1 == '2':
        print("thank you for shopping")
        break
    elif inp1 == '1':
        item = input("choose your items:").lower()
while True:
    quantity_input = input("enter quantity:")
    if quantity_input.isdigit():
        quantity = int(quantity_input)
        break
    else:
        print("please enter a valid quantity")
        if item in items:
            price = quantity*items[item]
            pricelist.append((item, quantity, items[item], price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
        else:
            print("selected item is not available sorry for the inconvenience")
            if totalprice > 0:
                tax = (totalprice*12)/100
                finalamount = tax + totalprice
                print(25* "=", "pythonlife supermarket", 25* "=")
                print(28* "," "hyderabad")
                print("name:", name, 30* "")
                print(75* "-")
                print("sno", 10* "", 'items', 8* "", 'quantity', 8* "", 'price')
                for i in range(len(pricelist)):
                    print(i,13* "", ilist[i],8* "", qlist[i], 8* "", plist[i])
                    print(75* "-")
                    print(50* "", 'total amount:', 'rs', totalprice)
                    print("tax amount", 50* "", 'rs', tax)
                    print(75* "-")
                    print(50* "", 'final amount:', 'rs', finalamount)
                    print(75* "-")
                    print(20* "", "thank you & visit again")
                    print(75* "-")                