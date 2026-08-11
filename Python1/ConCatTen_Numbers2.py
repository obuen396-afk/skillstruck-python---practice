string = "There are {1} letters in the alphabet in english, although there are {0} letters in spanish."
letters_big = 30
letters_small1 = 26
print(string.format(letters_big, letters_small1))

number = input("Pick a 3-digit number, EXCACTLY! ")
number1 = number[0]
number2 = number[1]
number3 = number[2]
Sum = "The sum of those digits is {}."
Number = str(int(number1) + int(number2) + int(number3))
print(Sum.format(Number))

miles = int(input("How many miles a day? "))
total_miles = int(input("What is the total number of miles to your destination? "))
answer = "The total number of days you will need to drive there is {}."
print(answer.format(total_miles / miles))