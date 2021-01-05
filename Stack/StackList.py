class Stack:

  def __init__(self):
    self.data = []

  def __repr__(self):
    return(str(self.data))

  def push(self, value):
    self.data.append(value)

  def pop(self):
    if len(self.data) == 0:
      return None
    else:
      return self.data.pop()

  def peek(self):
    if len(self.data) == 0:
      return None
    return self.data[len(self.data) - 1]

  def isEmpty(self):
    return self.data == []
