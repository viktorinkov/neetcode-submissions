class TimeMap:

    def __init__(self):
        self.myMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myMap:
            self.myMap[key] = []

        self.myMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res, pairs = "", self.myMap.get(key, [])

        n = len(pairs)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] <= timestamp:
                res = pairs[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
