# # Task 2.1
user_input = input('Input: ')
print("Word {0} has {1} letters.".format(user_input, str(len(user_input))))

# Task 2.2 - Касир в кінотеватрі
user_age = input('Enter your age: ')
ua_var = int(user_age)  #user_age_variable
if type(ua_var) == int:
    if 7 > ua_var > 0:
        print("Де твої батьки")
    elif ua_var == 7:
        print("Вам сьогодні пощастить!")
    elif 16 > ua_var > 7:
        print("Це фільм для дорослих!")
    elif 99 > ua_var >= 65:
        print("Покажіть пенсійне посвідчення!")
    else:
        print("А білетів вже немає!")
else:
    print("Not a digit! Try again.")

