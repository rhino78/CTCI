from LinkedList import *


def deleteDups(linkedlist):
    if linkedlist.head is not None:
        currNode = linkedlist.head

        dic = {currNode.value: True}
        while currNode.next != None:

            if currNode.next.value in dic:
                print("removing: {}".format(currNode.value))
                currNode.next = currNode.next.next
            else:
                dic[currNode.next.value] = True
                currNode = currNode.next


# -----test-----
L = randomLinkedList(9, 3, 7)
print(L)
deleteDups(L)
print(L)
