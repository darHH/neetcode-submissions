class TimeMap:
    # keep a dict of dicts, outer dict's key is the normal key, inner dict's key is timestamp
    def __init__(self):
        self.key_store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_store:
            curr_timestamp_store = self.key_store[key]
        else:
            curr_timestamp_store = dict()
            self.key_store[key] = curr_timestamp_store
        curr_timestamp_store[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        curr_store = self.key_store[key]
        filtered_store = {k: v for k, v in curr_store.items() if k <= timestamp}
        if not filtered_store:
            return ""
        latest_value = filtered_store[max(filtered_store)]
        return latest_value

