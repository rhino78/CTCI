# 2.7 Intersection
# Given two (singly) linked Lists, determine if the two lists intersect.
# Return the intersecting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth  node of the first linked list is the exact same node (by reference)
# as the jth node of the second linked list, then they are intersecting.

from LinkedList import *


def intersectingNode(l1, l2):
    p1 = l1.head
    p2 = l2.head
    while p1 is not None and p2 is not None:
        if p1 == p2:
            return p1
        p1 = p1.next
        p2 = p2.next

# -----tests-----
L1 = LinkedList()
L1.addNode('c')
L1.addNode('c')
L1.addNode('c')
L2 = LinkedList()
L2.addNode('b')
L2.addNode('b')
L2.addNode('b')
L3 = LinkedList()
L3.addNode('a')
L3.addNode('a')
L3.addNode('a')
L3.tail.next = L1.head
L2.tail.next = L1.head
print(L1)
print(L2)
print(L3)
t = intersectingNode(L2, L3)
print(t)
