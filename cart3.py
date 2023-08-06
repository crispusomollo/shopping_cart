cart = {} #Dictionary
print("Welcome to the Shopping Cart Program!")
 
while True:
    print()
    print ("Please type in one of these options")
    print ("1. Add item ")
    print ("2. View cart ")
    print ("3. Remove item ")
    print ("4. Compute total ")
    print ("5. Quit application ")
  
    print()
    select = int(input(" Type in a number to go on "))
    print()
 
    if select == 1:
        item = input(" What would you like to add?  ")
        price = float(input(" Type in the price "))
        cart [item] = price
        print(f" {item} costing ${price} has been added to your cart.")
        #print(f" The price of {item} is ${price} ")
 
    if select == 2:
        print("This is what is in your shopping cart")
        for item in cart:
            print(f"  {item} - ${cart [item]}")
 
    if select == 3:
        takeout = input(" Type in what you would like to remove? ")
        cart.pop(takeout)
        print(f" {takeout} has been removed from your cart" )
 
    if select == 4:
        total = 0
        for item in cart:
            total += cart [item]
        print(f" The total cost of items in the cart is ${total}")
 
    if select == 5:
        print ("Comeback soon.")
        #quit()
        break

