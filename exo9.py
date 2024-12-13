cities = []

print("Enter the names of cities. Type 'stop' to finish.")

while True:
        city = input("Enter the city: ").strip()
        if city.lower() == 'stop':
            break
        cities.append(city)

for city in cities:
        population = len(city) * 1000000
        print(f"The city {city} has {len(city)} letters, so its population is: {population}")