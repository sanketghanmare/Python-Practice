import shelve

with shelve.open("shelhtext") as fruit:
    fruit["lemon"] = "sweet and aour"
    fruit["apple"] = "keeps docter away"

    print(fruit["apple"])

print(fruit)

fruit = shelve.open("shelhtext")
fruit["lemon"] = "sweet and aour"
fruit["apple"] = "keeps docter away"

print(fruit["apple"])
fruit.close()
print(fruit)
