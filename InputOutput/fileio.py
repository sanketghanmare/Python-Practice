jabber = open('sample.txt', 'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end="")
#
# jabber.close()

# No need to explicity close the file if using with it will also handles
# error
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "jabberwock" in line.lower():
#             print(line, end="")


# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end="")
#         line = jabber.readline()


with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end="")

# Reverse print
for line in lines[::-1]:
    print(line, end="")

# Each line reverse
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end="")
