# 2.4 partition
# write code to partition a liked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# if x is contained within the list, the values of x only need to be after the elements less than x (below). 
# The partition element x can appear anywhere in the "right partition";
# it does not need to appear between the left and right partitions
# input 3-5-8-5-10-2-1[partition 5]
# output 3-1-2-10-5-5-8


from LinkedList import *


def partition(linkedlist, x):
    if linkedlist.head is not None:
        p1 = linkedlist.head
        p2 = linkedlist.head.next
        while p2 is not None:
            print('evaluating {}'.format(p2.value))
            if p2.value < x:
                print('moving {} to the front'.format(p2.value))
                p1.next = p2.next
                p2.next = linkedlist.head
                linkedlist.head = p2
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next


# -----test-----
L = randomLinkedList(10, 0, 50)
x = 25
print(L)
partition(L, x)
print(L)

