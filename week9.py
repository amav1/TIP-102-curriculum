
Session 1 standard set version 1
###Problem 1

#Understand
I: Given two binary trees order1 and order2 where each node represents a cookie quantity, 
   merge trees into one combined order
O: Merged tree where overlapping nodes are summed and non-overlapping nodes are preserved
C: 
E: If one or both input trees are None

#Plan
if order1 is None, return order2... if order2 is None, return order1

create a new node whose value = order1.val + order2.val

recursively merge the left subtrees and assign to merged.left
recursively merge the right subtrees and assign to merged.right
return merged

#Implement
class TreeNode:
    def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    if not order1:
        return order2
    if not order2:
        return order1

    merged = TreeNode(order1.val + order2.val)
    merged.left = merge_orders(order1.left, order2.left)
    merged.right = merge_orders(order1.right, order2.right)
    return merged

Time: O(N) 
Space: O(N (or h to indicate height))



###Problem 2

#Understand
I: Given the root of a binary tree design where each node represents a cream puff flavor,
   return the list of flavors in level order (left → right, level by level)
O: A list containing flavors in level order.
C: 
E: If the root is None, return an empty list

#Plan
if root is None, return []
initialize a queue with the root
while the queue is not empty:
  pop the front node.
  append node.val to the result list
  add left and right children to the queue if they exist
return the result list

#Implement
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order_flavors(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return result

Time complexity : O(N) 
Space complexity : O(N)



###Problem 3

#Understand
I: Given the root of a binary tree where each node represents a cake section,
   find the maximum number of tiers (longest path from root to a leaf)
O: An integer representing the maximum tiers
C: 
E: If the root is None, return 0

#Plan
if root is None, return 0
recursively compute depth of left and right subtrees
return 1 + max(left_depth, right_depth)

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(root):
    if not root:
        return 0
    left_depth = max_tiers(root.left)
    right_depth = max_tiers(root.right)
    return 1 + max(left_depth, right_depth)

Time: O(N)
Space: O(N)






Session 2 standard set version 1

###Problem 1

#Understand
I: Given the root of a binary tree display representing baked goods, 
   determine if the tree is balanced
O: True if balanced, False otherwise
C: The difference in height between left and right subtrees of every node 
   must not exceed 1
E: If the root is None, the tree is considered balanced (True)

#Plan
define helper function that returns the height of a subtree 
   or -1 if it is unbalanced
recursively compute the heights of left and right subtrees
if either subtree is unbalanced (height = -1)
if the absolute difference between heights > 1, return -1 (unbalanced)
otherwise, return 1 + max(left_height, right_height).
the tree is balanced if the helper does not return -1.

#Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
    return check(root) != -1

Time: O(N)
Space: O(N)



###Problem 2

#Understand
I: Given the root of a binary tree orders where each node value represents 
   the number of cookies ordered by a customer, 
   compute the sum of all cookie orders at each tree level (day)
O: A list containing the sum of cookie quantities for each level
C: 
E: If the root is None, return []

#Plan
if root is None, return []
initialize a queue with the root and an empty result list
while the queue is not empty:
   determine the number of nodes in the current level (level_size)
   initialize level_sum = 0
   for each node in the level:
       pop node from queue
       add node.val to level_sum
       enqueue left and right children if they exist
   append level_sum to result
return result list

#Implement
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_cookies_each_day(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_sum = 0

        for _ in range(level_size):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level_sum)

    return result

Time: O(N)
Space: O(N)



###Problem 3

#Understand
I: Given the root of a binary tree chocolates where each node represents 
   the sweetness level of a chocolate, 
   return a list of the absolute differences between the maximum and 
   minimum sweetness levels for each row
O: A list of integers representing differences for each level
C: 
E: If a level has only one node, difference = 0. 
   If root is None, return []

#Plan
if root is None, return []
initialize a queue with the root and an empty result list
while the queue is not empty:
   determine the number of nodes in the current level
   track min_val and max_val for that level
   for each node in that level:
       update min_val and max_val
       enqueue left and right children if they exist
   append abs(max_val - min_val) to result
return result

#Implement
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweetness_difference(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        min_val = float('inf')
        max_val = float('-inf')

        for _ in range(level_size):
            node = q.popleft()
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        diff = abs(max_val - min_val) if level_size > 1 else 0
        result.append(diff)

    return result

Time: O(N)
Space: O(N) 
