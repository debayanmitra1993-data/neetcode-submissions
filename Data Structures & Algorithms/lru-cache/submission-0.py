class LLNode:
    def __init__(self, key, value, prevp = None, nextp = None):
        self.key = key
        self.value = value
        self.prevp = prevp
        self.nextp = nextp

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.curr_capacity = 0
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
        else:
            self.head.prevp = node
            node.nextp = self.head
            self.head = node

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            self.hashmap[key] = node
        else:
            node = LLNode(key, value)
            self.insert(node)
            self.hashmap[key] = node
            self.curr_capacity += 1
        
        if self.curr_capacity > self.capacity:
            node = self.hashmap[self.tail.key]
            del self.hashmap[self.tail.key]
            self.remove(node)
            self.curr_capacity -= 1
        
    def remove(self, node):
        if node.nextp is not None and node.prevp is not None:
            node.prevp.nextp = node.nextp
            node.nextp.prevp = node.prevp
        elif node.nextp is None and node.prevp is not None:
            self.tail = self.tail.prevp
            self.tail.nextp = None
        elif node.nextp is not None and node.prevp is None:
            self.head = self.head.nextp
            self.head.prevp = None
        else:
            self.head = None
            self.tail = None
        
        node.prevp = None
        node.nextp = None


        
