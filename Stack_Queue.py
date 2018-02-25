#stack implementation

from collections import deque

stack=[3,1,5]
stack.append(6)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(len(stack))

#implementation stack using Class

class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
        return self.stack.append(val)
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0





#implementation of Queue
print('Queue\n')
queue=[5,7,2]
print(queue)
print(queue.pop(0))
print(queue)
queue.append(9)
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)


#using Class
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.insert(0,val)
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.size() == 0


a=Queue()
a.enqueue(5)
a.enqueue(3)
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())