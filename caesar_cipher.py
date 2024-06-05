def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            if char.islower():
                new_code = char_code + shift_amount
                if new_code > ord('z'):
                    new_code -= 26
            elif char.isupper():
                new_code = char_code + shift_amount
                if new_code > ord('Z'):
                    new_code -= 26
            encrypted_text += chr(new_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                result = encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

        again = input("Do you want to run the program again? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
