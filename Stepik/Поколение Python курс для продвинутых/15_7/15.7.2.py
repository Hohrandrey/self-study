from functools import reduce

data = [
    ["Bangkok", 18180280, "admin"],
    ["Karachi", 21422590, "primary"],
    ["Bengaluru", 13187098, "primary"],
]

filtered_data = filter(lambda town: town[1] > 10000000 and town[2] == "primary", data)
sorted_filtered_data = list(sorted(filtered_data, key=lambda town: town[0]))
res_data = reduce(
    lambda string, town: string + town[0] + ", ", sorted_filtered_data, "Cities: "
)

print(res_data[:-2])
