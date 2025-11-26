# Caesar Cipher

A Python implementation of the classic Caesar Cipher encryption and decryption algorithm. This interactive command-line tool allows you to encode and decode messages using a shift-based substitution cipher.

## Features

- 🔐 **Encode messages**: Encrypt text using a customizable shift amount
- 🔓 **Decode messages**: Decrypt previously encoded text
- 🔄 **Interactive loop**: Continue encoding/decoding multiple messages without restarting
- 🎨 **ASCII art logo**: Beautiful visual display when the program starts
- 📝 **Preserves non-alphabetic characters**: Spaces, numbers, and special characters remain unchanged

## How It Works

The Caesar Cipher is one of the oldest encryption techniques. It works by shifting each letter in the alphabet by a fixed number of positions. For example, with a shift of 3:
- 'a' becomes 'd'
- 'b' becomes 'e'
- 'z' wraps around to 'c'

The program handles both encoding (shifting forward) and decoding (shifting backward) operations.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Caesar-Cipher
```

2. No additional dependencies required - uses only Python standard library!

## Usage

Run the program:
```bash
python main.py
```

The program will prompt you for:
1. **Direction**: Type `encode` to encrypt or `decode` to decrypt
2. **Message**: Enter the text you want to encode/decode
3. **Shift number**: Enter the number of positions to shift (must be the same shift used for encoding when decoding)

After processing, you can choose to continue with another message or exit.

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
Here is the encoded result: khoor zruog

Type 'yes' if you want to go again. Otherwise type 'no'.
yes

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog
Type the shift number:
3
Here is the decoded result: hello world
```

## Project Structure

```
Caesar-Cipher/
├── main.py      # Main program logic
├── art.py       # ASCII art logo
└── README.md    # This file
```

## Notes

- The program converts all input to lowercase for processing
- Non-alphabetic characters (spaces, numbers, punctuation) are preserved as-is
- The shift amount wraps around the alphabet (e.g., shift of 26 is equivalent to shift of 0)

## License

This project is open source and available for educational purposes.
