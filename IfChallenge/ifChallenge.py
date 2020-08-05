name = str(input("Please enter your name \n"))
age = int(input("Please enter your age \n"))

if 18 <= age < 31:
    print(f"Welcome to Holiday club {name}")
else:
    print(f"Sorry you are not allowed to enter due to invalid age group")
