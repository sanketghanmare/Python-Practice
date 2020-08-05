# private variable does not exist in python but anything which starts
# __(underscore) has the intention similar to private and does not mean
# to change but it is upto a user whether or not to change it.
import shelve

print(dir())
print(dir(__builtins__))
print()
print(dir(shelve))

for m in dir(__builtins__):
    print(m)

help(shelve)
