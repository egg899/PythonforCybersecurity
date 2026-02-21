def rot13(text):
    result = ""

    for char in text:
        ascii_code = ord(char)
        
        
        if 65 <= ascii_code <= 90:
            new_code = ascii_code + 13
            if(new_code > 90):
                new_code = new_code - 26
            result += chr(new_code)    


        elif 97 <= ascii_code <= 122:
            new_code = ascii_code + 13
            if new_code > 122:
                new_code = new_code - 26
            result += chr(new_code)    

        else:
            result += char
    print(result)    

           
            
    


rot13('Hello World')
rot13('Uryyb Jbeyq')