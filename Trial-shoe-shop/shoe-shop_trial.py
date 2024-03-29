from colorama import init, Fore
init()
print("HEY!!! THIS IS ZEBBYLION'S ONLINE SHOE SHOP\n")

while True:
    name = input("Enter your name please: ")
    if name:
        break
    else:
        print(Fore.RED + "Error: Name cannot be empty. Please try again.\033[0m")

print("Hello!!!" + Fore.YELLOW + name + "\033[0m\n" + "Welcome to our shop.")

brand = {
    "1": "Jordan",
    "2": "Nikes",
    "3": "Yeezys",
    "4": "Vans",
    "5": "Pradas"
}
show_brands = input(Fore.GREEN + "Press enter to see available brands\033[0m")
print("We have:")
print(f"1: {brand['1']}\n2: {brand['2']}\n3: {brand['3']}\n4: {brand['4']}\n5: {brand['5']}")


Jordans = ["Air-Jordan-1", "Jordan J11 Retro Concord (2018)", "Mens Air Jordan 9 Retro", "Air Jordan 3",
           "Women Jordan Air 1 Low SE", "Air Jordan v"]

Nikes = ["Airmax 95", "Air max 270Men", "Air-Force-1", "Nike Air Huarache", "Women Nike High Top", "nike dunk low"]

Yeezys = ["Yeezy 700", "Yeezy 350s", "Yeezy slides", "Yeezy powerphase", "YEEZY 450's", "Yeezy 500 Blush"]

Vans = ["Vans old skool", "Vans Men Sk8-Hi", "Vans Slip-on", "vans Authentic", "Vans Women high cut", "Vans Sk8-mid"]

Pradas = ["Prada cloudBust", "Prada Linea Rossa", "Prada cup", "Prada Punta Ala high", "Women Prada Pegasus",
          "Prada loafers"]


while True:
    try:
        pick = int(input("Which shoe brand is your favourite:(~enter number~):  "))
        if pick < 1 or pick > 5:
            raise ValueError
        break
    except ValueError:
        print(Fore.RED + f"Recheck and enter available brands\033[0m")

for j in Jordans:
    if pick == 1:
        print(Fore.BLUE + j + "\033[0m")

for n in Nikes:
    if pick == 2:
        print(Fore.BLUE + n + "\033[0m")

for y in Yeezys:
    if pick == 3:
        print(Fore.BLUE + y + "\033[0m")

for v in Vans:
    if pick == 4:
        print(Fore.BLUE + v + "\033[0m")

for p in Pradas:
    if pick == 5:
        print(Fore.BLUE + p + "\033[0m")

while True:
    type_shoe = input("Which shoe type in the above list would you want to buy:(~check spelling~):  ")
    if type_shoe:
        break
    else:
        print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

if type_shoe == Jordans[0]:
    print(f"{Jordans[0]} retails at" + Fore.BLUE + "$25.00\033[0m")

elif type_shoe == Jordans[1]:
    print(Jordans[1], "retails at" + Fore.BLUE + " $21.00\033[0m")

elif type_shoe == Jordans[2]:
    print(Jordans[2], "retails at" + Fore.BLUE + " $27.00\033[0m")

elif type_shoe == Jordans[3]:
    print(Jordans[3], "retails at" + Fore.BLUE + " $19.00\033[0m")

elif type_shoe == Jordans[4]:
    print(Jordans[4], "retails at" + Fore.BLUE + " $31.00\033[0m")

elif type_shoe == Jordans[5]:
    print(Jordans[5], "retails at" + Fore.BLUE + " $29.00\033[0m")

else:
    pass

if type_shoe == Nikes[0]:
    print(Nikes[0], "retails at" + Fore.BLUE + " $27.50\033[0m")

elif type_shoe == Nikes[1]:
    print(Nikes[1], "retails at" + Fore.BLUE + " $26.00\033[0m")

elif type_shoe == Nikes[2]:
    print(Nikes[2], "retails at" + Fore.BLUE + " $31.25\033[0m")

elif type_shoe == Nikes[3]:
    print(Nikes[3], "retails at" + Fore.BLUE + " $33.00\033[0m")

