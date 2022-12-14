# Provides the checkout business logic to teh application
from data_layer.pricing import fetch_by_id

__all__ = ['calculate_total']

MAX_ORDER_SIZE = 1000

def calc_watch_price(data: dict, watch_count):
    if data['discount'] is None:
        return watch_count * int(data['unit_price'])
    else:
        parsed_discount = data['discount'].split("for")
        discount_item_count = int(parsed_discount[0])
        discount_price = int(parsed_discount[1])
        total_discount_item_price = (watch_count // discount_item_count) * discount_price
        total_item_price = (watch_count % discount_item_count) * int(data['unit_price'])
        return total_item_price + total_discount_item_price


def calculate_total(watch_ids: list):
    if watch_ids is None:
        return None

    # Limit the number watches we can order to protect the data_layer layer
    if len(watch_ids) > MAX_ORDER_SIZE:
        return None

    watch_id_counts = {watch_id: watch_ids.count(watch_id) for watch_id in watch_ids}
    total_price = 0
    for watch_id, count in watch_id_counts.items():
        data = fetch_by_id(watch_id)
        if data is None:
            return None
        else:
            total_price += calc_watch_price(data, count)

    return total_price
