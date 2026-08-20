class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def insertAtFirst(head, value):
    newNode = ListNode(value)
    newNode.next = head
    return newNode