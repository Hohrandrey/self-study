countries = ["Australia", "Canada", "Portugal", "Japan"]
capitals = ["Canberra", "Ottawa", "Lissabon", "Tokyo"]
population = [27_840_775, 41_575_585, 10_749_635, 122_950_000]

for capital, country, population in zip(capitals, countries, population):
    print(
        f"{capital} is the capital of {country}, population equal {population} people."
    )
