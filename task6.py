import requests

google_table_url = 'https://script.google.com/macros/s/AKfycbyebAzn0MmvHgevw' \
                   '-lreLC8wzuk90lI4HTExFeXw2q9ZaT4_w_0a10hz9630hYmV7MSAQ/exec'

table_response = requests.get(google_table_url)
my_goods_json = table_response.json()
my_goods = my_goods_json['goods']

my_goods_cost = 0
my_gluten_goods_cost = 0
my_good_quantity = 0
total_goods_sum = 0
gluten_total_goods_sum = 0

for good in my_goods:
    my_good_cost = good.get('Price', 0)
    my_good_quantity = good.get('Remnant', 0)
    is_gluten_good = good.get('Contains gluten', 0)
    total_good_price = my_good_cost * my_good_quantity
    total_goods_sum += total_good_price

    if is_gluten_good is True:
        gluten_total_goods_sum += total_good_price
print('All products cost is: {}'.format(total_goods_sum))
print('All gluten products cost is: {}'.format(gluten_total_goods_sum))
