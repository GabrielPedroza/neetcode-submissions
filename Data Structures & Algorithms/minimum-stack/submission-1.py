class Node:
    def __init__(self, val, minVal):
        self.val = val
        self.minVal = minVal
        self.prev = None
        self.next = None

class MinStack:

    def __init__(self):
        self.node = None
        
    def push(self, val: int) -> None:
        if not self.node:
            self.node = Node(val, val)
        else:
            new_node = Node(val, min(val, self.getMin()))
            self.node.next = new_node
            new_node.prev = self.node
            self.node = new_node

    def pop(self) -> None:
        self.node = self.node.prev

    def top(self) -> int:
        return self.node.val

    def getMin(self) -> int:
        return self.node.minVal
        
