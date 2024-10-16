print("Welcome to the Tip Calculator !")
bill = float (input("What was the total bill ? $"))
tip = int (input ("What percentage of tip would you like to give? 10,12,15 ?"))
split = int (input("How many people to split the Bill ?"))
amount = tip /100 * bill + bill
pay = amount / split
finalamount = "{:.2f}".format(pay)
print("Each person should pay:$", finalamount)
