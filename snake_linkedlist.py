# snake_linkedlist.py
# ---------------------------------------
# Linked List implementation for Snake body

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert new head (snake moves forward)
    def insert_at_beginning(self, x, y):
        new_node = Node(x, y)
        new_node.next = self.head
        self.head = new_node

    # Remove tail (snake moves without eating food)
    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        prev = self.head
        temp = self.head.next
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    # Return list of all snake segment positions
    def get_positions(self):
        positions = []
        temp = self.head
        while temp:
            positions.append((temp.x, temp.y))
            temp = temp.next
        return positions
