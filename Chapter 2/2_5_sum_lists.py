# 2.5 sum lists
# you have two numbers represented by a linked list, where each node contains  a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# write a function that adds the two numbers and returns the sum as a linked list.
# example:
# (7-1-6) + (5-9-2) that's 617+ 295
# Output 2-1-9 that's 912

from LinkedList import *

def reverseList(LList):
    p = LList.head
    rev_it = []
    while (p != None):
        rev_it.append(p.value)
        p = p.next

    results = LinkedList()

    for i in reversed(rev_it):
        results.addNode(i)

    return results

def addLists(L1, L2):
    p1 = reverseList(L1).head
    p2 = reverseList(L2).head
    ones_place = 0
    tens_place = 0
    linkedlist_sum = LinkedList()
    while (p1 != None) or (p2 != None):
        print(p1.value)
        print(p2.value)
        sum = p1.value + p2.value + tens_place
        print(sum)
        if sum > 9:
            ones_place = int(str(sum)[1:])
            tens_place = int(str(sum)[:1])
            # allow for 2 digit answer in the head
            if p1.next is None:
                linkedlist_sum.addNode(sum)
            else:
                linkedlist_sum.addNode(ones_place)
            print(str(tens_place) + " " + str(ones_place))
        else:
            linkedlist_sum.addNode(sum)
        p1 = p1.next
        p2 = p2.next
    return reverseList(linkedlist_sum)


# -----test-----
L1 = randomLinkedList(3, 0, 9)
L2 = randomLinkedList(3, 0, 9)
print(L1)
print(L2)
t = addLists(L1, L2)
print(t)
