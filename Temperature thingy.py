# Jamie Hilton
# 14/10/2014
# temperature thing v1.1

temperature = int(input("Please enter the temperature in (c): "))

if temperature > 99:
    print("The water is at boiling temperature")

elif temperature < 0:
    print("The water is at freezing temperature")

else:
    print("The water is not freezing or boiling")
