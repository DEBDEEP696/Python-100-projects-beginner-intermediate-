from art import logo
print (logo)

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul (n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {  "+":add,  #function name are stored in dictionary
                "-":sub,
                "*":mul, 
                "/":div
            }
def calculator():
    num1 = float(input("Enter the 1st number: "))
    flag = True

    while flag:
        for symbol in operations:
            print(symbol)
        operation_symbol= input("Enter the operation you want to execute: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1,num2)    #function name is kept as dictionary values, and while calling with keys, brackets ‘(parameters)’ are added.
        print (f"{num1} {operation_symbol} {num2} = {result}")

        q = input( f"Type 'y' to conitune calculating with {result}, or type 'q' to quit ,or type 'n' for new claculation: ")
        if q == "y":
            flag = True
            num1 = result
        elif q == "n":
            calculator()    # Recursive call
        else:
            print(f"Good Bye...The final answer is {result} .")
            flag = False
            break
    return
        
calculator()