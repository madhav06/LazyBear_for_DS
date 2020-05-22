
# Stack Implementations

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        #return self.items.pop()
        print (self.items.pop())


    def peek(self):
        #returnself.items[len(self.items)-1]
        print (self.items[len(self.items)-1])

    def size(self):
        #return len(self.items)
        print (len(self.items))




s = Stack()

#print(s.isEmpty())

s.push(1)
s.push('two')
s.peek()

s.push(True)
s.size()

print(s.isEmpty())

s.pop()
s.pop()
s.size()

s.pop()
print(s.isEmpty())
