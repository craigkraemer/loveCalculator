print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
name_lower = name.lower()
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
tens_place = t + r + u + e
l = name_lower.count('l')
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
ones_place = l + o + v + e
score = int((f"{tens_place}{ones_place}"))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}, you are soul mates!")