class LLNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.array = [LLNode()]*1000

    def put(self, key: int, value: int) -> None:
        idx_key = key % 1000
        pointer = self.array[idx_key]
        while pointer.next is not None:
            if pointer.next.key == key:
                pointer.next.val = value
                return 
            pointer = pointer.next
        pointer.next = LLNode(key, value)

    def get(self, key: int) -> int:
        idx_key = key % 1000
        if self.array[idx_key].next is None:
            return -1
        
        pointer = self.array[idx_key]
        while pointer is not None:
            if pointer.key == key:
                return pointer.val
            else:
                pointer = pointer.next
        return -1

    def remove(self, key: int) -> None:
        idx_key = key % 1000
        pointer = self.array[idx_key]
        while pointer.next is not None:
            temp = pointer.next
            if pointer.next.key == key:
                pointer.next = temp.next
                temp.next = None
                return
            else:
                pointer = pointer.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)