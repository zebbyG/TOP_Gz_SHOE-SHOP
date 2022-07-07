print("THIS IS ZEBBYLION'S ONLINE SHOE SHOP\n")

name = input("Enter your name please: ")

print("Hello!!! " + name + "\n" + "Welcome to our shop :)\n")

# cont = input("Type ~yes~ to see the brand we have: ")

brands = ["Jordans", "Nikes", "Yeezys", "Vans", "Pradas"]
cont = input("Type ~yes~ to see the brands available: ")
# out = False
for c in cont:
    if c == 'yes':
        continue
    # if c == 'no':
        # out = True
        # break
print("\nWe have the:")
for b in brands:
    # if l == "Jordans" "Nikes" "Vans" "Yeezys" "Pradas":
    print(b)
    # else:
    #    print("Brand not available :(\nPlease check the available brands")

# print("\nThese are the brands available at our shop at the momement\n")

# class Shoesshop:
    # def __init__(self, brand):
    #  self.brand = brand
    # def shoe_sale(self):
    # print("We have:" " "  + self.brand + ".")
# availablebrands = Shoesshop("Jordans, Nikes, Yeezys, Vans and Pradas")
# availablebrands.shoe_sale()
# while True:
    # try:
#       pick = str(input("Which shoe brand is your favourite:(~check spelling~):  "))
    # break
    # except NameError:
    # print("You did not enter any of the available brands")
    # except:
    # print("An unknown error occured please try again")
Jordans = ["jordan i", "jordan 11", "Mens Air Jordan 9 Retro", "jordan iii", "Women Jordan Air 1 Low SE", "Jordan v"]

Nikes = ["Airmax", "Air max 270Men", "Air Jordan", "air max 95", "Nike Air", "nike dunk low"]

Yeezys = ["Yeezy 700", "Yeezy 350s", "Yeezy slides", "Yeezy powerphase", "Yeezy BOOST 350v2", "Yeezy 500 Blush"]

Vans = ["Vans old skool", "Vans Sk8-Hi", "Vans Slip-on", "vans Authentic", "Vans Era", "Vans Sk8"]

Pradas = ["Prada cloudBust", "Prada Linea Rossa", "Prada cup", "Prada Punta Ala", "Prada Sport", "Prada loafers"]

# while True:
# try:
pick = input("Which shoe brand is your favourite:(~check spelling~):  ")
# for b in brands:
#     for p in pick:
#         if p != b:
#             break
#     else:
#         continue
#     break
# for p in pick:
#     if pick == Jordans or pick == Vans or pick == Pradas or pick == Yeezys or pick == Nikes:
#         continue
#     if pick != brands:
#          raise NameError("Brand not available\nCheck spelling and re-enter again")

# break
# except TypeError:
# print("You did not enter any of the available brands")
# except:
# print("An unknown error occured please try again")
# for l in brands:
# while l == "Jordans" "Nikes" "Vans" "Yeezys" "Pradas":
# print(l)
# else:
# print("Brand not available :(\nPlease check the available brands")
# break

# if l == "Jordans" "Nikes" "Vans" "Yeezys" "Pradas":
# print(l)
# else:
# print("Brand not available :(\nPlease check the available brands")
# break
# for l in brands:
# if pick != "Prada" "Vans" "Yeezys" "Nikes" "Jordans":
# print("Brand not available :(\nPlease check the available brands")
# break
# else:
# pass

for j in Jordans:
    if pick == 'Jordans':
        print(j)
# print("\nThese are some of the Jordan shoes we have")

for n in Nikes:
    if pick == 'Nikes':
        print(n)
# print("\nThese are some of the Nikes shoes we have")

for y in Yeezys:
    if pick == 'Yeezys':
        print(y)
# print("\nThese are some of the Yeezys shoes we have")

for v in Vans:
    if pick == 'Vans':
        print(v)
# print("\nThese are some of the Vans shoes we have")

for p in Pradas:
    if pick == 'Pradas':
        print(p)
# print("\nThese are some of the Pradas shoes we have")

# else:
    # pass
    # print("Brand not available at the moment :( \n CHECK LATER")
