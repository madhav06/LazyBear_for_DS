# How to Use collections.deque
#
# In python, there is specific object in the collections module
# that we can use here linked lists called 'deque'. pronounced as 'deck'.

# Create a linked Lists
from collections import deque
#deque()

#populate it
deque(['a', 'b', 'c'])

llist = deque("abcde")
print(llist)

# adding element: append() or appendleft() adds
llist.append("f")
print(llist)

llist.append("p")
print(llist)

# removing element: pop() or popleft() removes
llist.pop()
print(llist)

llist.appendleft("z")
print(llist)

llist.popleft()
print(llist)
