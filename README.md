# 🏦 Goldman Sachs Software Engineering Virtual Experience Program

This program, offered by Forage, focuses on the analysis and enhancement of password security policies in an organization. The project involves cracking a simulated leaked password database, assessing the organization's existing security measures, and proposing strategies to improve password protection. By understanding the techniques used by hackers to bypass security controls, we can recommend effective solutions to strengthen the organization's password policies.

## 📋 Table of Contents

- [🌐 Overview](#overview)
- [⚙️ Features](#features) 
- [👥 Authors](#authors) 
- [📦 Requirements](#requirements)
- [🌲 Project Structure](#project-structure) 
- [🚀 Launching the Application](#running-the-program)
- [🚶🏽 Walkthrough](#Walkthrough)
- [📋 Memo](#Memo)
- [📚 Additional Resources](#additional-resources)
- [📝 License](#license) 

## 🌐 Overview

In a typical organisational scenario, user information is stored in a database, where usernames are stored in plaintext, while passwords are encrypted. This project simulates a 'compromised database' in which leaked information is stored in a .txt file, with each line containing a username and its corresponding password hash.

Password hashes are generated using cryptographic hash functions, which convert plaintext passwords into unique combinations of letters and numbers. For instance, the MD5 hash of "password" would be: 5f4dcc3b5aa765d61d8327deb882cf99. Since hashes for a specific plaintext password will always be the same, attackers can use precomputed tables of hashes (also known as rainbow tables) to match hashes with their plaintext counterparts.

In this project, I use a password cracking tool called Hashcat, which leverages the power of GPUs to efficiently crack various types of hashes. By comparing the hashes in the leaked database with those in a precompiled list of plaintext passwords (such as the cracked.txt file), I can reveal the original passwords and assess the organization's password security.

The goal is to identify weak passwords, analyze existing security measures, and propose enhancements to strengthen the organization's password policies. I will also provide a memo that outlines the findings and recommendations for improving password security.

## ⚙️ Features

- Utilizes Hashcat for efficient password recovery
- Interactive command-line interface for user-friendly operation
- Parses leaked password databases and extracts required information
- Displays cracked passwords in a well-formatted and aesthetic table
- Logs important events and debug information for better analysis

## 👥 Authors

- [@joshfinney](https://github.com/joshfinney)
- Version: 1.1

## 📦 Requirements

The following libraries and packages are required to run the password cracking script. Ensure that you have the correct versions installed in your development environment.

- [Python](https://www.python.org/) 3.7+: A high-level, interpreted, and dynamically-typed programming language, used as the primary language for the password cracking script.
- [hashcat](https://hashcat.net/hashcat/) 6.2.6+: A fast password recovery tool that utilizes GPU acceleration to crack various hash types.
- [Homebrew](https://brew.sh/) 3.3.9+: A package manager for macOS and Linux systems, used for installing hashcat and other software.
- [Rich](https://rich.readthedocs.io/en/stable/) 10.12.0+: A Python library that provides a simple and powerful way to style and format terminal output, improving the aesthetics and readability of the password cracking script's output.
- [cracked.txt](https://drive.google.com/drive/folders/1jCz7_qvdVJkXJ6O0eqzscLsVbWv1NaBf?usp=share_link) : This is the precompiled list of plaintext passwords that I have used in the walkthrough, feel free to use your own.

## 🌲 Project Structure

```plaintext
Goldman-Sachs-SWE-Program/
├── cracked.txt
├── dump.txt
├── outfile.txt
├── parsed_hashes.txt
├── main.py
├── walkthrough.gif
├── README.md
└── LICENSE
```

## 🚀 Launching the Application

To run the password cracking script, follow the steps below:
1. Ensure that all required dependencies are installed.
2. Navigate to the project directory.
3. Execute the following command:

```bash
python3 main.py
```

This command runs the password cracking script, which processes the input files and displays the cracked passwords in a well-formatted table.

## 🚶🏽 Walkthrough
![](https://github.com/joshfinney/Goldman-Sachs-SWE-Program/blob/main/walkthrough.gif)

## 📋 Memo

**Executive Summary**: This memo presents an analysis of the password protection controls currently used by the organisation and proposes potential uplifts to enhance the security of passwords. The analysis indicates that the organisation is using the MD5 hashing algorithm to protect passwords, which is considered weak and vulnerable to attacks. 

Furthermore, based on the provided wordlist, the organisation's password policy appears to be inadequate. The memo outlines a set of recommendations to improve the current password protection mechanisms and policies.

**Current Controls and Limitations**: Our analysis shows that the organisation is using the MD5 hashing algorithm to protect passwords. This algorithm produces a 32-character hash for each password, which is relatively fast to compute. However, MD5 is no longer considered a secure hashing algorithm due to its vulnerability to attacks, such as collision and preimage attacks. As a result, an attacker can easily crack passwords protected using MD5, especially if the passwords are weak or part of a known wordlist.

Furthermore, based on the provided wordlist, it is not possible to determine the organisation's specific password policy, such as minimum length or character complexity requirements. However, some of the cracked passwords indicate that the policy may not be sufficiently robust to protect against password-guessing or brute-force attacks.

**Proposed Uplifts and Justifications**: To enhance the organisation's password security, we recommend implementing the following measures:
Stronger Hashing Algorithm: Replace MD5 with a more secure hashing algorithm, such as bcrypt, scrypt, or Argon2. These algorithms are slower to compute and specifically designed to protect passwords against brute-force attacks.

**Salting**: Implement salting to ensure that hashes for identical plaintext passwords are unique, even if two users have the same password. Salting will help prevent attackers from using precomputed tables (e.g., rainbow tables) to crack passwords.

**Key Stretching**: Use key stretching techniques to increase the time and computational effort required to compute hashes, making brute-force attacks more difficult and time-consuming for attackers.

**Multi-Factor Authentication (MFA)**: Introduce MFA as an additional layer of security, requiring users to provide more than one form of identity verification (e.g., a password and a one-time code sent to a registered device) to access their accounts.

**Enhanced Password Policy**: Improve the organisation's password policy by enforcing a minimum password length of at least 12 characters and requiring a mix of uppercase and lowercase letters, numbers, and special characters. Additionally, implement checks for common passwords, set a password expiration period, and require users to change their passwords regularly. Finally, establish a password history policy to prevent users from reusing recent passwords.

**Conclusion**: By implementing these proposed uplifts, the organisation can significantly enhance its password security and mitigate the risks associated with password cracking. These measures will help protect the organisation's assets and user accounts from unauthorised access, ensuring the confidentiality and integrity of sensitive data.

## 📚 Additional Resources

- [Hashcat Wiki](https://hashcat.net/wiki/): A comprehensive resource on Hashcat, including usage instructions, examples, and optimization tips.
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/): The official Python style guide, which provides coding conventions and best practices for writing clean and maintainable Python code.
- [Python Logging Module](https://docs.python.org/3/library/logging.html): The official documentation for Python's built-in logging module, which facilitates logging important events and debugging information.
- [Cryptography.io](https://cryptography.io/en/latest/): A popular Python library that provides cryptographic recipes, including symmetric and asymmetric encryption, message digests, and key derivation.
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html): A comprehensive guide on best practices for securely storing passwords, provided by the Open Web Application Security Project (OWASP).
- [Khan Academy Cryptography Course](https://www.khanacademy.org/computing/computer-science/cryptography): A free online course on cryptography, covering topics such as encryption, decryption, and secure communication protocols.
- [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/): A comprehensive textbook covering various aspects of modern cryptography, including secure hashing, public-key encryption, and digital signatures.


## 📝 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

Copyright (c) 2023 Joshua Finney

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
