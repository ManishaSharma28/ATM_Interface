# menu of cafe
menu = {
    'Pizza' : 400,
    'Burger' : 60,
    'Red Bull' :150,
    'Coca' : 50,
    'Sprite' :30,
    'Ice Cream' : 50,
    'Cold Coffee' : 100,
    'Hot Coffee' :100,
    'Tea' : 20,
}

# welcoming
print("Welcome to Cafe")
print("Pizza : 400\nBurger : 60\nRed Bull :150\nCoca : 50\nSprite :30\nIce Cream : 50\nCold Coffee : 100\nHot Coffee :100\nTea : 20")
order_total = 0

first_order= input("Enter the name of item you want to order : ")
if first_order in menu:
    order_total += menu[first_order]
    print(f"Your order {first_order} is added.")
else:
    print(f"{first_order} is not avaialable.")
    
next_order = input("Do you want to add another order? (Yes/No)")
if next_order == "Yes":
    second_order = input("Enter the name to second order")
    if second_order in menu:
        order_total += menu[second_order]
        print(f"order {second_order} has been added.")
    else:
        print(f"oreder {second_order} is not available.")
        
    print(f"The total amount is{order_total}")
    