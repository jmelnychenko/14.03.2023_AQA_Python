# Task 4.1
list1 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

list1[:] = [item for item in list1 if 74 >= item >= 21]

print(list1)

# Task 4.2
dict_products = {
    "citos": 47.999,
    "BB_studio": 42.999,
    "mo-no": 49.999,
    "my-main-service": 37.245,
    "buy-now": 38.324,
    "x-store": 37.166,
    "the-partner": 38.988,
    "store-123": 37.720,
    "roze-tka": 38.003
}

lower_limit = 35.9
upper_limit = 37.339

for key, value in dict_products.items():
    if 37.339 >= value >= 35.9:
        print(key, value)