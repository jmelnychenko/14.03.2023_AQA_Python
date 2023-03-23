# Task 2.1
user_input = input('Input: ')
print("Word " + user_input + " has " + str(len(user_input)) + " letters.")

# Task 2.2 - Касир в кінотеватрі
user_age = input('Enter your age: ')
if user_age.isdigit():
    if 7 > int(user_age) > 0:
        print("Де твої батьки")
    elif int(user_age) == 7:
        print("Вам сьогодні пощастить!")
    elif 16 > int(user_age) > 7:
        print("Це фільм для дорослих!")
    elif 99 > int(user_age) >= 65:
        print("Покажіть пенсійне посвідчення!")
    else:
        print("А білетів вже немає!")
else:
    print("Not a digit! Try again.")

