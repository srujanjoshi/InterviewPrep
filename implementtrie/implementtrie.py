class TrieNode:
    
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.isEnd = False




class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children: 
                current.children[c] = TrieNode(c)
            current = current.children[c]
        current.isEnd = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        if current.isEnd == True:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix: 
            if c not in current.children:
                return False
            current = current.children[c]
        
        return True 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)