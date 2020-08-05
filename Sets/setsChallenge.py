string = str(input("Please enter your text: "))
vowels = frozenset("aeiou")

finalSet = set(string.lower()).difference(vowels)
print(finalSet)
finalSet = sorted(finalSet)
print(finalSet)
