# according to time say good morning,afternoon,evening

import time

t = time.strftime("%H:%M:%S")
print(t)
hour = int(time.strftime("%H"))
print(hour)

if (hour > 0 and hour < 12):
    print("good morning sir!")
elif (hour >= 12 and hour < 17):
    print("good afternoon sir!")
else:
    print("good evening sir !!")
