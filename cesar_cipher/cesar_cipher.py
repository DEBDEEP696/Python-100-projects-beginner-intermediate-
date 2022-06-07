from art import logo
print(logo)

def caesar(dir,text,shift_amount):
    result_text = ""
    if dir == "decode":
            shift_amount *= -1
    for char in text:
        if char not in alphabet:
            result_text+=char
        
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            result_text += alphabet[new_position]
            

    print(f"The {dir}d text is {result_text}.")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s = True
while s:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    user_text = input("Type your message:\n").lower()
    shift = (int (input("Type the shift number:\n"))) %26
    
    caesar(dir=direction, text=user_text, shift_amount=shift)
    
    ques = input("Type 'yes' if you want to continue again.Otherwise type 'no'.\n")
    if ques=="no":
        s = False
        print("GOODBYE....")
    
        

       





