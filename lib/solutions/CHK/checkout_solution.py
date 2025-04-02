

# noinspection PyUnusedLocal
# skus = unicode string

# Our price table and offers:
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


# Notes:
#  - For any illegal input return -1

# In order to complete the round you need to implement the following method:

# checkout(string) -> integer
#  - param[0] = a string containing the SKUs of all the products in the basket
#  - @return = an integer representing the total checkout value of the items

from collections import int

def checkout(skus):
    value_price_map = {'A':50, 'B': 30, 'C':20, 'D':15}
    special_price = {'A': {"quantity": 3, 'price': 130}, 'B': {"quantity": 2, 'price': 45}}

    sku_quantity_map = defaultdict(int)
    for char in skus:
        sku_quantity_map[char] +=1

    total_price = 0
    for sku, quantity in sku_quantity_map.items():
        if sku not in value_price_map:
            return -1
        min_price = quantity* value_price_map.get(sku, float('inf'))

        if sku in special_price:
            offer = special_price[sku]
            offer_quantity = offer.get('quantity')
            offer_price = offer.get('price')

            offer_price = (quantity//offer_quantity) * offer_price + (quantity%offer_quantity) * value_price_map.get(sku, float('inf'))
            min_price = min(min_price, offer_price)

        total_price += min_price


print(checkout("AAB"))




