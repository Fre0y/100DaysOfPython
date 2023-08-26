user = input("Your Name :-")

life = int(input("Whats your age :- "))

year_remaining = 90 - life

days = year_remaining * 365
weeks = year_remaining * 52
months = year_remaining * 12

print(f"Hello {user} you have {year_remaining} year remainig, {days} days, {weeks} weeks, {months} months")
