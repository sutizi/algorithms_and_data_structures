class Node:
    """
    Node for simple linked list
        -Value: value of element in node
        -Next: a pointer to next node in the sequence, null if node is the last element
    """

    def __init__(self, value):
        self.value = value 
        self.next = None

   def get_value(self):
       return self.value

   def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value
    
    def set_next(self, next_node):
        self.next = next_node
