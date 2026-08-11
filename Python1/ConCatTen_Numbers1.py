string = "There are {} letters in the alphabet."
letters = 26
print(string.format(letters))

age = 16
birthday = "My birthday is 7/29. (Hint, I'm {} years old.)"
print(birthday.format(age))

apples_per_tree = int(input("How many apples does Bob harvest a tree? "))
solution = "If Bob harvested one tree, he would have {} apples per wheelbarrow. If he harvested the whole orchard, he would have {} apples per wheelbarrow."
apples_per_8_trees = apples_per_tree * 8
apples_per_wheelbarrow = apples_per_tree / 3
apples8_per_wheelbarrow = apples_per_8_trees / 3
print(solution.format(apples_per_wheelbarrow, apples8_per_wheelbarrow))