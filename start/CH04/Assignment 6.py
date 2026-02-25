hackme = open("hackme.txt", "w")

name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
mother = input("What is your mother's maiden name? ")
school =input("What elementary school did you attend? ")


hackme.write(name + "\n")
hackme.write(color + "\n")
hackme.write(pet + "\n")
hackme.write(mother + "\n")
hackme.write(school + "\n")


hackme.close()