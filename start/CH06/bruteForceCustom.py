import crypt

def extract_prefix(full_hash):
    parts = full_hash.split('$')
    
    if len(parts) < 4:
        raise ValueError("Invalid crypt hash format.")
    
    return f"${parts[1]}${parts[2]}${parts[3]}$"


def test_password(hashed_password, algorithm_salt, plaintext_password):
    crypted_password = crypt.crypt(plaintext_password, algorithm_salt)
    if hashed_password == crypted_password:
        return True
    return False

#print(extract_prefix("$y$j9T$ryDe07Zxm2YLxpIyWcNb1/$Se.vK0DuyTRjRTtj1ZSyNk2o/rtKmFxYYfeCbejZURC"))

def crack_password():
    target_hash = input("Enter full crypt hash: ").strip()

    try:
        prefix = extract_prefix(target_hash)
        
    except ValueError as e:
        print("Error: ", e)
        return 

    
    for password in range(1000000):
        password_str = str(password).zfill(6)
        result = test_password(target_hash, prefix, str(password))
        print(password)
        
        if result:
            print("Match found: {0}".format(password))
            break
    else:
        print('nope, nothing was found')
       
    
    
if __name__ == "__main__":
    crack_password()