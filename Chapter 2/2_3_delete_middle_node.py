#2.3 Delete middle node
 # Implement an algorithm to delete a node in the middle (i.e any node but the first and last node, not necessarily the middle) of a singly linked list given only access to that node
 # example:
 # input: the node c from the linked list a-b-c-d-e-f
 # result: nothing is returned, but the new linked list looks like a-b-d-e-f


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
            print(curr.data)
            if curr.data == s:
                prev.next = curr.next
            prev = curr
            curr = curr.next