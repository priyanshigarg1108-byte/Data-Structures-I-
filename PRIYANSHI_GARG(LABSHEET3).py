#ques1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_tail(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def insert_position(self, data, pos):
        if pos <= 1:
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
        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            print("Deleted:", key)
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        print("Deleted:", key)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


s = SinglyLinkedList()

s.insert_head(20)
s.insert_head(10)
s.insert_tail(40)
s.insert_position(30, 3)

print("Singly Linked List:")
s.display()

s.delete(20)
print("After deletion:")
s.display()

#ques2
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new = Node(data)

        if self.head is None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def delete(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev
        else:
            self.tail = temp.prev

        print("Deleted:", key)

    def forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def backward(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


d = DoublyLinkedList()

d.insert(10)
d.insert(20)
d.insert(30)
d.insert(40)

print("Forward Traversal:")
d.forward()

print("Backward Traversal:")
d.backward()

d.delete(20)

print("After Deletion:")
d.forward()
