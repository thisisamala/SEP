from datetime import datetime, date

birth_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
today = date.today()

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

day_of_week = birth_date.strftime("%A")

next_birthday = birth_date.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_until_birthday = (next_birthday - today).days

print(f"\nYou are {age} years old.")
print(f"You were born on a {day_of_week}.")
print(f"There are {days_until_birthday} days until your next birthday.")

