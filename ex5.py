import random
import timeit

#Ai declaration : Used both Chatgbt and stackoverflow to fix this code as it was very buggy
# due to syntax issues  
class ListNode:
    def __init__(self, value, nextNode=None):
        # Initialize a ListNode with a value and a reference to the next node
        self.value = value
        self.nextNode = nextNode

class ListPriorityQueue:
    def __init__(self):
        # Initialize an empty priority queue
        self.headNode = None

    def enqueueElement(self, element):
        # Insert an element in the priority queue in sorted order
        newNode = ListNode(element)
        if not self.headNode or element < self.headNode.value:
            newNode.nextNode = self.headNode
            self.headNode = newNode
        else:
            current = self.headNode
            while current.nextNode and current.nextNode.value < element:
                current = current.nextNode
            newNode.nextNode = current.nextNode
            current.nextNode = newNode

    def dequeueElement(self):
        # Remove and return the first (smallest) element of the queue
        if self.headNode is None:
            return None
        removedElement = self.headNode.value
        self.headNode = self.headNode.nextNode
        return removedElement

    def peekElement(self):
        # Return the first element without removing it
        if self.headNode is None:
            return None
        return self.headNode.value

class HeapPriorityQueue:
    def __init__(self):
        # Initialize an empty heap array
        self.heapArray = []

    def enqueueElement(self, element):
        # Add an element to the heap and maintain the heap structure
        self.heapArray.append(element)
        self.heapSiftUp(len(self.heapArray) - 1)

    def dequeueElement(self):
        # Remove and return the smallest element from the heap
        if not self.heapArray:
            return None
        self.exchangeElements(0, len(self.heapArray) - 1)
        item = self.heapArray.pop()
        self.heapSiftdown(0)
        return item

    def peekElement(self):
        # Return the smallest element without removing it
        if self.heapArray:
            return self.heapArray[0]
        return None

    def heapSiftUp(self, index):
        # Adjust the heap upwards to maintain the heap property
        parent = (index - 1) // 2
        while index > 0 and self.heapArray[parent] > self.heapArray[index]:
            self.exchangeElements(parent, index)
            index, parent = parent, (parent - 1) // 2

    def heapSiftdown(self, index):
        # Adjust the heap downwards to maintain the heap property
        child = 2 * index + 1
        while child < len(self.heapArray):
            if child + 1 < len(self.heapArray) and self.heapArray[child + 1] < self.heapArray[child]:
                child += 1
            if self.heapArray[index] <= self.heapArray[child]:
                break
            self.exchangeElements(index, child)
            index = child
            child = 2 * index + 1

    def exchangeElements(self, i, j):
        # Swap two elements in the heap
        self.heapArray[i], self.heapArray[j] = self.heapArray[j], self.heapArray[i]

# generate a list of 1000 tasks
def generateTask():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:  # 70% chance to enqueue
            tasks.append(('enqueue', random.randint(1, 1000)))
        else:  # 30% chance to dequeue
            tasks.append(('dequeue', None))
    return tasks

#  tasks with ListPriorityQueue
def processTasksListQueue(tasks):
    queue = ListPriorityQueue()
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueueElement(task[1])
        else:
            queue.dequeueElement()

#  tasks with HeapPriorityQueue
def processTasksHeapQueue(tasks):
    queue = HeapPriorityQueue()
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueueElement(task[1])
        else:
            queue.dequeueElement()

# Generate the tasks
tasks = generateTask()

# execution time 
timeListQueue = timeit.timeit(lambda: processTasksListQueue(tasks), number=1)
timeHeapQueue = timeit.timeit(lambda: processTasksHeapQueue(tasks), number=1)

# Calculate average time per task
averageTimePerTaskList = timeListQueue / 1000
averageTimePerTaskHeap = timeHeapQueue / 1000

# Print the results
print(f"ListPriorityQueue's Total Time: {timeListQueue:.6f} seconds, Average Time per Task: {averageTimePerTaskList:.6f} seconds")
print(f"HeapPriorityQueue's Total Time: {timeHeapQueue:.6f} seconds, Average Time per Task: {averageTimePerTaskHeap:.6f} seconds")

#discussion : 

#The HeapPriorityQueue typically outperforms the ListPriorityQueue in terms of speed. This is because, in a linked list 
#(used in ListPriorityQueue), insertions and deletions often require traversing through the list, which can be time-consuming. 
#On the other hand, a heap, which is the underlying structure of the HeapPriorityQueue, allows for quicker operations. 
#The heap's design enables it to manage large volumes of elements more efficiently, thanks to its faster insertions and deletions."