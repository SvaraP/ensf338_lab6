import sys
sys.setrecursionlimit(50000)

# 1. Implement a binary search tree with insertion and search operations as seen in class [0.2 pts]
import timeit
import random

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, root=None):
        if root is None:
            self.root = Node(data)
            return self.root
        if data <= root.data:
            if root.left is None:
                root.left = Node(data, root)
                return root.left
            else:
                return self.insert(data, root.left)
        else:
            if root.right is None:
                root.right = Node(data, root)
                return root.right
            else:
                return self.insert(data, root.right)

    def search(self, data, root=None):
        if root is None:
            root = self.root
        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None


# 2. Measure search performance using timeit as follows: [0.3 pts]
    # Generate a 10000-element sorted vector and use it to build a tree by inserting each element
    # Search each element. Time the search (averaged across 10 tries for each element), and return average and total time.
    
def measure_search_performance(bst, elements):
    total_time = 0
    for element in elements:
        avg_time = timeit.timeit(lambda: bst.search(element), number=10) / 10
        total_time += avg_time
    return total_time / len(elements), total_time

# Generate a sorted vector
sorted_vector = list(range(10000))

# Build BST using sorted vector
bst_sorted = BST()
for element in sorted_vector:
    bst_sorted.insert(element, bst_sorted.root)

# Measure search performance on sorted vector
avg_time_sorted, total_time_sorted = measure_search_performance(bst_sorted, sorted_vector)

print("Search Performance on Sorted Vector:")
print("Average time per search:", avg_time_sorted)
print("Total time for all searches:", total_time_sorted)


# 3. Measure search performance using timeit as follows: [0.3 pts]
    # Shuffle the vector used for question 2 (using random.shuffle)
    # Search each element. Time the search (averaged across 10 tries for each element), and return average and total time

# Shuffle the vector
random.shuffle(sorted_vector)

# Build BST using shuffled vector
bst_shuffled = BST()
for element in sorted_vector:
    bst_shuffled.insert(element, bst_shuffled.root)

# Measure search performance on shuffled vector
avg_time_shuffled, total_time_shuffled = measure_search_performance(bst_shuffled, sorted_vector)

print("\nSearch Performance on Shuffled Vector:")
print("Average time per search:", avg_time_shuffled)
print("Total time for all searches:", total_time_shuffled)


# 4. Discuss the results. Which approach is faster? Why? [0.2 pts]
''' 
The approach with the shuffled vector is faster, this is due to the difference in the structure of the Binary Search Tree.
In the case of the sorted vector, when elements are inserted into the BST in sorted order, the tree becomes highly unbalanced, resembling a linked list. 
As a result, the search operation becomes inefficient, as it has to traverse through a long linear chain to find the desired element. 
This linear search behavior leads to longer average search times, O(n).
However, in the case of the shuffled vector, where elements are inserted into the BST in a more randomized order, the tree maintains better balance. 
As a result, the search operation becomes more efficient, as the tree's height is minimized, leading to faster search times, O(log n).
'''