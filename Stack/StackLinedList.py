class Node:

  def __init__(self, value=None, next=None):
    self.value = value
    self.next  = next

  def __repr__(self):
    return str(self.value)
  

class Stack:

  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def __repr__(self):
    content = []
    runner  = self.top
    while runner:
      content.append(runner)
      runner = runner.next
    return str(content)
  
  def push(self, value):
    to_insert = Node(value=value)
    if self.top:
      to_insert.next = self.top
      self.top = to_insert
      self.length += 1
    else:
      self.top = to_insert
      self.bottom = to_insert
      self.length += 1

  def pop(self):
    if self.top is None:
      return
    if self.top:
      if self.top.next:
        self.top = self.top.next
        self.length -= 1
      else:
        self.top = None
        self.bottom = None
        self.length = 0
        
  def peek(self):
    return self.top

  def isEmpty(self):
    return self.length == 0
