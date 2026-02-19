# Task 1
dict1 = {'x': 10, 'y': 20}
dict1.clear()

# Task 2
dict_ = {'a': 1, 'b': 2, 'c': 1}
print(list(dict_.keys()))

# Task 3
for k, v in dict_.items():
    print(k, v)

# Task 4
dict4 = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
dict4 = {k: v for k, v in dict4.items() if v >= 4}

# Task 5
dict5 = {1: {'a': 1}, 2: {'b': 4}, 3: {'c': 1}, 4: {'d': 5}, 5: {'e': 6}}
dict5 = {k: list(v.keys())[0] for k, v in dict5.items()}

# Task 7
dict7 = {'a': 1, 'b': 2, 'c': 1}
dict7['d'] = 3

# Task 9
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
dict9 = d1.copy()
dict9.update(d2)