total = 0
username = input("Username: ")
password = input("Password: ")
if username == "asdf" and password == "1234":
    print("Login Success!!")
    while True:
        print("Wellcome to eShopping.")
        print("What would you like to buy?")
        print("----------------------------")
        print("1. Pencil 150 Bath")
        print("2. Pen 200 Bath")
        print("3. Stick 500 Bath")
        
        item = input("Choose item (Enter 1, 2, 3): ")
        if item =="1":
            total = total + 150
            print("+ Pencil in your shopping cart. (+150 Bath)")
        elif item =="2":
            total = total + 200
            print("+ Pen in your shopping cart. (+200 Bath)")
        elif item =="3":
            total = total + 500
            print("+ Stick in your shopping cart. (+500 Bath)")
        else:
            print("Error Pls choose again.")
            continue

        print (f"Total Price: {total} Bath")
    
        confirm = input ("Whold you want to check out. (y/n): ")

        if confirm.lower() == "y":
            print("Confirm order Thank for shopping.")
            break

        elif confirm.lower() == "n":
            print("Choose another item.")

else:
    print("Error invalid Username or Password")

print("-----------------------------------")
print(f"Total price: {total} Bath")
