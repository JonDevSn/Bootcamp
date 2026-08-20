import code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # Create Nodes
head = Node(10)
second = Node(20)
third = Node(30) 

head.next = second
second.next = third
third.next = None 
def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
        print("None")