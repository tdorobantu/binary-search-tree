# OPTIMAL SOLUTION; PASSES ALL TESTS!

# Assume n is the number of nodes in BST
# Time Complexity: O(n)
# Space Complexity: O(n)

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array) # Go Left
        array.append(tree.value) # Add value to array
        inOrderTraverse(tree.right, array) # Go Right
    return array

def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value) # Add value to array
        preOrderTraverse(tree.left, array) # Go Left
        preOrderTraverse(tree.right, array) # Go Right
    return array

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array) # Go Left
        postOrderTraverse(tree.right, array) # Go Right
        array.append(tree.value) # Add value array
    return array


