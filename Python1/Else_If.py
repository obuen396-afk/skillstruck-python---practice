#######################Checkpoint########################
coins = 10
if coins > 20:
    print("You have more than enough to buy a puppy")
elif coins == 20:
    print("You have exactly enough to buy a puppy")
else :
    print("You do not have enough to buy a puppy")
######################Greater Than?######################
number = int(input("Enter a number. "))
number1 = int(input("Enter another number. "))
if number > number1:
    print("The first number is larger.")
elif number == number1:
    print("The numbers are the same.")
else :
    print("The second number is larger.")
################Smallest of Three Numbers################
number = input("Enter a number.")
number1 = input("Enter another number.")
number2 = input("Enter a third number.")
if number <= number1 and number < number2 :
    print(number)
elif number < number1 and number <= number2 :
    print(number)
elif number1 < number and number1 <= number2 :
    print(number1)
elif number1 <= number and number1 < number2 :
    print(number1)
elif number2 < number and number2 <= number1 :
    print(number2)
elif number2 <= number and number2 < number1 :
    print(number2)
elif number == number1 and number == number2 :
    print(number2)