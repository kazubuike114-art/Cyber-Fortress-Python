import datetime # This is a tool to tell the time

secret_key = "Dragon123"
attempts = 0

print("🏰 THE GUARD IS WRITING IN THE LOGBOOK...")

while attempts < 3:
    guess = input("\nEnter Secret Key: ")
    
    # Get the current time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if guess == secret_key:
        log_entry = f"[{now}] SUCCESS: Captain entered the fortress.\n"
        print("✅ Access Granted!")
        # Open the logbook and write the success
        with open("fortress_logs.txt", "a") as log_file:
            log_file.write(log_entry)
        break
    else:
        attempts += 1
        log_entry = f"[{now}] WARNING: Wrong password used! (Attempt {attempts})\n"
        print(f"❌ Wrong! Attempt {attempts}/3")
        # Open the logbook and write the warning
        with open("fortress_logs.txt", "a") as log_file:
            log_file.write(log_entry)
            
        if attempts == 3:
            print("🚨 LOCKDOWN! Incident recorded in logs.")
