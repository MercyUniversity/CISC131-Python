class Node:
    def __init__(self, data):
        # Initialize a Node with data and a pointer to the next node
        self.data = data
        self.next = None  # Set the next pointer to None initially

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head pointer
        self.head = None

    def push(self, new_data):
        # Insert a new node at the beginning of the list
        new_node = Node(new_data)  # Create a new node with the given data
        new_node.next = self.head  # Set the new node's next to the current head
        self.head = new_node  # Move the head pointer to the new node

    def insertAfter(self, prev_node, new_data):
        # Insert a new node after the given previous node
        if prev_node is None:  # Check if the previous node is null
            print("The given previous node must be in LinkedList")
            return
        new_node = Node(new_data)  # Create a new node with the given data
        new_node.next = prev_node.next  # Set the new node's next to the previous node's next
        prev_node.next = new_node  # Update the previous node's next to the new node

    def append(self, new_data):
        # Insert a new node at the end of the list
        new_node = Node(new_data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, make new node the head
            self.head = new_node
            return
        last = self.head  # Start from the head node
        while (last.next):  # Traverse the list to find the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new node

    def printList(self):
        # Print all elements in the linked list
        temp = self.head  # Start from the head
        while (temp):  # Traverse through the list
            print(temp.data, end=" ")  # Print the data in the current node
            temp = temp.next  # Move to the next node

# Create a linked list
llist = LinkedList()

# Add elements to the list
llist.push(10)  # Insert 10 at the beginning
llist.push(20)  # Insert 20 at the beginning
llist.push(30)  # Insert 30 at the beginning

print("Created Linked List: ")
llist.printList()  # Print the current linked list

print()

# Insert 40, after the node with data 20
llist.insertAfter(llist.head.next, 40)  # Insert 40 after the second node (20)

print("Linked List after inserting 40: ")
llist.printList()  # Print the list after insertion

print()

# Append 50 to the end of the list
llist.append(50)  # Add 50 at the end of the list

print("Linked List after appending 50: ")
llist.printList()  # Print the final linked list after appending

print()
