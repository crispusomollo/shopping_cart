cart = {} #Dictionary
print("Welcome to the Shopping Cart Program!")
 
while True:
    print()
    print ("Please type in one of these")
    print ("1. Add item ")
    print ("2. View cart ")
    print ("3. Remove Item ")
    print ("4. compute total")
    print ("5. exit program")
  
    select = int(input(" Type in a number to go on "))
 
    if select == 1:
        item = input(" What would you like to add?  ")
        price = float(input(" type in the price "))
        cart [item] = price
        print(f"'{item}' has been added to your cart.")
        print(f" The price is ${price}")
 
    if select == 2:
        print("This is what is in your shopping cart")
        for item in cart:
            print(f"  {item} - ${cart [item]}")
 
    if select == 3:
        takeout = input(" Type in what you would like to remove?  ")
        cart.pop(takeout)
 
    if select == 4:
        total = 0
        for item in cart:
            total += cart [item]
        print(f" ${total}")
 
    if select == 5:
        print ("comeback soon.")
        break
