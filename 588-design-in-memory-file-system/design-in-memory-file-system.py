class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = ""
class FileSystem:
    def __init__(self):
        self.root = TrieNode()
    def ls(self, path: str) -> List[str]:
        paths = path.split("/")[1:]
        node = self.root
        if path == "/":                          # ← add this
            return sorted(node.children.keys()) # ← and this
        for p in paths:
            node = node.children[p]
        if node.val:
            return [paths[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        paths = path.split("/")[1:]
        node = self.root
        for path in paths:
            if path not in node.children:
                node.children[path] = TrieNode()
            node = node.children[path]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath.split("/")[1:]
        node = self.root
        for path in paths:
            if path not in node.children:
                node.children[path] = TrieNode()
            node = node.children[path]
        node.val += content
        

    def readContentFromFile(self, filePath: str) -> str:
        paths = filePath.split("/")[1:]
        node = self.root
        for path in paths:
            node = node.children[path]
        return node.val
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)