🏰 Cyber Fortress: Python Edition
Welcome to the Fortress. This project demonstrates how to build professional security tools using Python.
🛡️ Project 1: The Front Gate (Authentication)
The Gate Keeper is the first line of defense. It acts as a digital guard that checks every visitor's password before letting them inside.
How it Works:
Identity Check: It asks for a "Secret Key."
Comparison Brain: It matches the input against a master password.
Access Control: It only opens the gate if the password is 100% correct.
​🛡️ Level 2: The Guard's Memory (Rate Limiting)
​The Guard's Memory is an upgrade to our fortress. Instead of just checking passwords, the guard now carries a clipboard to track how many times someone gets the key wrong.
​How it Works:
​The Clipboard (Variable): We created a counter called attempts that starts at zero.
​The Tally: Every time a wrong key is used, the guard adds 1 to the count.
​The Lockdown: If the count reaches 3, the guard stops listening and seals the gate.
​🛡️ Level 3: The Secret Logbook (Security Logging)
​The Secret Logbook is the final layer of our fortress. It creates a permanent record of everything that happens at the Front Gate.
​How it Works:
​Time Stamping: The guard uses the datetime tool to record the exact moment of an event.
​Permanent Storage: It writes the history into a file called fortress_logs.txt.
​Audit Trail: Even if the computer is turned off, the history is saved for the Captain to read later.
​🔑 Level 4: Password Generator (The Key Maker)
​The Password Generator ensures that the "Secret Keys" used for the fortress are impossible to guess.
​How it Works:
​The Ingredient Mix: It combines uppercase letters, lowercase letters, numbers, and special symbols.
​The Digital Dice: It uses the random library to pick characters one by one.
​Custom Length: The Captain can choose exactly how long and strong the key needs to be.
​🔐 Level 5: The Encryption Engine (Cryptography)
​This is my most advanced security project yet. It ensures that the Fortress's internal messages remain secret even if they are intercepted.
​How it Works:
​Plaintext: The original message enter by the Captain.
​The Shift Key: A secret number used to scramble the letters.
​Ciphertext: The scrambled output that looks like random letters to a hacker.
​🔍 Level 6: The Vulnerability Scanner (Security Auditing)
​The Vulnerability Scanner is a tool that searches for weaknesses in our own fortress so we can fix them before a hacker finds them.
​How it Works:
​The Dictionary Check: It compares any password against a "Weak Database" of common keys like 123456 or admin.
​Complexity Rules: It checks if the key is long enough to resist a guessing robot.
​Instant Reporting: It gives the Captain a "Security Report" showing if the fortress is safe or vulnerable.
​📡 Level 7: The Web Health Monitor (System Availability)
​The final piece of the fortress is a monitoring system that ensures our web services are alive and healthy.
​How it Works:
​The Heartbeat: The script sends a request to a URL to check for a "Status 200" (the universal code for "Everything is OK").
​Automated Logic: It uses a loop to check the site every few seconds without human help.
​Incident Alerting: If the site fails to respond, it immediately prints an alert with the specific error.
