# Abstraction of Data Access Layer

__all__ = ['fetch_by_id']

test_data = [
    {'id': '001', 'name': 'Rolex', 'unit_price': '100', 'discount': '3 for 200'},
    {'id': '002', 'name': 'Michael Kors', 'unit_price': '80', 'discount': '2 for 120'},
    {'id': '003', 'name': 'Swatch', 'unit_price': '50'},
    {'id': '004', 'name': 'Casio', 'unit_price': '30'}
]


def fetch_by_id(watch_id: str) -> dict:
    for watch in test_data:
        if watch['id'] == watch_id:
            return watch
    return None
