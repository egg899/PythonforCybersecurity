# import platform
# import os

# def read():
#     lines = []
#     script_path = os.path.realpath(__file__)
#     script_folder = os.path.split(script_path)
#     f = open(script_folder[0] + "/hackme.txt", "r")
#     for line in f:
#         line = line.strip()
#         lines.append(line)
#     # return lines 
#     print("Here is someone to hack - information ")
#     for i in lines:
#         print(i)   

# read() 

text_file = open("hackme.txt")
file_contents = text_file.read()
text_file.close()
print(file_contents)


