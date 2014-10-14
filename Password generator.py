# Jamie Hilton
# 10/10/14
# Password generator

import random

length = int(input("How many characters do you want in your password?: "))

for counter in range(length):

    character = random.randint(65, 122)

    converted_character = chr(character)

    print(converted_character)



