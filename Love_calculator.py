his=input("Enter his name: ")
her=input("Enter her name: ")
name = his + her
count1 = 0 
count2 = 0 
for i in name.lower():
    if (i =='t' or i =='r'or i =='u'or i =='e'):
        count1 += 1
    if (i =='l' or i =='o'or i =='v'or i =='e'):
        count2 += 1
score = count1*10 + count2
if score < 10 or score > 90:
    print(f"Your love score is {score}, you go together like coke and mento .")
elif score <= 50 and score >= 40:
    print(f"Your love score is {score}, you are alright together .")
else:
    print(f"Your love score is {score}")