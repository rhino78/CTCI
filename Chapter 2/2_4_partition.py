#2.4 partition
# write code to partition a liked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
# if x is contained within the list, the values of x only need to be after the elements less than x (below). 
# The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions
# input 3-5-8-5-10-2-1[partition 5]
# output 3-1-2-10-5-5-8


 class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next



class LinkedList(object):
    def __init__(self, head=None, current=None, count=0):
        self.head = head
        self.current = current
        self.count = count

    def insert(self, data):
      new_node = Node(data)
      new_node.set_next(self.head)
      self.head = new_node

    def size(self):
      current = self.head
      count = 0
      while current:
            count+=1
            current =current.get_next()
      return count

    def removeNode(self, s):
        curr = self.head

        while curr.next is not None:
            if curr.data == s:
                prev.next = curr.next
            prev = curr
            curr = curr.next

    def AddAtStart(self, data):
      new_node = Node(data)
      new_node.next = head.next
      head.next = new_node
      count = count +1

    def AddAtLast(self, data):
      new_node = Node(data)
      current.next = new_node
      count = count +1


    def partition(i):
      templist = set()
      count = 0
      curr = head

      while curr.next is not None:
            if curr.data is not None:
                  templist.add(curr)
                  removeNode(curr.data)

                  if curr.data < i:
                        AddAtStart(curr.data)
                  else:
                        AddAtLast(curr.data)
            count = count +1
            curr = curr.next