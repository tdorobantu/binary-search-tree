# Binary Search Tree Class
# includes insert, contains and remove methods

class BST:
    def __init__(self, value):
        self.value = value
        self.right = None 
        self.left = None

    # Complexity Analysis of all methods
    # Space Complexity O(1)
    # Time Complexity (where n is number of nodes in BST)
    # Average: O(log(n)) 
    # Worst: O(n) - this occurs when tree depth is equal to nr. of nodes 
    

    def insert(self, value):
        currentNode = self
        while currentNode is not None:
            parentNode = currentNode
            if value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        if value < parentNode.value:
            parentNode.left = BST(value)
        else:
            parentNode.right = BST(value)
        return self 

    def contains(self, value):
        currentNode = self
        while True:
            if currentNode is None:
                return False
            elif currentNode.value == value:
                return True
            else:
                currentNode = currentNode.left if value < currentNode.value else currentNode.right
        pass

    def smallest(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def largest(self):
        currentNode =  self
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.value

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode 
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.smallest()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.right is not None:
                        currentNode.value = currentNode.right.smallest()
                        currentNode.right.remove(currentNode.value, currentNode)
                    elif currentNode.left is not None:
                        currentNode.value = currentNode.left.largest()
                        currentNode.left.remove(currentNode.value, currentNode)
                    else:
                        # Assumes that a tree with only the root value CANNOT be deleted
                        break
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self
