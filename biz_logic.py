def calc_price(item_count, unit_price, discount_item_count=0, discount_price=0):
    if discount_item_count > 0:
        total_discount_item_price = (item_count // discount_item_count) * discount_price
        total_item_price = (item_count % discount_item_count) * unit_price
        return total_item_price + total_discount_item_price
    else:
        return item_count * unit_price
