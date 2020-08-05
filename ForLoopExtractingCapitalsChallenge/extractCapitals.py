quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)

print()

for i in range(0, 10):
    print(f"Number is Now {i}")

print()

for i in range(10):
    print(f"Number is Now {i}")

print()

# In steps of 2
for i in range(0, 11, 2):
    print(f"Number is Now {i}")

print()

# In reverse order steps of 2
for i in range(10, 0, -2):
    print(f"Number is Now {i}")


print()

# Number from 0-100 which are divisible by 7
for i in range(100):
    if i % 7 == 0:
        print(i)
