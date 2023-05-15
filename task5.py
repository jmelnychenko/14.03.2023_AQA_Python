import null as null
import requests


url = "https://dummyjson.com/users?limit=100"

response = requests.get(url)

my_users = response.json()

list_of_men = my_users['users']
brown_man_age = 0
brown_man_count = 0
browm_avarage_age = 0

# середній вік чоловіків з Brown волоссям
for man in list_of_men:
    man_age = man.get('age', 0)
    man_hair = man.get('hair')['color']

    if man_hair == "Brown":
        brown_man_age += man_age
        brown_man_count += 1
        brown_avarage_age = brown_man_age/brown_man_count
print(int(brown_avarage_age))

#список людей, що проживають в місті Louisville
list_Louisville = []
for man in list_of_men:
    man_city = man.get('address', {}).get('city')
    if man_city == 'Louisville':
        list_Louisville.append(man)
print(list(list_Louisville))

