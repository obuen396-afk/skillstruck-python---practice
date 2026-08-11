##checkpoint##
animals = ["Hedgehog", "Shark", "Narwhal", "Anglerfish"]
for x in animals :
    print(x + " is the spikiest animal ever!")
##Automatic Numbers##
var1 = int(input("Enter a number."))
var2 = int(input("Enter another number."))
for x in range(var1, var2 + 1) :
    print(x)
## Add the Numbers##
num1 = int(input("Enter a number."))
num2 = int(input("Enter another number."))
big_num = 0
for x in range(num1, num2 + 1) :
    big_num = big_num + x
print(big_num)