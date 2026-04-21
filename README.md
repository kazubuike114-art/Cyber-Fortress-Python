🏰 Cyber Fortress: Python Edition
Welcome to the Fortress. This project demonstrates how to build professional security tools using Python.

​ ​🛡️ Layer 1: The Front Gate (Authentication)
​Filename: gate_keeper.py
​The Problem: Standard systems need a way to verify identity securely. I built a logic-gate that requires a 100% match.
​Update (v2): gate_keeper_v2_bcrypt.py
​Why I upgraded: I realized storing passwords as plain text is a major vulnerability. If a database is leaked, every user is exposed. By switching to Bcrypt, I ensured only a non-reversible hash is stored.
🧠 Layer 2: The Guard’s Memory (Rate Limiting)
​Filename: guard_memory.py
​The Problem: Brute-force attacks. Without a "memory," a hacker can guess a password a million times a second.
​The Solution: I implemented a counter mechanism using a while loop.
​Why a while loop? It allows the program to persist in a state of "waiting" until a condition is met (either the correct key is found or the maximum attempts are exhausted).
​Technical Hurdle: Managing the state of the "remaining tries" so that the user receives accurate feedback after every failure.
​Scalability: For 1,000 users, I would move this logic to a database like Redis to track attempts by IP address or username.
​📜 Layer 3: The Secret Logbook (Security Logging)
​Filename: secret_logbook.py
​The Problem: If a breach occurs, we need to know when and how.
​The Solution: I integrated the Python datetime module to create persistent records.
​Key Feature: The script creates an "Audit Trail" in fortress_logs.txt. This ensures that even if the session ends, the history is saved for the "Captain" to read.
​🔑 Layer 4 & 5: The Key Maker & Encryption Engine
​Filenames: password_generator.py & encryption_engine.py
​The Goal: Moving from static keys to dynamic, scrambled data.
​The Logic: * The Key Maker: Uses the random library to generate high-entropy strings.
​The Encryption Engine: Implements a Shift Cipher (Caesar Cipher) logic to scramble messages into ciphertext.
​🔍 Layer 6 & 7: Vulnerability Scanner & Web Health Monitor
​Concept: Proactive defense.
​Vulnerability Scanner: Compares user inputs against a "Weak Database" of common passwords (like 123456).
​Health Monitor: Uses a loop to send "Heartbeat" requests to a URL, checking for a Status 200 to ensure the fortress is still online.
