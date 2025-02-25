# Create a LinkedList

# Class to create Node(value, next):
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Print
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# add to last

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
# pop last one out
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            pre = self.head
            while (temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -=1
            if self.length == 0:
                self.head = None
                self.tail = None
        return temp.value
    
# add to first element
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popFirst(self):
        if new_linked_list.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.tail = None
            new_linked_list.length -= 1
        if new_linked_list == 1:
            self.tail == None
        return temp


new_linked_list = LinkedList(10)
new_linked_list.append(3)
new_linked_list.append(5)
new_linked_list.pop()
new_linked_list.prepend(2)
new_linked_list.popFirst()
new_linked_list.print()
    