# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:45:06 2022

@author: craig
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
name_lower = name.lower()
name_count_t = name_lower.count("t")
name_count_r = name_lower.count("r")
name_count_u = name_lower.count("u")
name_count_e = name_lower.count("e")
name_count_tens = name_count_t + name_count_r + name_count_u + name_count_e
name_count_l = name_lower.count('l')
name_count_o = name_lower.count("o")
name_count_v = name_lower.count("v")
name_count_e = name_lower.count("e")
name_count_ones = name_count_l + name_count_o + name_count_v + name_count_e
score = (f"{name_count_tens}{name_count_ones}")
score_int = int(score)
if score_int < 10 or score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}, you are soul mates!")