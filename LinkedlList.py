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
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for i in range(index):
                # Since temp point to the head initially, this we increment temp one by one as how many time the loop is run
                temp = temp.next 
            return temp.value
        
    def set_value (self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index > 0:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        pre= self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after





new_linked_list = LinkedList(10)
new_linked_list.append(3)
new_linked_list.append(5)
new_linked_list.pop()
new_linked_list.prepend(2)
new_linked_list.popFirst()
new_linked_list.print()
print(new_linked_list.get(1)) 