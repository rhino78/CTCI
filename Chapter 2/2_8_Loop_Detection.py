# 2.8 Loop Detection
# given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
# DEFINITION:
# circular linked list: A(corrupt) linked list in which a node's next pointer points to an earlier node,
# so as to make a loop in the linked list
# example
# input A-B-C-D-E-C
# output C


from LinkedList import *

def is_circular(n):
    p1 = n
    p2 = n.next
    while p1 is not None:
        if p1 == p2:
            return True
        p1 = p1.next
        p2 = p2.next.next
    return False

# -----test-----
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = c
p1 = a

print(is_circular(a))

