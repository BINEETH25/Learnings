class MyHashSet:
    
    def __init__(self):
        self.data = set()
        
    def add(self, key: int) -> None:
        self.data.add(key)
    
    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.data
    
    def printshow(self):
        return self.data

myHashset = MyHashSet()
myHashset.add(1)
myHashset.add(4)
print(myHashset.contains(1))
print(myHashset.contains(3))
myHashset.add(2)
print(myHashset.contains(2))
myHashset.remove(2)
print(myHashset.contains(2))
print(myHashset.printshow())