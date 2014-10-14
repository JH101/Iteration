# Jamie Hilton
# 10/10/2014
# Title input v1.1

name = input("Please enter your first name: ")

last_name = input("Please enter your last name: ")

gender = input("Please enter your gender m/f: ")

if gender == "m":
    print("Mr {0} {1}".format(name, last_name))

elif gender == "f":
    print("Ms {0} {1}".format(name, last_name))

else:
    print("Please enter an appropriate gender")
