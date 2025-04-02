

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
value_price_map = {'A':50, 'B': 30, 'C':20, 'D':15, 'E':40, 'F':10}
special_price = {'A': [{"quantity": 5, 'price': 200},{"quantity": 3, 'price': 130}, ], 'B': [{"quantity": 2, 'price': 45}], 
'E': [{"quantity": 2, 'free': {'B':1}}], 'F': [{"quantity": 2, 'free': {'F':1}}]}

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

    free_B = 0
    total_price = 0
    if sku_quantity_map["E"] > 0:
        offer = special_price["E"][0]
        offer_quantity = offer.get('quantity')
        offer_free_item = offer.get('free')['B']
        offer_free_item_sku = 'B'

        quantity_E = sku_quantity_map["E"] 
        free_B = offer_free_item * (quantity_E // offer_quantity)
        if sku_quantity_map["B"] - free_B >= 0:
            sku_quantity_map["B"] -= free_B
        


    for sku, quantity in sku_quantity_map.items():
        if sku not in value_price_map:
            return -1
        
        min_price = quantity* value_price_map.get(sku, float('inf'))
        remaining_quantity = quantity
        if sku == "F" and sku_quantity_map["F"] > 0:

            offer = special_price["F"][0]
            offer_quantity = offer.get('quantity')
            offer_free_item = offer.get('free')['F']
            offer_free_item_sku = 'F'
            quantity_F = sku_quantity_map["F"] 
            remaning =  (quantity_F % (offer_quantity+offer_free_item))
            special_quantity = (quantity_F // (offer_quantity+offer_free_item)) * offer_quantity

            min_price = min(min_price, (special_quantity+remaning) *  value_price_map.get(sku, float('inf')))


        elif sku != "E" and sku in special_price:
            offers = special_price[sku]

            offer_price_product = 0
            for offer in offers:
                offer_quantity = offer.get('quantity')
                offer_price = offer.get('price')

                offer_price_product += (remaining_quantity//offer_quantity) * offer_price 
                remaining_quantity = (remaining_quantity%offer_quantity)
                

            min_price = min(min_price, offer_price_product+ remaining_quantity * value_price_map.get(sku, float('inf')))

        total_price += min_price

    return total_price


print(checkout("FFFF"))


