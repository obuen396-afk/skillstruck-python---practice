N = 1
while N == 1 :
    number = int(input("Which number?"))
    by = (input("Add/Subtract/Multiply/Divide?"))
    number2 = int(input("Select another number."))
    if by == "Add" :
        print(number + number2)
    if by == "Subtract" :
        print(number - number2)
    if by == "Multiply" :
        print(number * number2)
    if by == "Divide" :
        print(number / number2)
    if by == "Divide + Modulus" :
        print(int(number / number2), "Remainder: " + str(number % number2))
    else :
        print("\033[1;31mError: you put in the wrong sign! \n\033[0mgood thing this isn't a \033[5mreal \033[0merror, this program would stop then!")

int1 = 5
int2 = 5
print(int1 + int2)
print(int1 - int2)
print(int1 * int2)
print(int1 / int2)