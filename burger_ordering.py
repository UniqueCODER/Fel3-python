def computation(menu, a, b, c):
    print(menu)
    choice = input("Choice: ")
    if choice.upper() == "A" or choice == "1":
        return a
    elif choice.upper() == "B" or choice == "2":
        return b
    elif choice.upper() == "C" or choice == "3":
        return c
    else:
        print("Choose Valid option")
    return 0

menu = ['''
    Select Burger\t\t\t Price
    [A] Burger with Cheese \t P25.00 
    [B] Chicken Burger \t\t P35.00 
    [C] Quarter Pounder  \t P70.00 
    ''', '''
    Add-on     \t\t\t   Price
    [1] No add-on           +0.00 
    [2] w/Drink             P15.00 
    [3] w/ Fries and Drink  P30.00 
    ''']

order = computation(menu[0], 25, 35, 70) + computation(menu[1], 0, 15, 30)
print("Total Bill :", order)
