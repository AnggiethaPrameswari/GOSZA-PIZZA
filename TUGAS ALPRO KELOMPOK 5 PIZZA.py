
# TUGAS KELOMPOK ALPRO PIZZA

print("WELCOME GOSZA LOVERS PIZZA")

nama = input("Enter Your Name: ")
print("Hello", nama, "what do you want to order?")

print("""
    MENU PIZZA
    1: Super Supreme  \t\tRp.50000
    2: Meat Monsta    \t\tRp.65000
    3: Veggie Garden  \t\tRp.70000
    4: Cheese Lovers  \t\tRp.60000
    5: Tuna Melt      \t\tRp.80000
    6: Pepperoni      \t\tRp.75000
      """)


bill = 0
PesananPizza = ""
hargaPesananPizza = 0
PesananCrust = ""
hargaPesananCrust = 0
PesananSize = ""
hargaPesananSize = 0
ExtraCheese = ""
hargaExtraCheese = 0

while True:
    #input pemilihan menu pizza
    pilihan = int(input("Select Your Pizza according to the number on the menu: "))

    #jika memilih menu nomor 1 harga ditambah 50000
    if pilihan == 1:
        bill += 50000
        PesananPizza += "Super Supreme"
        hargaPesananPizza += 50000
        break

    #jika memilih menu nomor 2 harga ditambah 65000
    elif pilihan == 2:
        bill += 65000
        PesananPizza += "Meat Monsta"
        hargaPesananPizza += 65000
        break

    #jika memilih menu nomor 3 harga ditambah 70000
    elif pilihan == 3:
        bill += 70000
        PesananPizza += "Veggie Garden"
        hargaPesananPizza += 70000
        break

    #jika memilih menu nomor 4 harga ditambah 60000
    elif pilihan == 4:
        bill += 60000
        PesananPizza += "Cheese Lovers"
        hargaPesananPizza += 60000
        break
    
    #jika memilih menu nomor 5 harga ditambah 80000
    elif pilihan == 5:
        bill += 80000
        PesananPizza += "Tuna Melt"
        hargaPesananPizza += 80000
        break

    #jika memilih menu nomor 6 harga ditambah 75000
    elif pilihan == 6:
        bill += 75000
        PesananPizza += "Pepperoni"
        hargaPesananPizza += 75000
        break
    #jika tidak memilih menu diantara nomor 1-6 maka akan memilih ulang menu
    else:
        print("Menu Pizza Not Available")
        print("Please enter the correct number")


print("""
CRUST PIZZA
    1: Crown Crust \t\t\tRp.5000
    2: Pan Crust \t\t\tRp.10000
    3: Cheesy Bite Crust \t\tRp.20000
      """)

while True:
    #input pemilihan menu crust pizza
    pilihan = int(input("Select The Crust according to the number on the menu: "))

    #jika memilih menu nomor 1 harga ditambah 5000
    if pilihan == 1:
        bill += 5000
        PesananCrust += "Crown Crust"
        hargaPesananCrust += 5000
        break

    #jika memilih menu nomor 2 harga ditambah 10000
    elif pilihan == 2:
        bill += 10000
        PesananCrust += "Pan Crust"
        hargaPesananCrust += 10000
        break

    #jika memilih menu nomor 3 harga ditambah 20000
    elif pilihan == 3:
        bill += 20000
        PesananCrust += "Cheese Bite Crust"
        hargaPesananCrust += 20000
        break

    #jika tidak memilih menu diantara nomor 1-3 maka akan memilih ulang menu
    else:
        print("Menu Crust Not Available")
        print("Please enter the correct number")
    
print("""
    UKURAN PIZZA
    1: Small \t\tRp.0
    2: Medium \t\tRp.8000
    3: Large \t\tRp.15000
    """)

while True:
    #input pemilihan ukuran pizza
    pilihan = int(input("Select Pizza Size according to the number on the menu: "))

    #jika memilih ukuran nomor 1 (small) maka tidak ada tambahan harga
    if pilihan == 1:
        bill += 0
        PesananSize = "small"
        hargaPesananSize += 0
        break

    #jika memilih ukuran nomor 2 (medium) maka harga ditambah 8000
    elif pilihan == 2:
        bill += 8000
        PesananSize = "medium"
        hargaPesananSize += 8000
        break
        
    #jika memilih ukuran nomor 3 (large) maka harga ditambah 15000
    elif pilihan == 3:
        bill += 15000
        PesananSize = "large"
        hargaPesananSize += 15000
        break

    #jika tidak memilih ukuran diantara nomor 1-3 maka akan memilih ulang ukuran pizza
    else:
        print("Pizza Size Not Available")
        print("Please enter the correct number")
    
    #Memilih extra keju atau tidak
ExtraCheese = input("Do you wan't Extra Cheese? (yes/no) ")

#jika "yes" maka harga ditambah 13000
if ExtraCheese == "yes":
    hargaExtraCheese += 13000
    bill += 13000
    ExtraCheese = "You Add Extra Cheese"

#jika "no" maka tidak ada biaya tambahan untuk extra cheese
else:
    ExtraCheese = "You Don't Add Extra"
    

print(f"{nama}'s Order: ")
print(f"{PesananPizza} - Rp{hargaPesananPizza}")
print(f"{PesananCrust} - Rp{hargaPesananCrust}")
print(f"{PesananSize} - Rp{hargaPesananSize}")
print(f"{ExtraCheese} - Rp{hargaExtraCheese}")
print(f"Total Bill: - Rp{bill}")
print("Thank you for order at Gosza Lovers Pizza. Please wait for your order")




