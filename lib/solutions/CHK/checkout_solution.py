

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
# value_price_map = {'A':50, 'B': 30, 'C':20, 'D':15, 'E':40, 'F':10}
# special_price = {'A': [{"quantity": 5, 'price': 200},{"quantity": 3, 'price': 130}, ], 'B': [{"quantity": 2, 'price': 45}], 
# 'E': [{"quantity": 2, 'free': {'B':1}}], 'F': [{"quantity": 2, 'free': {'F':1}}]}
value_price_map = {
    'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60,
    'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20,
    'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
}

special_price = {
    'A': [{"quantity": 5, 'price': 200}, {"quantity": 3, 'price': 130}],
    'B': [{"quantity": 2, 'price': 45}],
    'E': [{"quantity": 2, 'free': {'B': 1}}],
    'F': [{"quantity": 2, 'free': {'F': 1}}],
    'H': [{"quantity": 10, 'price': 80}, {"quantity": 5, 'price': 45}],
    'K': [{"quantity": 2, 'price': 150}],
    'Q': [{"quantity": 3, 'price': 80}],
    'R': [{"quantity": 3, 'free': {'Q': 1}}],
    'U': [{"quantity": 3, 'free': {'U': 1}}],
    'V': [{"quantity": 3, 'price': 130}, {"quantity": 2, 'price': 90}],
    'P': [{"quantity": 5, 'price': 200}],
    'N': [{"quantity": 3, 'free': {'M': 1}}]
}

def apply_free_offers(sku_quantity_map):

    for sku, offers in special_price.items():
        for offer in offers:
            if 'free' in offer:
                offer_quantity = offer['quantity']
                free_item_sku, free_item_count = next(iter(offer['free'].items()))
                
                if sku in sku_quantity_map:
                    free_items_to_take = (sku_quantity_map[sku] // offer_quantity) * free_item_count
                    if free_item_sku in sku_quantity_map:
                        sku_quantity_map[free_item_sku] = max(0, sku_quantity_map[free_item_sku] - free_items_to_take)



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

    apply_free_offers(sku_quantity_map)

    total_price = 0
    for sku, quantity in sku_quantity_map.items():
        if sku not in value_price_map:
            return -1
        
        min_price = quantity* value_price_map.get(sku, float('inf'))
        remaining_quantity = quantity
        if sku in special_price:
            offers = special_price[sku]

            offer_price_product = 0
            for offer in offers:
                if 'price' in offer:
                    offer_quantity = offer['quantity']
                    offer_price = offer['price']

                    if remaining_quantity is not None: 
                        offer_price_product += (remaining_quantity // offer_quantity) * offer_price
                        remaining_quantity %= offer_quantity
                    else:
                        return -1 
            

            min_price = min(min_price, offer_price_product+ remaining_quantity * value_price_map.get(sku, float('inf')))

        total_price += min_price

    return total_price
