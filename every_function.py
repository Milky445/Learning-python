cities = []

cities.insert(0, 'Dubai')
cities.insert(2, 'Toronto')
cities.append('Albuquerque')
del cities[0]
cities.pop(1)

print(cities)
print(len(cities))