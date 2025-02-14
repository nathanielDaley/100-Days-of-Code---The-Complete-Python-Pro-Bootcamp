alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
length_of_alphabet = 26

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for index in range(len(original_text)):
        shifted_position = alphabet.index(original_text[index]) + shift_amount
        shifted_position %= length_of_alphabet

        cipher_text += alphabet[shifted_position]

    return cipher_text

def decrypt(original_text, shift_amount):
    output_text = ""
    for index in range(len(original_text)):
        shifted_position = alphabet.index(original_text[index]) - shift_amount
        shifted_position %= length_of_alphabet

        output_text += alphabet[shifted_position]

    return output_text

def caesar(original_text, shift_amount, direction_type):
    if direction_type == "decode":
        shift_amount *= -1

    output_text = ""
    for index in range(len(original_text)):
        shifted_position = alphabet.index(original_text[index]) + shift_amount
        shifted_position %= length_of_alphabet

        output_text += alphabet[shifted_position]

    return output_text


if not (direction == "encode" or direction == "decode"):
    print("Invalid encoding selection. Exiting.")
else:
    print(f"Here is the {direction}d result: {caesar(text, shift, direction)}")