# brand_picked = input("Did the brand you enterd list the shoes available in the shop:(yes/no): ")
# for s in 'Shoeshop':
    # if brand_picked == 'yes':
        # continue
    # elif brand_picked == 'no':
        # print("Check the brand spelling and try again :)")
    #    break

type_shoe = input("Which shoe type in the above list do you want to buy:(~check spelling~):  ")

if type_shoe == Jordans[0]:
    print(Jordans[0], "retails at $25.00")

elif type_shoe == Jordans[1]:
    print(Jordans[1], "retails at $21.00")

elif type_shoe == Jordans[2]:
    print(Jordans[2], "retails at $27.00")

elif type_shoe == Jordans[3]:
    print(Jordans[3], "retails at $19.00")

elif type_shoe == Jordans[4]:
    print(Jordans[4], "reatils at $31.00")

elif type_shoe == Jordans[5]:
    print(Jordans[5], "retails at $29.00")

else:
    pass
    # print("Shoe out of stock or shoe is not in the jordan brand")

if type_shoe == Nikes[0]:
    print(Nikes[0], "retails at $27.50")

elif type_shoe == Nikes[1]:
    print(Nikes[1], "retails at $26.00")

elif type_shoe == Nikes[2]:
    print(Nikes[2], "retails at $31.25")

elif type_shoe == Nikes[3]:
    print(Nikes[3], "retails at $33.00")

elif type_shoe == Nikes[4]:
    print(Nikes[4], "retails at $34.50")

elif type_shoe == Nikes[5]:
    print(Nikes[5], "retails at $94.90")

else:
    pass
    # print("Shoe out of stock or shoe is not in the Nikes brand")

if type_shoe == Yeezys[0]:
    print(Yeezys[0], "retails at $26.00")

elif type_shoe == Yeezys[1]:
    print(Yeezys[1], "retails at $39.00")

elif type_shoe == Yeezys[2]:
    print(Yeezys[2], "retails at $19.80")

elif type_shoe == Yeezys[3]:
    print(Yeezys[3], "retails at $21.85")

elif type_shoe == Yeezys[4]:
    print(Yeezys[4], "retails at $18.00")

elif type_shoe == Yeezys[5]:
    print(Yeezys[5], "retails at $24.90")

else:
    pass
    # print("Shoe out of stock or shoe is not in the Yeezys brand")

if type_shoe == Vans[0]:
    print(Vans[0], "retails at $15.00")

elif type_shoe == Vans[1]:
    print(Vans[1], "retails at $21.39")

elif type_shoe == Vans[2]:
    print(Vans[2], "retails at $22.90")

elif type_shoe == Vans[3]:
    print(Vans[3], "retails at $17.00")

elif type_shoe == Vans[4]:
    print(Vans[4], "retails at $22.30")

elif type_shoe == Vans[5]:
    print(Vans[5], "retails at $27.25")

else:
    pass
    # print("Shoe out of stock or shoe is not in the Vans brand")

if type_shoe == Pradas[0]:
    print(Pradas[0], "retails at $37.80")

elif type_shoe == Pradas[1]:
    print(Pradas[1], "retails at $40.50")

elif type_shoe == Pradas[2]:
    print(Pradas[2], "retails at $44.00")

elif type_shoe == Pradas[3]:
    print(Pradas[3], "retails at $49.20")

elif type_shoe == Pradas[4]:
    print(Pradas[4], "retails at $46.00")

elif type_shoe == Pradas[5]:
    print(Pradas[5], "retails at $38.85")

else:
    pass
    # print("Shoe out of stock or shoe is not in the Prada brand")


report = input("\nDid you find your best fit: "
               "(yes/no): ")

if report == 'yes':
    order = input("Do you want to place an order:(yes/no): ")
    if order == 'yes':
        import datetime
        z = datetime.datetime.now()
        print("Your order has been successfully placed at", z)
        print("\nWe will contact you for more information on your order.")
    else:
        pass

else:
    print("Sorry :(\nYou can come check later to find your best fit :). Welcome!!\n")

print("\nTHANKS FOR VISITING ZEBBYLION'S ONLINE SHOE SHOP :)\nHope to see you again soon")
