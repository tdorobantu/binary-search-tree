from BST import BST
from math import inf

# assume n is the number of nodes in the BST
# Space Complexity: O(1)
# Time Complexity: Worst O(n) | Average O(log(n))

def closestVal(tree, target):
    currentNode = tree
    smallestDiff = inf
    while currentNode is not None:
        nextDiff = min(absDiff(currentNode.value, target), smallestDiff)
        closest =  currentNode.value if nextDiff != smallestDiff else closest
        smallestDiff = nextDiff
        if currentNode.value < target:
            currentNode = currentNode.right
        elif currentNode.value > target:
            currentNode = currentNode.left
        else:
            break
    return closest

def absDiff(val1, val2):
    if (val1 >= 0 and val2 >= 0) or (val1 < 0  and val2 < 0):
        return abs(abs(val1) - abs(val2))
    else:
        return abs(val1 - val2)

# Quick Test
# Building test Tree

tree =  BST(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(5)
tree.insert(13)
tree.insert(22)
tree.insert(1)
tree.insert(14)

print(f"Closest value to target of 12: Expected 13 | Received {closestVal(tree, 12)}")
