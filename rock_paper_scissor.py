import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list=[]
list.append(rock)
list.append(paper)
list.append(scissors)


choice = int(input("What do you chose ? Type 0 for Rock , 1 for Paper and 3 for Scissors.\n"))
if choice >2 or choice<0:
    print("Invalid choice")
    quit()
print(f"You chose : \n {list[choice]} ")
comp_choice = random.randint(0,2)
print(f"Computer chose {comp_choice} :\n {list[comp_choice]}")

if (choice==0 and comp_choice==2):
    print ("You Win") 
elif (choice==2 and comp_choice==0):
    print ("You Loose")   
elif choice < comp_choice:
    print("You Loose")
elif choice > comp_choice:
    print("You Win")
elif choice==comp_choice:
    print("Draw")



