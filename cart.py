import pprint

kikapu = {}
print("This is a Shopping Cart!")
 
while True:
    print()
    print ("Please type in one of these options: ")
    print ("1. Add your item ")
    print ("2. View your cart ")
    print ("3. Remove an item: ")
    print ("4. Calculate total: ")
    print ("5. Quit the program! ")
  
    print()
    option = int(input(" Type in a number to proceed "))
    print()

    #options = ['1','2','3','4','5']
    #if option not in options:
        #print('That option is not valid. Enter either 1, 2, 3, 4 or 5')
        #continue
    
    if option == 1:
        
        bidhaa = input(" What would you like to add to your cart? ")
        shingapi = float(input(" Type in the price of the item added: "))
        kikapu [bidhaa] = shingapi
        print(f" {bidhaa} costing KShs {shingapi} has been added to cart.")
 
    if option == 2:
        
        bidhaa = 0

        for bidhaa in kikapu:
            None
            
        if bidhaa == 0:
            print(" There are no Items in your cart!")
        else:
            print("These are the items in your shopping cart:")
            print('-' * 45)
            for bidhaa in kikapu:
                print(f" {bidhaa} - KShs {kikapu [bidhaa]}")
            #for bidhaa in range(len(kikapu)):
                #print('Item' + str(bidhaa) + ' in the cart is: ' + kikapu[bidhaa])
            print('-' * 45)
            pprint.pprint(kikapu)
            
    if option == 3:
        
        ondoa = input(" Type in the item you would like to remove from cart: ")

        if ondoa == '':
            print()
            print("You have not entered an item")
            continue
        elif ondoa not in kikapu:
            print()
            print('That item is not in your cart. Below are items in the cart:')
            print()
            pprint.pprint(kikapu)
            continue
        else:
            kikapu.pop(ondoa)
            #kikapu.remove(ondoa)
            print()
            print(f" {ondoa} has been removed from your cart" )
 
    if option == 4:
        
        jumla = 0
        
        for bidhaa in kikapu:
            jumla += kikapu [bidhaa]
            print(f" {bidhaa} - KShs {kikapu [bidhaa]}")
            
        if jumla == 0:
            print("Your cart is empty!")
        else:
            if jumla >= 50000:
                discount = jumla * 0.09
                jumla = jumla - discount
                print()
                print(f" Discount : {discount}")
                print('-' * 30)
                print(f"  Total cost: KShs {jumla} ")
                print('-' * 30)
            elif jumla >= 20000:
                discount = jumla * 0.06
                jumla = jumla - discount
                print()
                print(f" Discount : {discount}")
                print('----------------------------')
                print(f"  Total cost: KShs {jumla} ")
                print('----------------------------')   
            elif jumla >= 10000:
                discount = jumla * 0.03
                jumla = jumla - discount
                print()
                print(f" Discount : {discount}")
                print('----------------------------')
                print(f"  Total cost: KShs {jumla} ")
                print('----------------------------')
            else:
                print('----------------------------')
                print(f"  Total cost: KShs {jumla} ")
                print('----------------------------')
 
    if option == 5:
        
        print ("Thank you for shopping with us.")
        #quit()
        break
    
    #else:
        #print("That is not a valid entry. Try again")
        #break

