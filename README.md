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
