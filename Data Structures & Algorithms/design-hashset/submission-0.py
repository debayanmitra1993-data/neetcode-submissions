class LLNode:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

class MyHashSet:
    def __init__(self):
        self.array = [LLNode(-1)]*10000

    def add(self, key: int) -> None:
        idx = key % 10000
        pointer = self.array[idx]
        while pointer.next is not None:
            if pointer.next.key == key:
                return 
            pointer = pointer.next
        pointer.next = LLNode(key)

    def remove(self, key: int) -> None:
        idx = key % 10000
        pointer = self.array[idx]
        if pointer.next is None:
            return 
        while pointer.next is not None:
            if pointer.next.key == key:
                removepointer = pointer.next
                pointer.next = removepointer.next
                removepointer.next = None
                return
            pointer = pointer.next

    def contains(self, key: int) -> bool:
        idx = key % 10000
        pointer = self.array[idx]
        if pointer.next is None:
            return False
        while pointer is not None:
            if pointer.key == key:
                return True
            pointer = pointer.next
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)