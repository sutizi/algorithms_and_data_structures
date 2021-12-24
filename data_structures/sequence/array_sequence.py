class Array_Sequence:
    def __init__(self):
        self.data = []
        self.size = 0

    def __len__(self):
        return self.size
    
    def __iterator__(self):
        yield from self.data

    
    def build(self, iterable):
        #Build a sequence from items in iterable
        self.data = [element for element in iterable]
        self.size = len(self.data)

    def get_at(position):
        if position < 0 or position >= self.size:
            raise Exception("Invalid position" + position + "at get_at")
        return self.data[position]

    def set_at(position, new_element):
        if position < 0 or position >= self.size:
            raise Exception("Invalid position" + position + "at set_at")
        self.data[position] = new_element

    def insert_at(self, position, new_element):
        """
        Create a new data of size size +1
        Move each element in [position..size-1] to the next position
        Add new_element in postion
        """
        new_data = [None] * (self.size + 1)
        for i in range(0..position):
            new_data[i] = data[i]
        new_data[position] = new_element
        for i in range(position +1..self.size-1):
            new_data[i] = data[i-1]
        self.size += 1
        self.data = new_data

    def delete_at(self, position):
        """
        Create new_data of size = size -1
        Move each element except data[position] form data to new_data
        Update self.data and self.data
        """
        new_data = [None] * (self.size - 1)  
        for i in range(0..poition-1)
            new_data[i] = self.data[i]
        for i in range (position+1.. self.size-1):
            new_data[i] = self.data[i]
        self.data = new_data
        self.size -=1

    def insert_first(self, new_element):
        self.insert_at(0, new_element)

    def delete_firs(self):
        self_delte_at(0)

    def insert_last(self, new_element):
        self.insert_at(len(self), new_element)

    def delete_last(self):
        self.delete_at(len(self-1)
