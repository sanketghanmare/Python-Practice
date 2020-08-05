# cities = ["Boston", "Montreal", "Nagpur", "Sydney", "Tokyo", "Paris"]
#
# with open("cities.txt", 'w') as city_files:
#     for city in cities:
#         # Named argument city_files
#         print(city, file=city_files)

cities = []

with open("cities.txt", 'r') as city_files:
    for city in city_files:
        cities.append(city.strip('\n'))

print(cities)
