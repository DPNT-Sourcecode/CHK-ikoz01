

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
    special_price = {'A': [{"quantity": 3, 'price': 130}], 'B': [{"quantity": 2, 'price': 45}]}

    sku_quantity_map = defaultdict(int)
    for char in skus:
        sku_quantity_map[char] +=1
    raise NotImplementedError()


