# Author: Alina Vinogradova

import sys


class Stack:
    def __init__(self):
        self.items = []

    # Push given object on top of the stack
    def push(self, obj):
        self.items.append(obj)

    # Pop an object from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack.")
        return self.items.pop()

    # Returns size of a stack
    def size(self) -> int:
        return len(self.items)

    # Returns object on top of the stack
    def top(self):
        return self.items[-1]

    def is_empty(self) -> bool:
        return self.size() == 0

    def print(self):
        sys.stderr.write("\t--- Stack bottom")
        for i in self.items:
            i.print()
        sys.stderr.write("\tStack top ---")

    def clear(self):
        self.items = []
