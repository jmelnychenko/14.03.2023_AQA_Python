# # Task 2.1
user_input = input('Input: ')
print("Word {0} has {1} letters.".format(user_input, str(len(user_input))))

# Task 2.2 - Касир в кінотеватрі
user_age = input('Enter your age: ')
if user_age.isdigit():
    ua_var = int(user_age)
    if '7' in user_age:
        print("Вам сьогодні пощастить!")
    elif ua_var < 7:
        print("Де твої батьки")
    elif ua_var < 16:
        print("Це фільм для дорослих!")
    elif 99 > ua_var >= 65:
        print("Покажіть пенсійне посвідчення!")
    elif ua_var >= 99:
        print("Некоректний вік")
    else:
        print("А білетів вже немає!")
else:
    print("Not a digit! Try again.")

