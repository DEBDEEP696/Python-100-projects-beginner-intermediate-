print("Welcome to tip-bill calculator....")
bill=float(input("What was the total bill? $"))
per = int(input("What percentage you want to tip? 10 , 12 or 15? "))
split = int(input("How many people to split the bill with? "))
pay = bill * ( 1+ per/100) #pay = bill + ((tip/100)*bill)
pay ="{:.2f}".format(pay/split, 2) #pay is formatted to a string with 2 places after decimal precision
print(f"Each person should pay: ${pay}")

