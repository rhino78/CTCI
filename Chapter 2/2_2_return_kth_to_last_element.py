# 2.2 return kth to last element in a list
# implement an algorithm to find the kth to last element of a singly linked list

from LinkedList import *


def getkthnode(linkedlist, k):
    pointer2 = linkedlist.head
    for i in range(k-1):
        if pointer2.next != None:
            pointer2 = pointer2.next
        else:
            return "k exceeds the length of linked list"

    pointer1 = linkedlist.head

    while pointer2.next != None:
        pointer2 = pointer2.next
        pointer1 = pointer1.next

    return str(pointer1.value)


# -----test-----
L = randomLinkedList(8, 0, 100)
print(L)
print("the 3rd to last element is: " + getkthnode(L, 3))
