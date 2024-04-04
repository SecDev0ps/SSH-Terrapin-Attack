import argparse

def simulate_ssh_handshake(client_version="2.0", server_response_truncated=False):
    """
    Simulates an SSH handshake with potential Terrapin manipulation (educational only).

    Args:
        client_version: String representing the SSH client version.
        server_response_truncated: Boolean indicating whether the server response is truncated.
    """
    # Simulate client hello message
    client_hello = f"SSH-2.0-{client_version}-OpenSSH_8.4p1 Ubuntu-1ubuntu2 LTS\n"

    # Simulate server response with potential truncation (Terrapin attack)
    if server_response_truncated:
        server_response = "SSH-2.0-SERVER\n"  # Truncated version (vulnerable)
    else:
        server_response = "SSH-2.0-SERVER\nkex algos: chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr\n"

    print("Client hello:")
    print(client_hello)
    print("Server response:")
    print(server_response)

    # Analyze the response (educational purposes only)
    if len(server_response.split("\n")) < 2:
        print("WARNING: Server response might be truncated (potential Terrapin attack).")
    else:
        print("Server response seems complete.")

        # Check if vulnerable
        if "chacha20-poly1305@openssh.com" in server_response or any(cipher.endswith("-cbc") for cipher in server_response.split(',')):
            print("VULNERABLE to Terrapin attack.")
        else:
            print("NOT vulnerable to Terrapin attack.")

def main():
    parser = argparse.ArgumentParser(description="Simulate an SSH handshake with potential Terrapin manipulation.")
    parser.add_argument("-url", required=True, help="URL of the SSH server.")
    parser.add_argument("-v", "--version", default="2.0", help="Client version (default: 2.0)")
    parser.add_argument("-t", "--truncated", action="store_true", help="Simulate a truncated server response.")

    args = parser.parse_args()

    simulate_ssh_handshake(client_version=args.version, server_response_truncated=args.truncated)

if __name__ == "__main__":
    main()
