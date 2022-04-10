hackme = open("hackme.txt", "w")

name = input("What is your name?\n")
color = input("What is your favourite color?\n")
pet = input("What was your first pet's name?\n")
mother = input("What is your mother's maiden name?\n")
school = input("What elementary school did you attend?\n")

hackme.write(name + "\n")
hackme.write(color + "\n")
hackme.write(pet + "\n")
hackme.write(mother + "\n")
hackme.write(school + "\n")

hackme.close()