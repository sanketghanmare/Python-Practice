import pickle

odd = list(range(1, 10, 2))
even = list(range(0, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(odd, pickle_file)
    pickle.dump(even, pickle_file)

with open("imelda.pickle", "rb") as pickleFile:
    odd_list = pickle.load(pickleFile)
    even_list = pickle.load(pickleFile)

for i in even_list:
    print(i)

print()

for o in odd_list:
    print(o)
