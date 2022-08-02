from day8_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

print(f"{logo}")

def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1  
    for letter in start_text:
        if letter in alphabet:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d result: {end_text}")
    


should_continue = True
while should_continue:            
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25; 
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()           
    if user_input == "no":
        print(f"Good Bye")
        should_continue = False


#     if direction == "encode":
#         encrypt(text,shift)
#     elif direction == "decode":
#         decrypt(text,shift)
#     else:
#         print(f"Wrong input")

# def encrypt(text,shift):
#     encode_string = "" # To store the encoded string
#     for char in text: # Looping through the charecters in the given text
#         if char in alphabet: # check the charecter exists in alphabet list. If it is, then move 'shift' number of charecters
#             position = alphabet.index(char) # Get the index position of character
#             position += shift

#             if position >= 26:
#                 position = position - 26 
                
#             encode_string += alphabet[position]
#         else:
#             encode_string += char
#     print(encode_string)



# def decrypt(text,shift):
#     decode_string = ""
#     for letter in text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             position -= shift
            
#             if position < 0:
#                 position = position + 26
#             decode_string += alphabet[position]
#         else:
#             decode_string += letter
#     print(decode_string)         
            

