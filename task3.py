# Task 3.1
while True:
    o_loop = input("Enter any word: ")
    if o_loop.lower().__contains__('o'):
        break
    print("Your word {} does not contain 'o' Try again:".format(o_loop))
print("Congrats! Your word {} contains 'o'".format(o_loop))

# Task 3.2
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if type(i) is str:
        lst2.append(i)
print(lst2)

# Task 3.3
user_input_str = "test string.o hello trololO"
user_input_list = user_input_str.lower().split()
tmp_value = 0
for i in user_input_list:
    if i.endswith("o"):
        tmp_value += 1

print("The number of words with that end with 'o': {}".format(tmp_value))
