'''
Apologies if this calculation is less accurate because 
I rounded one year to 365 days and one month to 30 days.
'''
import datetime as dt

print(f"\n{55*'='}")
print("Please Enter Your Date of Birth")
print(f"{55*'='}")

day = int(input("Day   : "))
month = int(input("Month : "))
year = int(input("Year  : "))

specific_time = input("Do you have a specific time of birth? (y/n): ")
print(f"{55*'='}")

if specific_time.lower() == 'y':
    while True:
        hour = int(input("Hour (0-23)   : "))
        if 0 <= hour <= 23:
            break
        else:
            print("Please enter hour in the range of 0 to 23.")

    while True:
        minute = int(input("Minute (0-59) : "))
        if 0 <= minute <= 59:
            break
        else:
            print("Please enter minute in the range of 0 to 59.")
else:
    hour = 0
    minute = 0

date_of_birth = dt.datetime(year, month, day, hour, minute)
print(f"Date of Birth: {date_of_birth.strftime('%d-%m-%Y %H:%M')}")
print(f"{55*'='}")

today = dt.datetime.today()
print(f"Today's date: {today.strftime('%d-%m-%Y %H:%M')}")
age_time = today - date_of_birth
age_years = age_time.days // 365
age_remaining_months = (age_time.days % 365) // 30
age_remaining_days = (age_time.days % 365) % 30
age_hours = age_time.seconds // 3600
age_remaining_minutes = (age_time.seconds % 3600) // 60

print(f"Age: {age_years} years, {age_remaining_months} months, {age_remaining_days} days, {age_hours} hours, {age_remaining_minutes} minutes\n")

