

# NODE CONSTRUCTOR ##
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # initializing the structure of the Linked List
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # append new node
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
    
    # pop last node
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        # checking if we have one node only
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1

        return temp
    
    # append new node to the head of list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

        return True
    
    # pop first node in list
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    # get node by it's passed index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # if index is on right half part of list or lift half part of list
        # method helps to iterrate faster by reducing time complextity
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp= temp.prev
        return temp
    
    # set node value by finding it's index and change it's value
    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False
    
    # insert node to specific index by it's value
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        before = self.get(index-1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    # remove node and it's value by given index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        before = self.get(index-1)
        temp = before.next

        before.next = temp.next
        temp.next.prev = before

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


        

        



        
        




my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.pop_first()
my_doubly_linked_list.remove(2)

#print(my_doubly_linked_list.print_list())

# my_doubly_linked_list.pop()
print(my_doubly_linked_list.print_list())
