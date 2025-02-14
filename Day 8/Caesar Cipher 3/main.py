# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
length_of_alphabet = 26

# TODO-3: Can you figure out a way to restart the cipher program?


# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, direction_type):
    if direction_type == "decode":
        shift_amount *= -1

    output_text = ""
    for index in range(len(original_text)):
        if original_text[index] in alphabet:
            shifted_position = alphabet.index(original_text[index]) + shift_amount
            shifted_position %= length_of_alphabet

            output_text += alphabet[shifted_position]
        else:
            output_text += original_text[index]

    return output_text

running = True
while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    if not (direction == "encode" or direction == "decode"):
        print("Invalid encoding selection. Exiting.")
    else:
        print(f"Here is the {direction}d result: {caesar(text, shift, direction)}\n")

    keep_running = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if not keep_running == "yes":
        running = False
