# 2.3 Delete middle node
# Implement an algorithm to delete a node in the middle
# (i.e any node but the first and last node, not necessarily the middle)
# of a singly linked list given only access to that node
# example:
# input: the node c from the linked list a-b-c-d-e-f
# result: nothing is returned, but the new linked list looks like a-b-d-e-f

from LinkedList import *


def deleteNode(linkedlist, node):
    if node.next is not None:
        node.value = node.next.value
        node.next = node.next.next


# -----test-----
L = randomLinkedList(5, 0, 100)
node = L.head.next.next
print(L)
print("deleting node")
deleteNode(L, node)
print(L)