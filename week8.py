Session 1 standard set version 1

###Problem 1

#Understand
I: Given a TreeNode("Trunk") root, build a binary tree using the apple variety diagram
O: A binary tree with all nodes correctly connected
C:
E: None

#Plan
Create all nodes from bottom to top
Connect children to parents accordingly
Return the completed root

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

fuji = TreeNode("Fuji")
opal = TreeNode("Opal")
crab = TreeNode("Crab")
gala = TreeNode("Gala")

mcintosh = TreeNode("Mcintosh", fuji, opal)
granny = TreeNode("Granny Smith", crab, gala)

root = TreeNode("Trunk", mcintosh, granny)





###Problem 2

#Understand
I: Root node of a tree where the root is an operator and both children are integers
O: The result of applying the operator to the children
C: 
E: None

#Plan
Check the operator in the root
Perform the corresponding operation
Return the computed result

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if root.val == "+":
        return root.left.val + root.right.val
    elif root.val == "-":
        return root.left.val - root.right.val
    elif root.val == "*":
        return root.left.val * root.right.val
    elif root.val == "/":
        return root.left.val / root.right.val

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree))







###Problem 3

#Understand
I: Root of a binary tree representing a plant
O: List of node values along the rightmost path
C: 
E: If no right child, return only root value

#Plan
Start at root and keep traversing right until None
Append each node's value to a list
Return the list

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    result = []
    current = root
    while current:
        result.append(current.val)
        current = current.right
    return result

ivy1 = TreeNode("Root",
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))








Session 2 standard set version 1

###Problem 1

#Understand
I: Root of a binary tree where each node value represents the number of splits in a Monstera leaf
O: Count of leaves that have an odd number of splits
C: 
E: Empty tree should return 0

#Plan
If the tree is empty, return 0
Use recursion to visit each node
Count 1 if node value is odd
Add counts from left and right subtrees

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_odd_splits(root):
    if not root:
        return 0
    count = 1 if root.val % 2 != 0 else 0
    count += count_odd_splits(root.left)
    count += count_odd_splits(root.right)
    return count


monstera = TreeNode(2,
                    TreeNode(3, TreeNode(6), TreeNode(7)),
                    TreeNode(5, None, TreeNode(12)))

print(count_odd_splits(monstera))
print(count_odd_splits(None))





###Problem 2

#Understand
I: Root of a BST where each node value is a flower name (string), and a target name
O: Boolean True/False if the flower is found in the BST
C: 
E: Empty tree should return False

#Plan
If tree is empty, return False
If target equals root value, return True
If target < root value, search left
Else search right

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(inventory, name):
    if not inventory:
        return False
    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)

# Example
garden = TreeNode("Rose",
                  TreeNode("Lily",
                           TreeNode("Daisy"),
                           TreeNode("Lilac")),
                  TreeNode("Tulip", None, TreeNode("Violet")))

print(find_flower(garden, "Lilac"))
print(find_flower(garden, "Sunflower"))






###Problem 4

#Understand
I: Root of a BST (collection) and a new plant name (string)
O: Updated BST with the new plant inserted in correct position
C: 
E: If tree is empty, return new node as root; if duplicate, insert in right subtree

#Plan
If the tree is empty, return a new TreeNode(name)
If name < current node value, go left
Else go right
If there is no child in that direction, insert the new node there
Return the original root

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    
    if name < collection.val:
        if collection.left:
            add_plant(collection.left, name)
        else:
            collection.left = TreeNode(name)
    else:
        if collection.right:
            add_plant(collection.right, name)
        else:
            collection.right = TreeNode(name)
    
    return collection