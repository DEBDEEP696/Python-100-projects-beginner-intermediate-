import re


age = int(input("Enter your age: "))

rem_age = 90 - age
days = rem_age * 365
weeks = rem_age * 52
months = rem_age * 12

print(f"You have {days} days , {weeks} weeks and {months} months left.")