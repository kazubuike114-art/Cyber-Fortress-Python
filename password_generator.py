import random
import string

# The Ingredients
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Mix them all together in one big pot
all_characters = letters + digits + symbols

print("🛡️ MASTER KEY GENERATOR 🛡️")

# Ask the Captain how long the key should be
length = 12 

# The "Dice Roll" - picking random characters
password = "".join(random.sample(all_characters, length))

print(f"Your new Unbreakable Key is: {password}")
print("Store this safely in the fortress vault!")
