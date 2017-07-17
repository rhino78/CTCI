#2.2 return kth to last element in a list
 # implement an algorithm to find the kth to last element of a singly linked list


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


def getKthNode(head, k):
	curr = head
	while(k > 0 and curr is not null):
		curr = curr.next
		k = k -1
	return curr
