import random
name = input("Enter your name:-")
n = name.split(",")
li = len(n)
num_r = random.randint(0,li-1)
meal = n[num_r]
print(f"{meal} is going to buy meal")
