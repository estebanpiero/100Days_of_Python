# Day 8: Function Parameters & Caesar Cipher

## Project: Caesar Cipher

### Description
A fully functional Caesar Cipher encryption and decryption program that allows users to encode and decode messages using a shift cipher. The program features a continuous loop for multiple encryptions/decryptions and includes ASCII art branding.

### What I Learned
- Function parameters and arguments
- Passing multiple parameters to functions
- String iteration and manipulation
- Index-based list operations
- Modular arithmetic for wrapping
- Error handling for characters not in alphabet
- Creating interactive command-line applications

### How to Run
```bash
cd "day8_project_cesar_cipher"
python3 app.py
```

### Features
- Encode messages with a specified shift value
- Decode encrypted messages
- Handles both uppercase and lowercase letters
- Preserves spaces and special characters
- Continuous operation mode
- ASCII art logo
- Input validation

### How It Works
**Encoding:**
- Each letter is shifted forward in the alphabet by the shift amount
- Example: "hello" with shift 3 becomes "khoor"

**Decoding:**
- Each letter is shifted backward in the alphabet by the shift amount
- Reverses the encoding process

### Key Concepts
- **Function Parameters**: Passing data to functions (`method`, `text`, `shift`)
- **String Iteration**: Looping through each character
- **List Indexing**: Finding and accessing alphabet positions
- **Modular Arithmetic**: Wrapping around the alphabet
- **Control Flow**: Handling different methods (encode/decode)

### Files
- `app.py`: Main application logic
- `cesar_cipher_v2.py`: Enhanced version
- `logo.py`: ASCII art logo

### Example Usage
```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world
Type the shift number:
> 3

Here's the result: khoor zruog
```

### Historical Note
The Caesar Cipher is one of the earliest known encryption techniques, named after Julius Caesar who used it to protect military communications.
