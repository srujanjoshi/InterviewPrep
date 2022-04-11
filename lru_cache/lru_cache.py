
class Node:
    def __init__(self, key: int, val:int, nxt =None, prev = None):
        self.key = key 
        self.val = val
        self.next = nxt
        self.prev = prev 
    
    

class LRUCache:
    
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.capacity = capacity
        self.tail = Node(-1, -1)
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def remove(self, node):
        prev_node= node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node 
        
    def add(self, node): 
        old_mru = self.tail.prev 
        old_mru.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = old_mru

    def get(self, key: int) -> int:
        #Check if the key is in the Dictionary
        if key in self.cache:
            #We also need to update cache[key] to be the MRU node/the tail of the list
            #This means 1.)removing the node from the list, and then 2.)inserting it at the tail
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            #We need to 1.)remove the old node from the list,
            self.remove(old_node)
        #Update value of key in the cache to be a node with the new value
        #add the new node to the tail of the list
        new_node = Node(key,value)
        self.cache[key] = new_node
        self.add(new_node)
        #If the size of our cache has been exceeded, we remove the LRU node/head of the list
        if(len(self.cache)>self.capacity):
            del self.cache[self.head.next.key]
            self.remove(self.head.next)
            
# Your LRUCache object will be instantiated and called as such:


capacity = 2
obj = LRUCache(capacity)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))