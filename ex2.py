import random
import timeit

#AI declaration: used it to clean up the cpode

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def binary_search(arr, x): #basic binary search 
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def bst_performance_time (arr): #measuremennt function to caclc the times 
    root = None
    total_time = 0
    for element in arr:
        root = insert(root, element)
    for element in arr:
        start_time = timeit.default_timer()
        search(root, element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / len(arr), total_time

def binarysearch_performance_time(arr): #measures the binary search pperformance
    sorted_arr = sorted(arr)
    total_time = 0
    for element in arr:
        start_time = timeit.default_timer()
        binary_search(sorted_arr, element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / len(arr), total_time

# Generating a shuffled vector
vector = list(range(100000))
random.shuffle(vector)

# Measuring BST performance
bst_average_time, bst_total_time = bst_performance_time(vector)
print("Avg time (BST search):", bst_average_time)
print("total time (BST search):", bst_total_time)

# Measuring binary search performance
binary_search_average_time, binary_search_total_time = binarysearch_performance_time(vector)
print("Avg time (Binaery search):", binary_search_average_time)
print("total time (Binaery search):", binary_search_total_time)

# Comparing performance
if bst_average_time < binary_search_average_time:
    print("BST is quicker.")
else:
    print("Binary search is quicker .")
