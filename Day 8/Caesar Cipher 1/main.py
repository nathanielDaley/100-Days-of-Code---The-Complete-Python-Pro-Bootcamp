alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
length_of_alphabet = 26

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
#  by the shift amount and print the encrypted text.
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for index in range(len(original_text)):
        shifted_position = alphabet.index(original_text[index]) + shift_amount
        shifted_position = shifted_position % length_of_alphabet

        cipher_text += alphabet[shifted_position]

    return cipher_text


print(f"Here is the encoded amount: {encrypt(text, shift)}")
