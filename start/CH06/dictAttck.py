#!/usr/bin/env python3
import crypt
import os

def extract_prefix(full_hash):
    """
    Extractind $id$salt from Linux crypt hash
    """

    parts = full_hash.split('$')
    
    if len(parts) < 4:
        raise ValueError("Invalid crypt hash format.")
    
    return f"${parts[1]}${parts[2]}${parts[3]}$"




def read_dictionary(dictionary_file):
    #Open provided dictinary file
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    return script_folder[0]+'/'+f'{dictionary_file}'


wordlist_file = read_dictionary("top10.txt")





def crack_password():
    # Ask user for full hash
    target_hash = input("Enter full crypt hash: ").strip()

    try:
        prefix = extract_prefix(target_hash)
    except ValueError as e:
        print("Error:", e)
        return
    
    try:
        with open(wordlist_file, "r", encoding="utf", errors="ignore") as file:
        
            for line in file:
                candidate = line.strip()

                # Hash candidate using same ID + salt
                hashed_candidate = crypt.crypt(candidate, prefix)

                if hashed_candidate == target_hash:
                    print("Password FOUND: ", candidate)
                    return
                
        print("Password not found in file.")

    except FileNotFoundError:
        print("Wordlist file not found.")
        
    
if __name__ == "__main__":
    crack_password()

    



#print(extract_prefix('$y$j9T$SXnM0JK7GEPeCAjt6pXGw.$vZnmQmn4ICZ97pJdcWgN5UKHcvT9pnrpz7j/8M2.NmD'))