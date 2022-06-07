print ("Welcome to Pizza Deliveries..........")
size = input("What size pizza you want ? S , M or L : ")
peperoni = input("Do you want pepperoni? Y/N : ")
cheese = input("Do you want extra cheese? Y/N : ")
bill=0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
        
else:
    print("!!Enter a valid size!!")
if peperoni == 'Y' :
    if size =='S':
        bill += 2
    else:
        bill += 3
if cheese =='Y':
    bill+=1
print(f"Your final bill is {bill}.")