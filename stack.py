# Implement a stack that has the following methods:
# 1. push(item), which pushes an element onto the stack
# 2. pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack,
#           then it should throw an error or return null. 
# 3. max(), which returns the maximum value in the stack currently.
# Each method should run in constant time.

class Stack:
  def __init__(self):
    self.stack = []
    self.max = None

  def pop(self):
    if len(self.stack) == 0:
      return None
    removed = self.stack.pop()
    if len(self.stack) == 0:
      self.max = None
    elif removed == self.max:
      self.max = self.stack[0]
      for value in self.stack:
        if value > self.max:
          self.max = value
    return removed

  def push(self, item):
    self.stack.append(item)
    if len(self.stack) == 1 or item > self.max:
      self.max = item

  def get_max(self):
    return self.max
