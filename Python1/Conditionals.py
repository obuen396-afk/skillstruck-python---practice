#########################################################
## Checkpoint ##
age = int(input("How old are you? "))
license = input("Do you have a driver's license? Y or N: ") == "Y"
print(license)
if not license :
    license = False
else :
    license = True

if age >= 16 and license == True :
    print("You are old enough to drive.")
else:
    print("You are not able to drive.")
#########################################################
## Can I Ride? ##
height_in_Inches = int(input("How tall are you (in inches)?"))
if height_in_Inches >= 48 :
    print("You can ride the roller coaster.")
else :
    print("You can't ride the roller coaster.")
#########################################################
## More than Average? ##
number = int(input("Pick a number from 0 to 100. "))
if number > 50 :
    print("More than average")
else :
    print("Fewer than average")