print("=============Computer Bazar============")
print("1. Dell(Rs:20000) 2. Toshiba(Rs: 30000) 3. Mac(Rs: 50000)")

option = int(input("select any option: "))

dell_price = 0
toshiba_price = 0
mac_price = 0
delivery_price = 0
plastic_price = 0
bag_price = 0
gift_price = 0
location_price = 0
tax_amt = 0
qt = 0

if option == 1:
    qt = int(input("enter quantity: "))
    dell_price += qt * 20000

elif option == 2:
    qt = int(input("enter quantity: "))
    toshiba_price += qt * 30000

elif option == 3:
    qt = int(input("enter quantity: "))
    mac_price += qt * 30000
else:
    print("Invalid selection")
    exit()

print("Delivery 1. Home(Rs: 1000) 2. Pickup(free)")
del_option = int(input("Select any option: "))
if del_option == 1:
    delivery_price += 1000

print("Packing 1. Plastic(Rs: 500) 2. Bag(Rs: 1000) 3. Gift Box(Rs: 5000)")
p_option = int(input("select any option: "))
if p_option == 1:
    plastic_price += 500
elif p_option == 2:
    bag_price += 1000
elif p_option == 3:
    gift_price += 5000
else:
    exit()

print("Location: 1. KTM(13%) 2. BKT(free) 3. LTP(free)")

l_option = int(input("enter your location: "))

total_price = dell_price + toshiba_price + mac_price
if l_option == 1:
    tax_amt += total_price * 0.13

gt = total_price + tax_amt + delivery_price + plastic_price + bag_price + gift_price

print(f"Quantity:{qt} Total:{total_price} Tax:{tax_amt} Grand Total:{gt}")
