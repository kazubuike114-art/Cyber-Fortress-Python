# Cyber-Fortress-Python

`Cyber-Fortress-Python` is a modular, open-source defensive security and tactical incident response toolkit built in Python. Designed for security practitioners, administrators, and developers, it provides lightweight, scriptable defenses for authentication hardening, rate limiting, audit logging, and perimeter monitoring.

## Features & Modules

* **Gate Keeper (`gate_keeper_v2_bcrypt.py`):** Secure user authentication utilizing strong cryptographic hashing (Bcrypt) to protect credentials against plaintext exposure.
* **Guard Memory (`guard_memory.py`):** Intelligent rate-limiting and persistence checks to mitigate brute-force attacks and abnormal connection spikes.
* **Secret Logbook (`secret_logbook.py`):** Immutable audit trailing and timestamped security logging to record critical events for post-incident analysis.
* **Key Maker & Encryption Engine (`password_generator.py`, `encryption_engine.py`):** High-entropy string generation and cryptographic scrambling utilities for secure data transmission.
* **Vulnerability & Health Monitors (`vulnerability_scanner.py`, `web_health_monitor.py`):** Proactive system scanning and heartbeat checks to verify endpoint integrity and service availability.

## Installation & Setup

1. Clone the repository:
   `git clone https://github.com/kazubuike114-art/Cyber-Fortress-Python.git && cd Cyber-Fortress-Python`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run individual modules:
   `python gate_keeper_v2_bcrypt.py`

## Contributing
Contributions, security bug reports, and pull requests are welcome! Please review our [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md) guidelines before submitting code.

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
