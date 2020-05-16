# A course by UCSD, week 1

# Linked Lists

# Each element of a linked list is called a node, and every node has two
# different fields:

# 1. Data - this contains value to be stored
# 2. Next - this contains reference to the next node

# linked lists are used in stacks, queues, graphs(adjacency list)..

# Using dictionary data structure(dict) we represent adjacency list:

graphs = {
   1: [2, 3, None],
   2: [4, None],
   3: [None],
   4: [5, 6, None],
   5: [6, None],
   6: [None]
}
