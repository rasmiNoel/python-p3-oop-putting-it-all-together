#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="", size=""):
        self.brand = brand
        self.size = size

    def size(self):
        if isinstance(self.size, int):
            return self.size
        else:
            print("size must be an integer.")
            
    def repair(self, condition="New"):
        self.condition = condition