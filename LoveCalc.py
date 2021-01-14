# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

string = name1 + name2
guy=string.lower()

t= guy.count("t")
r= guy.count("r")
u= guy.count("u")
e= guy.count("e")

true = t+r+u+e

l= guy.count("l")
o= guy.count("o")
v= guy.count("v")
e= guy.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
  print(f"Your Score is {love_score}\nYou go together like Coke and Mentos")
elif love_score > 40 and love_score < 50:
  print(f"Your Score is {love_score}\nYou're ALLLright")
else:
  print(f"Your Score is {love_score}, Not Baddddd")
