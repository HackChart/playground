import datetime

now = datetime.datetime.now() # Creates a time/date obj with the current computer time
print(now)
print(f"This current date is: {now.month}/{now.day}/{now.year}") # Obj has attributes for each aspect of the datetime
print(f"The current time is: {now.hour}:{now.minute}")

then = now
then = then.replace(hour=12, minute=00) # Use .replace to alter the attributes of a datetime obj. Does not perform in-place modification
print(f"After altering the datetime object, the time is: {then.hour}:{then.minute}")

