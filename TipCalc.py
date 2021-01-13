#Tip calculator

print("Welcome to the Tip Calculator !!!")
bill = input("Amount of the bill: ")
people = input("number of peps: ")
tip = input("What tip would you like to give ? 10%,12% or 15%")
cash = (int(bill)*float(tip)/10)/int(people)
print(f"Each one should pay: {cash}")