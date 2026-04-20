# Project 5: The Encryption Engine (Caesar Cipher)
# This tool scrambles messages so hackers cannot read them.

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Scramble uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Scramble lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char # Keep spaces and symbols as they are
    return result

print("🔐 --- FORTRESS ENCRYPTION ENGINE --- 🔐")

# 1. Get the message
message = input("Enter the secret message to hide: ")

# 2. Get the Secret Shift Key (a number)
secret_number = int(input("Enter a secret shift number (1-25): "))

# 3. Scramble it!
scrambled = encrypt(message, secret_number)

print(f"\n📡 Original Message: {message}")
print(f"🕵️ Encrypted (Ciphertext): {scrambled}")
print("\nOnly someone with your secret number can decode this!")
