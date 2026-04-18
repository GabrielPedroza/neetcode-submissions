class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value = ""

        l, r = 0, len(self.time_map[key]) - 1

        while l <= r:
            curr_index = l + (r - l) // 2
            curr_value = self.time_map[key][curr_index][0]
            curr_timestamp = self.time_map[key][curr_index][1]

            if curr_timestamp <= timestamp:
                value = curr_value
                l = curr_index + 1
            else:
                r = curr_index - 1

        return value