Session 1 standard problem set version 1

###Problem 1

#Understand
I: A list of strings, suits (Tony Stark's suits)
O: An int representing the total count of suits in the list
C: Must not use the len() function
E: An empty list []

#Plan
Initialize count=0, loop through the list, increment count for each element, return count...
We need to do the recursion now...
    Base Case: If the list is empty, return 0
    Recursive Step: Return 1 + the recursive call on the rest of the list (suits[1:])

#Implement
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    
    return 1 + count_suits_recursive(suits[1:])


#Recursive uses the call stack and list slicing, leading to O(N^2) time complexity, and O(N) space for the call stack.


###Problem 2

#Understand
 I: An array of integers, stones 
 O: An integer representing the total sum of the stone powers
 C: Must use a recursive approach
 E: An empty array []

#Plan
 Recursion....
    Base Case: If list is empty, return 0
    Recursive Step: Return the first element (stones[0]) + the recursive call on the rest of the list (stones[1:])

#Implement
def sum_stones(stones):
    if not stones:
        return 0

    return stones[0] + sum_stones(stones[1:])

# Time Complexity: O(N^2)


###Problem 3

#Understand
 I: A list of strings, suits (potentially with duplicates)
 O: An int representing the count of unique suits in the list
 C: Implement both iterative and recursive solutions
 E: A list with all duplicates, a list with no duplicates, an empty list []

#Plan
Iterative: Use set to store unique elements.. iterate through the list, adding elements to the set.... Return the size of the set
Recursive: Use a helper function that passes the list and a 'seen' set.
    Base Case: if list is empty, return the size of the 'seen' set
    Recursive Step: add the first element to the 'seen' set, then call the helper recursively on the rest of the list (suits[1:]) and the updated set

#Implement
def _count_distinct_recursive_helper(suits, seen):
    if not suits:
        return len(seen)
    
    suit = suits[0]
    seen.add(suit)

    return _count_distinct_recursive_helper(suits[1:], seen)

def count_suits_iterative(suits):
    distinct_suits = set()
    
    for suit in suits:
        distinct_suits.add(suit)
    return len(distinct_suits)

def count_suits_recursive(suits):
    
    return _count_distinct_recursive_helper(suits, set())

# Time Complexity:
# Iterative: O(N) (One pass, O(1) set insertion on average)
# Recursive: O(N^2) (Due to list slicing O(N) in each of the N recursive calls)




Session 2 standard problem set version 1



###Problem 1

#Understand
 I: An integer vacation_length and a sorted list of integers cruise_lengths
 O: True if vacation_length is present in cruise_lengths, and False otherwise
 C: Must use binary search (O(log n) time complexity)
 E: Target at start, end, middle, or not present

#Plan
initialize low=0, high=len-1.
loop while low <= high... and calculate mid.
if match, return True.. If cruise_lengths[mid] < target, set low = mid + 1.. Else, set high = mid - 1.
if loop exits, return False

#Implement
def find_cruise_length(cruise_lengths, vacation_length):
    low = 0
    high = len(cruise_lengths) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if cruise_lengths[mid] == vacation_length:
            return True
        
        elif cruise_lengths[mid] < vacation_length:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return False


###Problem 2

#Understand
 I: A sorted list of cabins (deck levels) and an int preferred_deck
 O: The index where preferred_deck is found, OR the index where it would be inserted to maintain sorted order
 C: Has to be a recursive function with O(log n) time complexity
 E: Target found, target smaller than min, target larger than max, target between two values

#Plan
use a recursive binary search to find the lower bound.. (first index >= target)
    Base Case: If low > high, return low (the insertion point)
    Recursive Step:
        if cabins[mid] >= target, the answer is mid or to the left... recurse (low, mid - 1).
        if cabins[mid] < target, the answer must be to the right... recurse (mid + 1, high).

#Implement
def find_cabin_index(cabins, preferred_deck):
    
    def find_cabin_index_recursive(low, high):
        
        if low > high:
            return low
        
        mid = low + (high - low) // 2
        
        if cabins[mid] >= preferred_deck:
            return find_cabin_index_recursive(low, mid - 1)
        else:
            return find_cabin_index_recursive(mid + 1, high)

    return find_cabin_index_recursive(0, len(cabins) - 1)


###Problem 3

#Understand
 I: A sorted list of rooms (0s followed by 1s). 1 means checked-in
 O: The total number of checked-in passengers (total count of 1s)
 C: Must be solved in O(log n) time complexity
 E: List contains only 0s, only 1s, or is empty

#Plan
the count of 1s is N - (index of the first 1)
use Binary Search to find the index of the **first occurrence of 1... (the lower bound of 1)
if the first 1 is found at index i, the result is len(rooms) - i

#Implement
def count_checked_in_passengers(rooms):
    n = len(rooms)
    
    def find_first_one_index(low, high):
       
        if low > high:
            return low
        
        mid = low + (high - low) // 2
        
        if rooms[mid] == 1:
            return find_first_one_index(low, mid - 1)
        else: 
            return find_first_one_index(mid + 1, high)

 
    first_one_index = find_first_one_index(0, n - 1)
    

    return n - first_one_index