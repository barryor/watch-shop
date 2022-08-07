# Abstraction of Data Access Layer
import csv

__all__ = ['fetch_by_id']

cached_data = None


def fetch_by_id(watch_id: str) -> dict:
    global cached_data
    if cached_data is None:
        with open('test_data.csv', newline='') as test_data_file:
            reader = csv.DictReader(test_data_file)
            cached_data = [row for row in reader]

    for watch in cached_data:
        if watch['id'] == watch_id:
            return watch
    return None
