cart = {}
print("This is a Shopping Cart!")
 
while True:
    print()
    print ("Please type in one of these options: ")
    print ("1. Add an item ")
    print ("2. View your cart ")
    print ("3. Remove an item: ")
    print ("4. Calculate total: ")
    print ("5. Quit the application ")
  
    print()
    option = int(input(" Type in a number to proceed "))
    print()
 
    if option == 1:
        item = input(" What would you like to add in your cart?  ")
        price = float(input("Type in the price of the item added: "))
        cart [item] = price
        print(f" {item} costing ${price} has been added successfully to your cart.")
 
    if option == 2:
        print("These are the items in your shopping cart: ")
        for item in cart:
            print(f"  {item} - ${cart [item]}")
 
    if option == 3:
        remove = input(" Type in the item you would like to remove from your cart: ")
        cart.pop(remove)
        print(f" {remove} has been removed from your cart" )
 
    if option == 4:
        total = 0
        for item in cart:
            total += cart [item]
        print(f" The total cost of items in the cart is ${total}")
 
    if option == 5:
        print ("Thank you for visiting my cart.")
        #quit()
        break

