print("Hello, Goodmorning")
customer = input()

Menu = {"burger": 10, "pizza": 20, "pasta": 15, "fries": 5}
print("What do you like to have,please have a look at our menu")
for item in Menu:
    print(item)

dish = input("I would like to have ")
if dish.strip() in Menu:
    print("Alright, you have selected " + (dish) + " Anything else")
else:
    print("sorry its not available, Anything you would like to have from our menu")
for item in Menu:
    print(item)
while (True):
    dish = input("ok,I want ")
    if dish in Menu:
        print("Sure, I have added")
        break
    else:
        print("sorry ,Again its not available, Anything you would like to have from our menu")
        continue
beverages = {"coke":"Rs 20", "water":50, "coffee":30, "fanta":20}
print ("What do like to have in drinks")
for item in beverages:
    print(item)
while (True):
    drink = input("I would like to have ")
    if drink in beverages:
        print("Great,", "having here or takeaway")
        break
    else:
        print("Sorry,its not available here, Please select the drink from the given list only ")
        continue
place = input()
if place == "having here":
    print("Alright mam, please take your seat, Thankyou")
else:
    print("Thankyou mam, your total bill amount is $30, have a nice day")




