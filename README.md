# SSH Terrapin Vulnerability Checker

## Overview
This script is designed to simulate an SSH handshake with potential Terrapin manipulation, a vulnerability known as CVE-2023-48795. The Terrapin vulnerability is a man-in-the-middle prefix truncation weakness in SSH servers, allowing remote attackers to bypass integrity checks and downgrade the connection's security. The vulnerability affects SSH servers that support either ChaCha20-Poly1305 or CBC ciphers with Encrypt-then-MAC (EtM) without strict key exchange countermeasures.

## CVE-2023-48795
CVE-2023-48795 is a vulnerability that affects the SSH protocol, particularly OpenSSH configurations vulnerable to the Terrapin attack. The vulnerability allows attackers to manipulate SSH handshakes, leading to potential security downgrades and integrity compromise.

## Usage
To use this script, follow these steps:

1. Install Python if you haven't already (Python 3.x is recommended).
2. Clone the repository `git clone https://github.com/Dev5ec0ps/SSH-Terrapin-Attack` or `wget https://github.com/Dev5ec0ps/SSH-Terrapin-Attack/blob/main/terrapin.py`
3. Go there `cd SSH-Terrapin-Attack`
4. Run the script with the desired options:

`python terrapin.py -url <SSH_server_URL> [-v <client_version>] [-t]`

Options:
- `-url`: URL of the SSH server (required).
- `-v`, `--version`: Client version (default: 2.0).
- `-t`, `--truncated`: Simulate a truncated server response (optional).

Example:

`python terrapin.py -url 127.0.0.0 -v 1.9.9p1 -t`

## Importance of Fixing the Issues
It's crucial to fix vulnerabilities like Terrapin (CVE-2023-48795) because they pose significant security risks to SSH communication. By exploiting these weaknesses, attackers can compromise the integrity and confidentiality of SSH connections, potentially leading to unauthorized access, data breaches, and other security incidents. Patching vulnerable SSH servers and ensuring secure configurations help protect against such attacks and maintain the security of network communication.

**More info: https://terrapin-attack.com/**
