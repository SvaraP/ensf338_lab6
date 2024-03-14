class ListNode:
    def __init__(self, value, nextNode=None):
        # Initializes a ListNode with a value and a reference to the next node
        self.value = value
        self.nextNode = nextNode

class ListPriorityQueue:
    def __init__(self):
        # Initializes an empty priority queue
        self.headNode = None

    def enqueueElement(self, element):
        # Inserts an element in the priority queue in sorted order
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
        # Removes and returns the first (smallest) element of the queue
        if self.headNode is None:
            return None
        removedElement = self.headNode.value
        self.headNode = self.headNode.nextNode
        return removedElement

    def peekElement(self):
        # Returns the first element without removing it
        if self.headNode is None:
            return None
        return self.headNode.value

 
 #--------------------------class HeapPriorityQueue:
    def __init__(self):
        # Initializes an empty heap array
        self.heapArray = []

    def enqueueElement(self, element):
        # Adds an element to the heap and maintains the heap structure
        self.heapArray.append(element)
        self.heapSiftUp(len(self.heapArray) - 1)

    def dequeueElement(self):
        # Removes and returns the smallest element from the heap
        if not self.heapArray:
            return None
        self.exchangeElements(0, len(self.heapArray) - 1)
        item = self.heapArray.pop()
        self.heapSiftdown(0)
        return item

    def peekElement(self):
        # Returns the smallest element without removing it
        if self.heapArray:
            return self.heapArray[0]
        return None

    def heapSiftUp(self, index):
        # Adjusts the heap upwards to maintain the heap property
        parent = (index - 1) // 2
        while index > 0 and self.heapArray[parent] > self.heapArray[index]:
            self.exchangeElements(parent, index)
            index, parent = parent, (parent - 1) // 2

    def heapSiftdown(self, index):
        # Adjusts the heap downwards to maintain the heap property
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
        # Swaps two elements in the heap
        self.heapArray[i], self.heapArray[j] = self.heapArray[j], self.heapArray[i]
# Measuring the execution time
#time_list_queue = timeit.timeit(process_tasks_list_queue, number=1)
#time_heap_queue = timeit.timeit(process_tasks_heap_queue, number=1)

# Calculate average time per task
#avg_time_per_task_list = time_list_queue / 1000
#avg_time_per_task_heap = time_heap_queue / 1000

# Print the results
#print(f"ListPriorityQueue - Total Time: {time_list_queue} seconds, Avg Time/Task: {avg_time_per_task_list} seconds")
#print(f"HeapPriorityQueue - Total Time: {time_heap_queue} seconds, Avg Time/Task: {avg_time_per_task_heap} seconds")