elif type_shoe == Nikes[4]:
    print(Nikes[4], "retails at" + Fore.BLUE + " $34.50\033[0m")

elif type_shoe == Nikes[5]:
    print(Nikes[5], "retails at" + Fore.BLUE + " $94.90\033[0m")

else:
    pass

if type_shoe == Yeezys[0]:
    print(Yeezys[0], "retails at" + Fore.BLUE + " $26.00\033[0m")

elif type_shoe == Yeezys[1]:
    print(Yeezys[1], "retails at" + Fore.BLUE + " $39.00\033[0m")

elif type_shoe == Yeezys[2]:
    print(Yeezys[2], "retails at" + Fore.BLUE + " $19.80\033[0m")

elif type_shoe == Yeezys[3]:
    print(Yeezys[3], "retails at" + Fore.BLUE + " $21.85\033[0m")

elif type_shoe == Yeezys[4]:
    print(Yeezys[4], "retails at" + Fore.BLUE + " $18.00\033[0m")

elif type_shoe == Yeezys[5]:
    print(Yeezys[5], "retails at" + Fore.BLUE + " $24.90\033[0m")

else:
    pass

if type_shoe == Vans[0]:
    print(Vans[0], "retails at" + Fore.BLUE + " $15.00\033[0m")

elif type_shoe == Vans[1]:
    print(Vans[1], "retails at" + Fore.BLUE + " $21.39\033[0m")

elif type_shoe == Vans[2]:
    print(Vans[2], "retails at" + Fore.BLUE + " $22.90\033[0m")

elif type_shoe == Vans[3]:
    print(Vans[3], "retails at" + Fore.BLUE + " $17.00\033[0m")

elif type_shoe == Vans[4]:
    print(Vans[4], "retails at" + Fore.BLUE + " $22.30\033[0m")

elif type_shoe == Vans[5]:
    print(Vans[5], "retails at" + Fore.BLUE + " $27.25\033[0m")

else:
    pass

if type_shoe == Pradas[0]:
    print(Pradas[0], "retails at" + Fore.BLUE + " $37.80\033[0m")

elif type_shoe == Pradas[1]:
    print(Pradas[1], "retails at" + Fore.BLUE + " $40.50\033[0m")

elif type_shoe == Pradas[2]:
    print(Pradas[2], "retails at" + Fore.BLUE + " $44.00\033[0m")

elif type_shoe == Pradas[3]:
    print(Pradas[3], "retails at" + Fore.BLUE + " $49.20\033[0m")

elif type_shoe == Pradas[4]:
    print(Pradas[4], "retails at" + Fore.BLUE + " $46.00\033[0m")

elif type_shoe == Pradas[5]:
    print(Pradas[5], "retails at" + Fore.BLUE + " $38.85\033[0m")

else:
    pass

while True:
    report = input("\nDid you find your best fit: (yes[y]~~no[n]): ")
    if report:
        break
    else:
        print(Fore.RED + "Cannot be empty\033[0m")

if report == 'yes' or report == 'y':
    while True:
        order = input("Do you want to place an order:(yes[y]~~no[n]): ")
        if order:
            break
        else:
            print(Fore.RED + "Cannot be empty\033[0m")

    if order == 'yes' or order == 'y':
        import datetime
        z = datetime.datetime.now()
        print(Fore.BLUE + f"{name}\033[0m" + Fore.GREEN + " your order has been successfully placed at\033[0m",
              z.strftime("%Y %b %d %A %H:%M:%S"))
        print(Fore.LIGHTMAGENTA_EX + "\nWe will contact you for more information on your order.\033[0m")
    else:
        pass

else:
    print(Fore.BLUE + f"Sorry {name} \033[0m.\n" +
          Fore.YELLOW + "You can come check later to find your best fit :). Welcome!!\n\033[0m")

print(Fore.GREEN + "\nTHANKS FOR VISITING ZEBBYLION'S ONLINE SHOE SHOP :)\033[0m" + Fore.BLUE + "\n"
      "Hope to see you again soon\033[0m")
