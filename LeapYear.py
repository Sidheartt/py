# Check whether a year is leap year or not
year = int(input("Which year do you want to check? "))

if year%4==0 and year%100 !=0:
  print("Its a leap year")
elif year%100 ==0 and year%400 ==0 :
  print("It's a leap year")
else:
  print("Its not a leap year")



