# Palindrome
# implement a function to determine if a linked list is a palindrome


from robustLinkedList import LinkedList

def ispalindrome(L1):
    k = len(L1)
    pointer = L1.head
    pali_check = []
    while pointer is not None:
        pali_check.append(pointer.value)
        pointer = pointer.next
    pali_check.reverse()

    pointer = L1.head

    for t in range(k):
        if pointer.value != pali_check[t]:
            return False
        pointer = pointer.next

    return True


# -----test-----
L1 = LinkedList([1, 2, 3, 4, 3, 2, 1])
L2 = LinkedList([1, 2, 3, 4, 5, 6, 7])
print(ispalindrome(L1))
print(ispalindrome(L2))
