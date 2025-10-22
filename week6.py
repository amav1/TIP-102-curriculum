Session 1 standard set version 1
I picked these because it's important to understand the concept of cycles and fast/slow pointers & how to implement them.

###Problem 6

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

#Understand
 I: Head of a singly linked list (song_audio) with integer values.
 O: Integer count of critical points (local minima or maxima).
 C: Head and tail are excluded. Requires access to previous and next nodes' values.
 E: List length <= 2 returns 0.

#Plan
initialize count = 0. Handle length <= 2 edge case

use three pointers: prev (head), current (head.next), next_node (head.next.next)

loop while next_node is not None (checking all internal nodes)
check for local minima (P > C and N > C) or local maxima (P < C and N < C)
Advance pointers: prev = current, current = next_node, next_node = next_node.next

then we return count

# Implement
def count_critical_points(song_audio):
    if song_audio is None or song_audio.next is None or song_audio.next.next is None:
        return 0

    count = 0
    
    prev = song_audio
    current = song_audio.next
    next_node = song_audio.next.next

    while next_node:
        P = prev.value
        C = current.value
        N = next_node.value

        is_minima = (P > C) and (N > C)
        is_maxima = (P < C) and (N < C)

        if is_minima or is_maxima:
            count += 1
    
        prev = current
        current = next_node
        next_node = next_node.next
        
    return count

# Time Complexity: O(N) - Single pass through the list
# Space Complexity: O(1) - Constant extra space for pointers and count


###Problem 5

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

#Understand
 I: Head of a linked list (playlist_head) that may contain a cycle.
 O: Integer length of the cycle, or 0 if no cycle exists.
 C: Must use the fast and slow pointer method (Floyd's algorithm).
 E: Empty list or list with no cycle returns 0.

#Plan

initialize slow and fast pointers. Move slow by 1, fast by 2.

if fast reaches None, return 0 (no cycle).

if slow == fast, a cycle exists. Keep curr pointer at the meeting point.

start a counter length = 0... move current by 1, incrementing length until current returns to the meeting point.

return the length

# Implement
def loop_length(playlist_head):
    if playlist_head is None or playlist_head.next is None:
        return 0

    slow = playlist_head
    fast = playlist_head
    has_cycle = False
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return 0

    current = slow  
    length = 0
    
    while True:
        current = current.next
        length += 1
        if current == slow:
            break

    return length

# Time Complexity: O(N) - One pass for detection, one pass for length (N is total nodes).
# Space Complexity: O(1) - Constant extra space for pointers and length.



###Problem 4

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

#Understand
 I: Head of a linked list (playlist_head).
 O: True if a cycle exists, False otherwise.
 C: Must use the two-pointer technique (fast and slow pointers).
 E: Empty list or list with one node returns False.

# Plan
initialize slow and fast pointers at the head.

loop while fast and fast.next are not None.

advance slow by 1, fast by 2.

if slow == fast, return True meaning the cycle detected

if loop completes, return False, meaning end of list reached

# Implement
def on_repeat(playlist_head):
    if playlist_head is None or playlist_head.next is None:
        return False
        
    slow = playlist_head
    fast = playlist_head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False

# Time Complexity: O(N) - The fast pointer covers the list in a single pass.
# Space Complexity: O(1) - Constant extra space for the two pointers.




Session 2 standard set version 1

###Problem 1

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

#Understand
 I: Head of a singly linked list 
 O: Boolean: True if the tail points to the head, False otherwise
 C: Must determine if the specific cycle exists
 E: Empty list or list with one node (no cycle possible)

#Plan
handle edge cases: If the list is empty, return False
traverse the list from the head, keeping track of the head node

use a 'current' pointer to iterate until current.next is None (meaning 'current' is the tail).

once the tail is found, check the condition: If tail.next == head, return True.
otherwise... return False

#Implement
def is_circular(clues):
    if clues is None:
        return False
        
    head = clues 
    current = clues
    
    
    while current.next:
        current = current.next
        
    
    if current.next == head:
        return True
    else:
        return False

# Time Complexity: O(N) - Single pass to find the tail
# Space Complexity: O(1) - Constant extra space for the head and current pointers



###Problem 2

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

#Understand
 I: Head of a linked list (evidence) that may contain a cycle
 O: An array containing all values that are part of *any* cycle, in any order
 C: 
 E: list with no cycle, empty list

#Plan
use fast/slow pointers to find if a cycle exists. If no cycle, return [].

if a cycle exists (slow == fast), reset 'slow' to the head. Advance 'slow' and 'fast' one step at a time until they meet again. This second meeting point is the start of the cycle.
start a new pointer 'collector' at the cycle start. Collect the value, and move collector one step. Stop when 'collector' returns to the cycle start. Store collected values in a list.

return list of collected values

#Implement
def collect_false_evidence(evidence):
    if evidence is None:
        return []

    slow = evidence
    fast = evidence
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if fast is None or fast.next is None:
        return []  

 
    slow = evidence
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
 
    cycle_values = []
    collector = slow
    tail = None
    
    while True:
        cycle_values.append(collector.value)
        tail = collector 
        collector = collector.next
        if collector == slow:
            break
            

    breaker = slow
    while breaker.next != slow:
        breaker = breaker.next
    
    breaker.next = None 

    return cycle_values

# Time Complexity: O(N) - Fast/slow pointers find the cycle in O(N). Finding the start and collecting values is also O(N)
# Space Complexity: O(L) - Where L is the length of the cycle, for storing the values in the array




###Problem 3

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

#Understand
 I: Head of a linked list (suspect_ratings), integer threshold
 O: Head of the partitioned linked list
 C: Nodes with value > threshold must precede nodes with value <= threshold. Relative order within the two partitions is not strict
 E: Empty list, list where all values are > threshold, list where all values are <= threshold

#Plan
create two dummy heads: one for the 'High Priority' list (value > threshold) and one for the 'Low Priority' list (value <= threshold).

traverse original list... For each node:
    - If node.value > threshold, append it to the High Priority list.
    - If node.value <= threshold, append it to the Low Priority list.

after traversal, link the tail of the High Priority list to the head of the Low Priority list.
return the head of the High Priority list (which is high_dummy.next).

#Implement
def partition(suspect_ratings, threshold):
    if suspect_ratings is None:
        return None

  
    high_dummy = Node(0) 
    low_dummy = Node(0)  
    
    high_tail = high_dummy
    low_tail = low_dummy
    
    current = suspect_ratings
    
    while current:
        next_node = current.next 
        current.next = None      
        
        if current.value > threshold:
            high_tail.next = current
            high_tail = high_tail.next
        else: 
            low_tail.next = current
            low_tail = low_tail.next
            
        current = next_node
        
    high_tail.next = low_dummy.next
    
    return high_dummy.next

# Time Complexity: O(N) - Single pass through the list where N is the number of suspects
# Space Complexity: O(1) - Constant extra space used for dummy heads and tail pointers