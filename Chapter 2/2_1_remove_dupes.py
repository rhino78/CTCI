#2.1 remove dupes
# write code to remove duplicates from an unsorted list

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

    def removeDuplicates(self):
    	dupes = set()
    	current = self.head
    	
    	while current:
    		if current.data in dupes:
    			prev.next = current.next
    		else:
    			dupes.add(current.data)
                prev = current
    		current = current.next

    def list_print(self):
    	current = self.head
    	while current:
    		print(current.data)
    		current = current.next