# question = input("Is today a good day? (n/y)") 


# def send_message(message):
    
#         if message == "y":
#          print("Yes, it is")



# for i in range(10):
#     send_message(question)








def send_message():
    question = input("Is today a good day? (n/y)") 
    
    if question == "y":
        for i in range(10):
            print("Yes, it is") 
    else:
        send_message()    

send_message()