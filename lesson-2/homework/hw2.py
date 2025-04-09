from datetime import datetime

name = input("Enter your name: ")

year_of_birth = int(input("Enter your year of birth: "))

current_year = datetime.now().year

age = current_year - year_of_birth

print(f"Hello, {name}! You are {age} years old.")
