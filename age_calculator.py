from datetime import datetime


def calculate_age(birthdate):
    now = datetime.now()
    age = now - birthdate
    years = age.days // 365
    days = age.days % 365
    hours = age.seconds // 3600
    minutes = (age.seconds % 3600) // 60
    return years, days, hours, minutes

# Example usage:
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
years, days, hours, minutes = calculate_age(birthdate)
print(f"You are {years} years, {days} days, {hours} hours, and {minutes} minutes old.")
