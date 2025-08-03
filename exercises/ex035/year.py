import time
from datetime import date
year = int(input("Type the year: \n"))
if year == 0:
    year = date.today().year
print("Processing...")
time.sleep(2)
if year % 4 == 0 and year % 100 != 0  or year % 400 == 0:
    print("The year is leap year")
else:
    print("The year is not leap year")