from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a function to encrypt or decrypt the text
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        # If the letter is not in the alphabet, add it to the output text
        if letter not in alphabet:
            output_text += letter
            
        # If the encode_or_decode is "decode", subtract the shift amount from the letter's position
        else:
            if encode_or_decode == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            # If the encode_or_decode is "encode", add the shift amount to the letter's position
            elif encode_or_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
    # Print the result
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Get the direction, text and shift amount from the user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Initialize the while loop to keep the program running until the user wants to stop
go_again = True
# While the user wants to go again, continue the loop
while go_again:
    # Call the caesar function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    # Ask the user if they want to go again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    # If the user doesn't want to go again, set go_again to False
    if restart == "no":
        go_again = False
        print("Goodbye!")
    # If the user wants to go again, print the logo and ask for the direction, text and shift amount again
    else:
        print(logo)
        # Ask the user for the direction, text and shift amount again
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        # Ask the user for the shift amount again
        shift = int(input("Type the shift number:\n"))