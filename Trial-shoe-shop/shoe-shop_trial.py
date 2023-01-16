print("HEEEY!!! THIS IS ZEBBYLION'S ONLINE SHOE SHOP\n")

name = input("Enter your name please: ")
for n in name:
    if not name:
        print("Cancelled...You MUST enter a name")
        break
    else:
        continue

print("Hello!!! " + name + "\n" + "Welcome to our shop :)\n")

# class ShoeShop


class ShoesShop:

    def __init__(self, brand):
        # initializing class ShoeShop
        self.brand = brand

    def available_brands(self):
        # function to print the available brands
        cont = input("Type ~yes~ to see brand available: ")
        for c in cont:
            if not c:
                print("Cancelled...You did NOT type yes")
                break
            else:
                continue
        print("\nWe have:" " " + self.brand + ".")


all_brands = ShoesShop("\n\tJordans\n\tNikes\n\tYeezys\n\tVans\n\tPradas")
all_brands.available_brands()


# brands = ["Jordans", "Nikes", "Yeezys", "Vans", "Pradas"]
# cont = input("Type ~yes~ to see the brands available: ")
# # out = False
# for c in cont:
#     if c == 'yes':
#         continue
#     # if c == 'no':
#         # out = True
#         # break
# print("\nWe have the:")
# for b in brands:
#     # if l == "Jordans" "Nikes" "Vans" "Yeezys" "Pradas":
#     print(b)
#  else:
# print("Brand not available :(\nPlease check the available brands")

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
Jordans = ["Air-Jordan-1", "Jordan J11 Retro Concord (2018)", "Mens Air Jordan 9 Retro", "Air Jordan 3", "Women Jordan Air 1 Low SE", "Air Jordan v"]

Nikes = ["Airmax 95", "Air max 270Men", "Air-Force-1", "Nike Air Huarache", "Women Nike High Top", "nike dunk low"]

Yeezys = ["Yeezy 700", "Yeezy 350s", "Yeezy slides", "Yeezy powerphase", "YEEZY 450's", "Yeezy 500 Blush"]

Vans = ["Vans old skool", "Vans Men Sk8-Hi", "Vans Slip-on", "vans Authentic", "Vans Women high cut", "Vans Sk8-mid"]

Pradas = ["Prada cloudBust", "Prada Linea Rossa", "Prada cup", "Prada Punta Ala high", "Women Prada Pegasus", "Prada loafers"]

# while True:
# try:
pick = input("Which shoe brand is your favourite:(~check spelling~):  ")
for p in pick:
    if not pick:
        print("Cancelled...You have to choose a brand ")
        break
    else:
        continue
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

for n in Nikes:
    if pick == 'Nikes':
        print(n)

for y in Yeezys:
    if pick == 'Yeezys':
        print(y)

for v in Vans:
    if pick == 'Vans':
        print(v)

for p in Pradas:
    if pick == 'Pradas':
        print(p)

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

type_shoe = input("Which shoe type in the above list would you want to buy:(~check spelling~):  ")
for t in type_shoe:
    if not t:
        print("Cancelled...You did NOT enter a shoe name")
        break
    else:
        continue

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
for r in report:
    if not r:
        break
    else:
        continue

if report == 'yes':
    order = input("Do you want to place an order:(yes/no): ")
    for o in order:
        if not o:
            break
        else:
            continue
    if order == 'yes':
        import datetime
        z = datetime.datetime.now()
        print("Your order has been successfully placed at", z.strftime("%Y %b %d %A %H:%M"))
        print("\nWe will contact you for more information on your order.")
    else:
        pass

else:
    print("Sorry :(\nYou can come check later to find your best fit :). Welcome!!\n")

print("\nTHANKS FOR VISITING ZEBBYLION'S ONLINE SHOE SHOP :)\nHope to see you again soon")
