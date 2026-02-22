from cryptography.fernet import Fernet

# Generat a key
key = Fernet.generate_key()
print("Key: ", key)


cipher = Fernet(key)

# Encript
message = input('Add a message: ')

# Convert string -> bytes
message_bytes = message.encode()

encrypted = cipher.encrypt(message_bytes)
print("Encrypted: ", encrypted)


# Decrypt
decrypted = cipher.decrypt(encrypted)
print("Decrypted: ", decrypted)