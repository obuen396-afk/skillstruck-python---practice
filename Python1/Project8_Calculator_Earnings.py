earningsgoal = float(input("How much money do you need to save in a year? "))
months = earningsgoal / 12
weeks = months / 4
days = weeks / 7
print("To save up " + str(round(earningsgoal, 2)) + " dollars in one year, you will need to save $" + str(round(months, 2)) + " per month.")
print("To save up " + str(round(months, 2)) + " dollars in one month, you will need to save $" + str(round(weeks, 2)) + " per week.")
print("To save up " + str(round(weeks, 2)) + " dollars in one week, you will need to save $" + str(round(days, 2)) + " per day.")