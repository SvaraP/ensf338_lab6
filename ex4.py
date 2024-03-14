class Heap:
    def emptyArray(self):
        # Initializes an empty array
        self.storage = []
    #part 1
    # Store array and transforms it into a heap.
    def heapify(self, arr):
        self.storage = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapSiftdown(i)
    #part 2
    # Adds element to heap
    def enqueue(self, element):
        self.storage.append(element)
        self.heapSiftUp(len(self.storage) - 1)
    #part 3
    # Remove root element from  heap
    def dequeue(self):
        if len(self.storage) > 0:
            self.exchange(0, len(self.storage) - 1)
            item = self.storage.pop()
            self.heapSiftdown(0)
            return item
        return None
    #Ai Decleartion: Used Chatgbt to fix the code for maintaining the heap 
    def heapSiftUp(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.storage[index] < self.storage[parent]:
            self.exchange(index, parent)
            index, parent = parent, (parent - 1) // 2
     #maintain heap property when elements are removed.
    def heapSiftdown(self, index):
        size = len(self.storage)
        while index * 2 + 1 < size:
            least = index * 2 + 1
            if least + 1 < size and self.storage[least + 1] < self.storage[least]:
                least += 1
            if self.storage[index] <= self.storage[least]:
                break
            self.exchange(index, least)
            index = least
    #swap elements in heap
    def exchange(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
    #Ai Decleartion: Used Chatgbt to help us outline how to write the tests, which we then followed: 
def testHeapWithSortedArrayInput():
    heap = Heap()
    sortedArrayInput = [5, 6, 7, 8, 9, 10]
    heap.heapify(sortedArrayInput)
    expectedOutput = sortedArrayInput
    assert heap.storage == expectedOutput, "Test failed"

def testHeapWithEmptyArrayInput():
    heap = Heap()
    emptyArrayInput = []
    heap.heapify(emptyArrayInput)
    expectedOutput = []
    assert heap.storage == expectedOutput, "Test failed"

def testHeapWithRandomArrayInput():
    heap = Heap()
    random_input = [5, 1, 8, 3, 6, 2, 7, 4]
    heap.heapify(random_input)
    expectedOutput = sorted(random_input)
    assert sorted(heap.storage) == expectedOutput, "Test failed"

# Run tests
testHeapWithSortedArrayInput()
testHeapWithEmptyArrayInput()
testHeapWithRandomArrayInput()

print("All tests passed.")
