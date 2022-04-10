#!/usr/bin/env python3
# Sample script that writes to a file
# By Alberto German Verissimo on April 8, 2022

# Open file for writing
test_file = open("testfile.txt", "w")

#write lines to the file
test_file.write("Hello World\n")
test_file.write("My name is Alberto\n")
test_file.write("I like rubber ducks\n")

#Close the file
test_file.close()
