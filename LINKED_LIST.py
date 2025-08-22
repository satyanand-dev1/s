class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    #Creation from a list
    def create(self,values):
        for value in values:
            self.insert_end(value)
    #insert at Beginnig
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert at a specific position(1-based index)
    def insert_pos(self, pos, data):
        if pos <= 0:
            print("Position should be >= 1")
            return
        if pos == 1:
            self.insert_begin(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
    # Delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
    #Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.text = None
    # Delete at a specific position
    def delete_pos(self, pos):
        if pos <= 0:
            print("Postion should be >= 1")
            return
        if self.head is None:
            print("Lsit is empty")
            return
        if pos == 1:
            self.delete_begin()
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Postion out of range")
                return
            temp = temp.next
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp.next = temp.next.next
    # Traversal
    def traversal(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")

#----------------------------------Main Program--------------------------
sll = SinglyLinkedList()
while True:
     print("\n --- Singly Linked List Operations ---")
     print("1. Create List")
     print("2. Insert at Beginning")
     print("3. Insert at end")
     print("4. Insert at Specific Position")
     print("5. Delete at beginning")
     print("6. Delete at end")
     print("7. Delete at Specific position")
     print("8. Traverse List")
     print("9. Exit")

     try:
        choice = int(input("Enter your choice: "))
     except ValueError:
            print("Please enter a valid integer choice: ")
            continue
     if choice == 1:
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        sll.create(elements)
     elif choice == 2:
        val = int(input("Enter value to insert:  "))
        sll.insert_begin(val)
     elif choice == 3:
        val = int(input("Enter value to insert: "))
        sll.insert_end(val)
     elif choice == 4:
        pos = int(input("Enter position: "))
        val = int(input("Enter value to insert: "))
        sll.insert_pos(pos,val)
     elif choice == 5:
        sll.delete_begin()
     elif choice == 6:
        sll.delete_end()
     elif choice == 7:
        pos = int(input("Enter Position: "))
        sll.delete_pos(pos)
     elif choice == 8:
        sll.traversal()
     elif choice == 9:
        print("Exiting.......")
        break
     else:
        print("Invalid choice! Try again.")
            
