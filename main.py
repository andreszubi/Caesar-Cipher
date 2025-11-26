alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
#  Create a variable called 'encrypted_text' to store the encrypted text.
    encrypted_text = ""
    # Loop through each letter in the original text
    for letter in original_text:
        # Calculate the shifted position
        shifted_position = alphabet.index(letter) + shift_amount
        # If the shifted position is greater than the length of the alphabet, wrap around to the beginning of the alphabet
        shifted_position %= len(alphabet)
        # Get the new letter
        new_text = alphabet[shifted_position]
        # Add the new letter to the encrypted text
        encrypted_text += new_text
    # Print the encrypted text
    print(f"The encrypted text is {encrypted_text}")

# Call the encrypt function
encrypt(original_text=text, shift_amount=shift)