
# 1. Implement a binary search tree with insertion and search operations as seen in class [0.2 pts]
import timeit
import random
import bisect

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if node.val < key:
            return self._search(node.right, key)
        return self._search(node.left, key)

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
sorted_vector = list(range(1000))

# Build BST using sorted vector
bst_sorted = BST()
for element in sorted_vector:
    bst_sorted.insert(element)

# Measure search performance on sorted vector
avg_time_sorted, total_time_sorted = measure_search_performance(bst_sorted, sorted_vector)

print("Search Performance on Sorted Vector:")
print("Average time per search:", avg_time_sorted)
print("Total time for all searches:", total_time_sorted)

# Shuffle the vector
random.shuffle(sorted_vector)

# Build BST using shuffled vector
bst_shuffled = BST()
for element in sorted_vector:
    bst_shuffled.insert(element)

# Measure search performance on shuffled vector
avg_time_shuffled, total_time_shuffled = measure_search_performance(bst_shuffled, sorted_vector)

print("\nSearch Performance on Shuffled Vector:")
print("Average time per search:", avg_time_shuffled)
print("Total time for all searches:", total_time_shuffled)


# 3. Measure search performance using timeit as follows: [0.3 pts]
    # Shuffle the vector used for question 2 (using random.shuffle)
    # Search each element. Time the search (averaged across 10 tries for each element), and return average and total time
# Shuffle the vector
random.shuffle(sorted_vector)

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
This linear search behavior leads to longer average search times.
However, in the case of the shuffled vector, where elements are inserted into the BST in a more randomized order, the tree maintains better balance. 
As a result, the search operation becomes more efficient, as the tree's height is minimized, leading to faster search times.
'''