#ques 1
# Insert an element
arr = [10, 20, 30, 40, 50]

index = int(input("Enter index: "))
value = int(input("Enter value: "))

if 0 <= index <= len(arr):
    arr.insert(index, value)
    print("After insertion:", arr)
else:
    print("Invalid index")

# Delete an element
index = int(input("Enter index to delete: "))

if 0 <= index < len(arr):
    arr.pop(index)
    print("After deletion:", arr)
else:
    print("Invalid index")

# Search an element
target = int(input("Enter value to search: "))

if target in arr:
    print("Found at index:", arr.index(target))
else:
    print("Not found")

#ques 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at specified position (1-based)
    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_head(data)
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete matching node
    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            print("Node deleted")
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Node not found")
            return

        prev.next = temp.next
        print("Node deleted")

    # Forward traversal
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
s = SinglyLinkedList()

while True:
    print("\n1. Insert at Head")
    print("2. Insert at Tail")
    print("3. Insert at Position")
    print("4. Delete Node")
    print("5. Display List")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        s.insert_head(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        s.insert_tail(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        s.insert_position(data, pos)

    elif choice == 4:
        key = int(input("Enter value to delete: "))
        s.delete(key)

    elif choice == 5:
        s.display()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")