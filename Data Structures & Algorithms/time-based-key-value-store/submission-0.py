class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(value, timestamp)]
        else:
            self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        array = self.hashmap[key]
        nearest_val = ""
        lidx, ridx = 0, len(array) - 1
        while lidx <= ridx:
            midx = (lidx + ridx)//2
            if array[midx][1] == timestamp:
                return array[midx][0]
            elif array[midx][1] > timestamp:
                ridx = midx - 1 
            elif array[midx][1] < timestamp:
                lidx = midx + 1
                nearest_val = array[midx][0]
        return nearest_val
            

        
