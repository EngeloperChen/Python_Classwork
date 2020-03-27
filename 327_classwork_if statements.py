number = input("Enter a number: ")

if int(number) > 5:
    print(str(number) + " is greater than " + str(5) + ".")
elif int(number) == 5:
    print(str(number) + " equals " + str(5) + ".")
else:
    print(str(number) + " is lower than " + str(5) + ".")
