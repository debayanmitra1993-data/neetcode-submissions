class LLNode:
    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.remove(node)
        self.insert(node)
        return node.value
    
    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.head.prev = node
        node.next = self.head
        self.head = node
    
    def remove(self, node):
        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None
        elif node.prev is None and node.next is not None:
            self.head = node.next
            self.head.prev = None
        elif node.prev is not None and node.next is None:
            self.tail = node.prev
            self.tail.next = None
        elif node.prev is not None and node.next is not None:
            node.next.prev = node.prev
            node.prev.next = node.next
        node.prev = None
        node.next = None

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        elif key not in self.hashmap:
            node = LLNode(key, value)
            self.insert(node)
            self.hashmap[key] = node
        
        if len(self.hashmap) > self.capacity and self.tail is not None:
            key_to_remove = self.tail.key
            node_to_remove = self.tail
            self.remove(node_to_remove)
            del self.hashmap[key_to_remove]