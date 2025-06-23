class MyHashMap:
    
    def __init__(self):
        self.size = 10
        self.buckets = [[] for _ in range(self.size)]
        
    def put(self, key : int, value : int) -> None:
        index = key % self.size
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key: int) -> int:
        index = key % self.size
        bucket = self.buckets[index]
        
        for (k, v) in bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


myHashMap =  MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))
print(myHashMap.get(3))
myHashMap.put(2, 1)
print(myHashMap.get(2))
myHashMap.remove(2)
print(myHashMap.get(2))