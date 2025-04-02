

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
value_price_map = {'A':50, 'B': 30, 'C':20, 'D':15}
special_price = {'A': {"quantity": 3, 'price': 130}, 'B': {"quantity": 2, 'price': 45}}

def checkout(skus):
    """
    Returns the checkout value of all skus.

    Args :
    skus : string containing all items

    Returns: 
    An integer with sum of price of all skus including offers.

    -1 if sku is not present in value_price_map
    """
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

    return total_price
