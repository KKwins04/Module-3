from datetime import date, time, datetime

#Calling the today
#Function of Date class
today = date.today()
now = datetime.now()
print("Today's date is: ", today)
print("\nCurrent date and time is: ", now)

#Printing data's components
print("\nDate components", today.year, today.month, today.day)