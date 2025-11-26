alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    # Create a condition to check if the direction is 'encode'
    if direction.lower() == "encode":
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
# Create a condition to check if the direction is 'decode'
    elif direction.lower() == "decode":
        # Create a function called 'decrypt' that takes 'encrypted_text' and 'shift_amount' as 2 inputs.
        def decrypt(encrypted_text, shift_amount):
            # Create a variable called 'decrypted_text' to store the decrypted text
            decrypted_text = ""
            # Loop through each letter in the encrypted text
            for letter in encrypted_text:
                # Calculate the shifted position
                shifted_position = alphabet.index(letter) - shift_amount
                # If the shifted position is less than 0, wrap around to the end of the alphabet
                shifted_position %= len(alphabet)
                # Get the new letter
                new_text = alphabet[shifted_position]
                # Add the new letter to the decrypted text
                decrypted_text += new_text
            # Print the decrypted text
            print(f"The decrypted text is {decrypted_text}")

        # Call the decrypt function
        decrypt(encrypted_text=text, shift_amount=shift)

caesar(direction=direction, text=text, shift=shift)