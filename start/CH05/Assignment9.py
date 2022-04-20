from cryptography.fernet import Fernet

def create_key():
    "Generate a key and save it into a file"
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# create_key() 

def load_key():
    "Load the key from the current direnctory " 
    # return open("key.key", "rb").read()   
    with open("key.key", "rb") as file:
        file_data = file.read()
        return file_data   

   

def encrypt(plain_text, key):
    plain_text = plain_text.encode()
    #key = key.encode()
    cipher_text = Fernet(key).encrypt(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text

def decrypt(cipher_text, key):
    cipher_text = cipher_text.encode()
    plain_text = Fernet(key).decrypt(cipher_text)
    plain_text = plain_text.decode()
    return plain_text



encKey=""

method = input("Which would you like to do: Create key, Encrypt, Decrypt (c/e/d)? ")
method = method[0].lower()

if method == "c":
    create_key()
elif method == 'e':
    plain_text = input("Message to encrypt: ")
    encKey = load_key()
    # print(encKey)
    cipher_text = encrypt(plain_text, encKey)
    print(cipher_text)
elif method == 'd':
    cipher_text = input("Message to decrypt: ")
    encKey = load_key()
    plain_text = decrypt(cipher_text, encKey)
    print(plain_text)
else:
    # Invalid choice was selected, print error and quit
    print("Wrong selectioon, choose C, E, or D")
