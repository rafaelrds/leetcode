from collections import defaultdict
from datetime import datetime
from bisect import bisect_left


def now():
    timestamp = int(datetime.now().timestamp())
    return timestamp


class HistoricalMap:
    def __init__(self):
        self.map = defaultdict(list)

    def put(self, key, value):
        self.map[key].append(tuple([now(), value]))

    def get(self, key, timestamp=now()):
        elements = self.map.get(key)

        if not elements:
            raise ValueError("Key not found!")

        idx = bisect_left(elements, timestamp)
        if idx == 0:
            raise ValueError("Key not found at that time!")

        ts, val = elements[idx]
        if ts == timestamp or idx == len(timestamp) - 1:
            match = val
        else:
            match = elements[idx - 1][1]
        return match
