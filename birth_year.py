from datetime import date, datetime
birth_year = int(input("What year were you born? \n"))
current_year = date.today().year
age = current_year - birth_year
print(f"You are currently {age} years old.")

#Without imports
#birth_year = int(input("What year were you born in? \n"))
#current_year = 2023
#age = current_year - birth_year
#print(f"You are currently {age} years old.")