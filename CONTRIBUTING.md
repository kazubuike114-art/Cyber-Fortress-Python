# Contributing Guidelines

Thank you for your interest in contributing to this project! Clear, secure, and well-tested contributions help keep this tool reliable for everyone.

## How to Contribute
1. **Fork the Repository:** Create your own fork of the project and clone it locally.
2. **Create a Feature Branch:** Branch off `main` using a descriptive name (e.g., `fix/auth-validation` or `feat/log-parser`).
3. **Follow Secure Coding Practices:**
   * Never hardcode API keys, credentials, or sensitive tokens in source files.
   * Validate and sanitize all external inputs and network payloads.
   * Keep dependencies minimal and up to date.
4. **Test Your Changes:** Run existing checks and verify that your changes do not break core functionality.
5. **Submit a Pull Request:** Open a PR against `main` with a clear summary of the problem solved and testing steps performed.

## Code Review & Governance
* All pull requests require maintainer review before merging into `main`.
* Security-sensitive changes (authentication, network listeners, file I/O, or dependency updates) undergo additional static analysis and manual audit.
* By submitting a contribution, you agree that your work will be licensed under the repository's open-source license.
