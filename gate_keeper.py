# 1. Set the secret master password
secret_key = "Dragon123"

# 2. Ask the visitor for the password
print("WELCOME TO THE FORTRESS.")
guess = input("Enter the Secret Key: ")

# 3. Check if the guess matches the secret
if guess == secret_key:
    print("ACCESS GRANTED. The gate is opening...")
else:
    print("ACCESS DENIED! Releasing the robot dogs!")
