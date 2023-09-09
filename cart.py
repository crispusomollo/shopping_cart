import sys
import pprint
from termcolor import colored
#from colorama import Fore, Back, Style
#from colored import fg

kikapu = {}
print("This is a very simple Shopping Cart!")
 
while True:
    print()
    print ("Please type in one of these options: ")
    print ("1. Add your item ")
    print ("2. View your cart ")
    print ("3. Remove an item: ")
    print ("4. Calculate total: ")
    print ("5. Quit the program! ")
  
    print()
    chaguo = int(input(" Type in a number to proceed "))
    print()

    #chaguzi = ['1','2','3','4','5']
    chaguzi = (1,2,3,4,5)
    if chaguo not in chaguzi:
        print('That option is not valid. Enter either 1, 2, 3, 4 or 5')
        #continue
        #break
    
    if chaguo == 1:
        
        bidhaa = input(" What would you like to add to your cart? ")
        shingapi = float(input(" Type in the price of the item added: "))
        kikapu [bidhaa] = shingapi
        print(f" {bidhaa} costing KShs {shingapi} has been added to cart.")
 
    if chaguo == 2:
        
        bidhaa = 0

        for bidhaa in kikapu:
            None
            
        if bidhaa == 0:
            ujumbe = colored('There are no items in your cart!', 'red', attrs=['reverse', 'blink'])
            print(ujumbe)
            #print("\033[1;32m There are no items in your cart!  \n")
            #print(" There are no items in your cart!  \n")
        else:
            print("These are the items in your shopping cart:")
            print('-' * 45)
            for bidhaa in kikapu:
                print(f" {bidhaa} - KShs {kikapu [bidhaa]}")
            #for bidhaa in range(len(kikapu)):
                #print('Item' + str(bidhaa) + ' in the cart is: ' + kikapu[bidhaa])
            print('-' * 45)
            pprint.pprint(kikapu)
            
    if chaguo == 3:
        
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
 
    if chaguo == 4:
        
        jumla = 0
        
        for bidhaa in kikapu:
            jumla += kikapu [bidhaa]
            print(f" {bidhaa} - KShs {kikapu [bidhaa]}")
            
        if jumla == 0:
            print("Your cart is empty!")
        else:
            if jumla >= 50000:
                punguzo = jumla * 0.09
                jumla = jumla - punguzo
                print()
                print(f" Discount : {punguzo}")
                print('-' * 30)
                print(f"  Total cost: KShs {jumla} ")
                print('-' * 30)
            elif jumla >= 20000:
                puguzo = jumla * 0.06
                jumla = jumla - punguzo
                print()
                print(f" Discount : {punguzo}")
                print('----------------------------')
                print(f"  Total cost: KShs {jumla} ")
                print('----------------------------')   
            elif jumla >= 10000:
                punguzo = jumla * 0.03
                jumla = jumla - punguzo
                print()
                print(f" Discount : {punguzo}")
                print('----------------------------')
                print(f"  Total cost: KShs {jumla} ")
                print('----------------------------')
            else:
                print('----------------------------')
                print(f"  Total cost: KShs {jumla} ")
                print('----------------------------')
 
    if chaguo == 5:
        
        print ("Thank you for shopping with us.")
        #quit()
        break
    
    #else:
        #print("That is not a valid entry. Try again")
        #break

