#2025-09956
from lab1_solution import Array

class ArrayQueue:
    def __init__(self, capacity = 10):
        self.array = Array(capacity)
        self.front_index = 0
        self.back_index = 0

    def __repr__(self):
        display = "["
        for index in range(self.array.capacity):
            display += f"{self.array.items[index]}, "
        display += f"] \nSize: {self.size()}, Front: {self.front_index}, Back: {self.back_index}\n" 
        return display
    
    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def enqueue(self, item):
        
        #runs IF next index of back_index in circular array is not Empty. Meaning: If circular array is full 
        if self.array.items[(self.back_index+1)%self.array.capacity] != None:
            placeholder_array = []
            #case 1: normal 
            if self.front_index < self.back_index:
                #copies elements of original array
                for index in range(self.array.capacity):
                    placeholder_array.append(self.array.items[index])
                #appends None to other half of the new circular array

            #wrap-around
            elif self.front_index > self.back_index:
                for index in range(self.array.capacity):
                    placeholder_array.append(self.array.items[(self.front_index+index)%self.array.capacity])
                self.front_index = 0
                self.back_index = self.array.capacity-1

            for empty_index in range(self.array.capacity):
                placeholder_array.append(None)

            #replacing old array
            self.array.items = placeholder_array
            self.array.capacity*=2

        #appending item at back index and updating size and back_index
        self.array.items[self.back_index] = item
        self.back_index = (self.back_index + 1) % self.array.capacity

    #returns size 
    def size(self):
            if self.front_index <= self.back_index:
                return self.back_index - self.front_index
            #front is bigger (wrap around)
            else:
                return self.array.capacity - (self.front_index - self.back_index)
            
    
    def dequeue(self):
        #raises exception
        if self.is_empty() == True:
            raise Exception("Empty Queue: cannot dequeue")
        else:
            #creates and returns placeholder, moves to next array index
            return_item = self.array.items[self.front_index]
            self.array.items[self.front_index] = None
            self.front_index = (self.front_index + 1) % self.array.capacity

            #updates front and back indices when size is 0  
            if self.size() == 0:
                self.front_index = 0
                self.back_index = 0

    def front(self):
        if self.is_empty() == True:
            raise Exception("Empty Queue: no front")
        return self.array.items[self.front_index]