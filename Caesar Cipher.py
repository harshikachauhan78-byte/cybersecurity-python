def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Preserve uppercase and lowercase
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Keep spaces, numbers, and punctuation unchanged
            result += char

    return result


print("=== Caesar Cipher ===")

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        encrypted = caesar_cipher(message, shift, "encrypt")
        print("Encrypted Message:", encrypted)

    elif choice == "2":
        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))
        decrypted = caesar_cipher(message, shift, "decrypt")
        print("Decrypted Message:", decrypted)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")