# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.


import pytz
import datetime

# for x in sorted(pytz.country_names):
#     print(x + ':' + pytz.country_names[x])

timeList = {"1": "AU:Australia",
            "2": "CF:Central",
            "3": "African Rep.",
            "4": "DE:Germany",
            "5": "IN:India",
            "6": "LU:Luxembourg",
            "7": "RU:Russia",
            "8": "US:United States",
            "9": "AQ:Antarctica",
            "0": "Quit"}

print("Please choose one of the time zone or 0 to quit")

for zone in sorted(timeList):
    print(f"{zone} {timeList[zone]}")

while True:
    userInput = input()
    if userInput == '0':
        break

    if userInput in timeList.keys():
        tz_to_display = pytz.timezone(timeList[userInput])
        world_time = datetime.datetime.now(tz_to_display)
        print(f"the time in {timeList[userInput]} is {world_time.strftime('%A %x %X %z')} {world_time.tzname()}")
        print(f"Local time in {datetime.datetime.now().strftime('%A %x %X')}")
        print(f"UTC time in {datetime.datetime.utcnow().strftime('%A %x %X')}")
