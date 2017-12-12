# class Stack:
#      def __init__(self):
#          self.items = []

#      def isEmpty(self):
#          return self.items == []

#      def push(self, item):
#          self.items.append(item)

#      def pop(self):
#          return self.items.pop()

#      def peek(self):
#          return self.items[len(self.items)-1]

#      def size(self):
#          return len(self.items)
from pythonds.basic.stack import Stack


lst = Stack()

lst.push(3)
lst.push(5)
lst.pop()
lst.push("hoi")
lst.pop()

print(lst.peek())

