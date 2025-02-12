print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

billWithTip = round(tip / 100 * bill + bill, 2)
perPersonPayment = "{:.2f}".format(billWithTip / people)
print(f"Each person should pay ${perPersonPayment}")
