import timeit
import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left:
                self._insert_recursive(node.left, key)
            else:
                node.left = TreeNode(key)
        elif key > node.key:
            if node.right:
                self._insert_recursive(node.right, key)
            else:
                node.right = TreeNode(key)
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

def measure_bst_performance(data):
    bst = BinarySearchTree()
    total_time = 0
    for _ in range(10):
        random.shuffle(data)
        start_time = timeit.default_timer()
        for item in data:
            bst.insert(item)
        for item in data:
            bst.search(item)
        total_time += (timeit.default_timer() - start_time)
    average_time = total_time / 10
    return average_time, total_time

def measure_binary_search_performance(data):
    total_time = 0
    for _ in range(10):
        random.shuffle(data)
        data.sort()  # Sorting the shuffled data
        start_time = timeit.default_timer()
        for item in data:
            binary_search(data, item)
        total_time += (timeit.default_timer() - start_time)
    average_time = total_time / 10
    return average_time, total_time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    data = list(range(10000))  # Generating a sorted vector
    bst_avg_time, bst_total_time = measure_bst_performance(data)
    print("Binary Search Tree Performance:")
    print("Average time per search:", bst_avg_time)
    print("Total time:", bst_total_time)
    
    binary_search_avg_time, binary_search_total_time = measure_binary_search_performance(data)
    print("\nBinary Search Performance:")
    print("Average time per search:", binary_search_avg_time)
    print("Total time:", binary_search_total_time)
