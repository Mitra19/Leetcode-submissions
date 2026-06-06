class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = -1
class FileSystem:
    
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        parts = path.split("/")[1:]
        print(parts)
        node = self.root
        for i, part in enumerate(parts):
            if part not in node.children:
                if i < len(parts) - 1:
                    return False
                node.children[part] = TrieNode()
            node = node.children[part]
        if node.val != -1:
            return False
        node.val = value
        return True
        

    def get(self, path: str) -> int:
        parts = path.split("/")[1:]
        node = self.root
        for part in parts:
            if part not in node.children:
                return -1
            node = node.children[part]
        return node.val
        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)