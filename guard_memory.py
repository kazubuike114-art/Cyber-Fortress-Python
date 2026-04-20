# Project 2: The Guard's Memory (Rate Limiting)
# This script stops hackers from guessing passwords over and over.

secret_key = "Dragon123"
attempts = 0  # This is the guard's clipboard
max_tries = 3 # This is the rule of the fortress

print("🏰 THE GUARD IS NOW WATCHING THE GATE...")

# The guard keeps the gate closed as long as attempts are less than 3
while attempts < max_tries:
    guess = input("\nEnter the Secret Key: ")
    
    if guess == secret_key:
        print("✅ SUCCESS! The gate is opening. Welcome, Captain!")
        break  # The good guy is in! Stop the loop.
    else:
        attempts = attempts + 1  # Guard adds a tally mark to the clipboard
        remaining = max_tries - attempts
        
        print(f"❌ WRONG! The guard makes a note in his book.")
        
        if attempts < max_tries:
            print(f"⚠️ Warning: You have {remaining} tries left before lockdown!")
        else:
            print("🚨 LOCKDOWN! 3 mistakes made. The gate is sealed!")
            print("The Guard is calling the sheriff...")
