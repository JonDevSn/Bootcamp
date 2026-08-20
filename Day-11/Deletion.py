def deleteValue(head, value):
    if head is None:
        return None

    # If first node has the value
    if head.val == value:
        return head.next

    curr = head

    while curr.next is not None:
        if curr.next.val == value:
            curr.next = curr.next.next
            return head

        curr = curr.next

    return head