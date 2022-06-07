print("Welcome To The Rollercoaster: ")
height = int(input("Enter yout height in cm: "))
price = 0
if height >= 120 :
    age = int(input("Enter yout age: "))
    print ("You can ride.")
    if age < 12:
        price = 5
    elif age<=18:
        price = 7
    else:
        if age >= 45 and age <=55:
            price=0
            print("Have a free ride on us....")
        else:
            price = 12


    photo = input("Do you want photos? Yes/No:  ")
    if photo == "Yes":
        price += 3
    print (f"Ticket price is ${price}.")
else:
    print("You can't ride.")