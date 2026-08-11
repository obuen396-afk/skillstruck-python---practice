String1 = " My superstring\'s so spectacular, it can be striped, indexed, sliceed, reverseed, splited, lengthed, and finded! "
print(String1.strip())
print(String1[5])
print(String1[2:10:3])
print(String1[len(String1)::-1])
print(String1.split())
print(len(String1))
print(String1.find("d"))
print(String1.rfind("d"))

String = input("Enter a sentence.")
String1 = String.split()
print(len(String1))

String = input("Enter a sentence with many Es.")
print(str(String.find("e")) + "-" + str(String.rfind("e")))