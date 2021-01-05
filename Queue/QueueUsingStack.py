class Stack:

  def __init__(self):
    self.data = []

  def __repr__(self):
    return(str(self.data))

  def push(self, value):
    self.data.append(value)

  def pop(self, index=None): # 'index' for QueueUsingStack usage
    if len(self.data) == 0:
      return None
    elif index is None:
      index = len(self.data) - 1
    return self.data.pop(index)

  def peek(self):
    if len(self.data) == 0:
      return None
    return self.data[len(self.data) - 1]

  def isEmpty(self):
    return self.data == []



class QueueUsingStack:

  def __init__(self):
    self.internal_stack = Stack()

  def __repr__(self):
    return(str(self.internal_stack))

  def enqueue(self, value=None):
    self.internal_stack.push(value)

  def dequeue(self):
    self.internal_stack.pop(0)
