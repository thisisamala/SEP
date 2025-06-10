def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_message += shifted_char
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_message += char

    return encrypted_message

# Example usage:
message1 = "hello"
shift1 = 2
print(caesar_cipher_encrypt(message1, shift1))  # Output: jgnnq

message2 = "Secure123"
shift2 = 3
print(caesar_cipher_encrypt(message2, shift2))  # Output: Vhfxuh123
