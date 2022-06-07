import random

name_str = input("Enter the name of participants separated by ' , ' :  ")
names = name_str.split(" , ")
last = len(names) - 1

ch = random.randint(0,last)
person = random.choice(names)
print (f"{person} is going to pay the bill")
print(f"{names[ch]} is going to pay the next bill .")
