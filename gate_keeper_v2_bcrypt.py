import bcrypt

# --- SETTING UP THE FORTRESS ---
# In a real app, this hash would come from a database
password = "Dragon123"
# Convert string to bytes and hash it
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

print("🔒 SECURITY UPGRADED: The password is now hashed.")

# --- THE GUARD'S CHECK ---
user_guess = input("Enter the Secret Key to enter the Fortress: ")

# Check if the guess matches the hash
if bcrypt.checkpw(user_guess.encode('utf-8'), hashed_password):
    print("✅ SUCCESS! The gate is opening.")
else:
    print("❌ WRONG! The guard makes a note in the logbook.")
