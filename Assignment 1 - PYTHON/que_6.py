input_list = [
    ["cat1","a"],
    ["cat1","b"],
    ["cat2","c"],
    ["cat2","d"],
    ["cat3","e"]
]

results = {}

for key, value in input_list:
    if key not in results:
        results[key] = []
    results[key].append(value)


print(input_list)
print()
print(results)



