#!/usr/bin/env python3

class Shoe:
    condition = "New"
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    
    def get_size(self):
        return self._size
    
    def set_size(self,size):
        if (type(size) in (int, float)):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self,brand="brand"):
        print("Your shoe is as good as new!")
       