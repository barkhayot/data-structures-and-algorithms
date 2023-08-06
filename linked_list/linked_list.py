

# NODE CONSTRUCTOR ##
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LINKED LIST IMPLEMENTATION
class LinkedList:

    # initializing the structure of the Linked List
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # custom printing all values of the Linked List
    def print_list(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # append new node   
    def append_new_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

        return True

    # pop last node
    def pop_last_node(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next

        # setting node after removing last node
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        # checking after removing node in case we had one node only
        if self.length == 0:
            self.head = None
            self.tail = None


        return temp.value

    # append new node to head of list
    def prepend_new_node(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        
        return True

    # pop first node    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1


        if self.length == 0:
            self.tail = None
        return temp

    # finding node by index of linked list
    def get(self, index):
        # check if passed index is valid for linked list
        if index < 0 or index >= self.length:
            return None
        
        # getting new variable as a temp for looping through LL
        temp = self.head

        # we need to us (underscore while we are not using avriable during process)
        for _ in range(index):
            temp = temp.next
        return temp

        # return temp.value for value of node

    # change value of the node
    def set_value(self, index, value):
        
        # using get method to get node by index and change value if node exists  
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # insert new node
    def insert(self, index, value):
        
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend_new_node(value)
        if index == self.length:
            return self.append_new_node(value)
        
        node = Node(value)
        temp = self.get(index - 1)
        node.next = temp.next
        temp.next = node 
        self.length += 1
        return True

    # remove node    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last_node()
        
        prev = self.get(index - 1)
        # next_node = self.get(index + 1)
        # temp.next = next_node
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # change all node HEAD -> TAIL
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
        


# TESTING FUNCTIONS
my_linked_list = LinkedList(3)

my_linked_list.prepend_new_node(2)
my_linked_list.prepend_new_node(1)

my_linked_list.pop_last_node()
print(my_linked_list.get(0))
my_linked_list.insert(1, 4)
my_linked_list.reverse()
my_linked_list.print_list()
