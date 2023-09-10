# QUEUE IMPLEMENTATION

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new = Node(value)
        self.first = new
        self.last = new
        self.length = 1

    def print_q(self):
        temp = self.first

        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new = Node(value)

        if self.length == 0:
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
    
        return temp.value
        
my_queue = Queue(3)
my_queue.enqueue(34)
my_queue.enqueue(12)
my_queue.print_q()
my_queue.dequeue()
my_queue.print_q()
              
