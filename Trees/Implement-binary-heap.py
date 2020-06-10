# This is a python program to implement a binary heap.

# The program creates a binary max-heap and presents a menu to the user to perform various operations on it.

# Strategy:

# Create a class BinaryHeap with an instance variable items set to an empty list. 
# This empty list is used to store the binary heap.

# Define methods size, parent, left, right, get, get_max, extract_max, max_heapify, swap and insert.

# Methods:
# size: returns the number of elements in the heap.
# parent: takes an index as argument and returns index of the parent.
# left: takes an index as argument and returns the index of its left child.
# right: takes an index as argument and returns the index of its right child.
# get: takes index as argument and returns the key at the index.
# get_max: returns the maximum element in the heap by returning the first element in the list items.
# extract_max: returns the maximum element in the heap and removes it.
# max_heapify: takes an index as argument and modifies the heap structure at and below the node 
# ...at this index to make it satisfy the heap property.
# swap: takes two index as arguments, and swaps the corresponding elements in the heap.
# insert: takes a key as argument and adds that key to the heap.


# Program:

class BinaryHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def parent(self, i):
        return (i - 1 )// 2

    def left(self, i):
        return 2*1 + 1

    def right(self, i):
        return 2*i + 2

    def get(self, i):
        return self.items[i]

    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= self.size() - 1 and self.get(l) > self.get(i)):
            largest = l
        else:
            largest = i
        if (r <= self.size() - 1 and self.get(r) > self.get(largest)):
            largest = r

        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self, key):
        index = self.size()
        self.items.append(key)

        while (index != 0):
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p



bheap = BinaryHeap()

print('Menu')
print('insert<data>')
print('max get')
print('max extract')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'max':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(bheap.get_max()))
        elif suboperation == 'extract':
            print('Maximum valiue removed: {}'.format(bheap.extract_max()))


    elif operation == 'quit':
        break
