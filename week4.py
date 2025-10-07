Session 2 standard set version 1

###Problem 6

I chose this problem because it's a straightforward application of FIFO principles, demonstrating how a simple list can model a queue structure for processing.

#Understand

I – A list of dictionaries (NFTs)
O – A list of strings (NFT names in processing order)
C – Must follow FIFO order.
E – Empty list returns empty list.

#Plan
Iterate through the input list and extract the name from each dictionary.

#Implement

def process_nft_queue(nft_queue):
    processed_names = []
    for nft in nft_queue:
        processed_names.append(nft["name"])
    return processed_names

# For N NFTs....
# Time Complexity: O(N)

# Space Complexity: O(N)
# Because processed_names list is created to store all N names.


###Problem 7

I chose this problem because it demonstrates how stack logic (or a counter, in this case) can be used to ensure that every opening action ("add") is correctly closed by a subsequent action ("remove").

#Understand

I – A list of strings ("add" or "remove")
O – Boolean (True if balanced, False otherwise)
C – "remove" must correspond to a preceding "add".
E – ["remove", "add"] is False.

#Plan
Use a counter for open "add" actions. Increment on "add", decrement on "remove". If the counter drops below zero, or if it's non-zero at the end, return False.

#Implement

def validate_nft_actions(actions):
    add_count = 0  
    
    for action in actions:
        if action == "add":
            add_count += 1
        elif action == "remove":
            add_count -= 1
        
        if add_count < 0:
            return False
            
    return add_count == 0

# For N actions...
# Time Complexity: O(N)

# Space Complexity: O(1)
# Because only one constant-size variable (add_count) is used


###Problem 8

I chose this problem because it leverages the fact that the input list is sorted to efficiently locate the two boundary values closest to the budget.

#Understand
Since the list is sorted, how can we efficiently locate the two values closest to the budget?
What special case must we consider if the budget is less than or greater than all NFT values?

I – A sorted list of floats (nft_values) and a float (budget)
O – A tuple of two floats: (closest ≤ budget, closest ≥ budget)
C – The input list is sorted.
E – Handle cases where the budget is outside the range of values.

#Plan
Iterate through the sorted list to find where the values switch from being ≤ budget to > budget. This location defines our two target values.
Then, handle the edge cases where the budget is entirely outside the list's range.

#Implement

def find_closest_nft_values(nft_values, budget):
    n = len(nft_values)
    L = -1
    R = n

    for i in range(n):
        if nft_values[i] <= budget:
            L = i
        else:
            R = i
            break

    if L == -1:
        closest_less_or_equal = nft_values[0]
    else:
        closest_less_or_equal = nft_values[L]
        
    if R == n:
        closest_greater_or_equal = nft_values[n - 1]
    else:
        closest_greater_or_equal = nft_values[R]
        
    return (closest_less_or_equal, closest_greater_or_equal)

# For N be the number of values.

# Time Complexity: O(N)
# Because it takes a single pass loop over all N values to find the location relative to the budget

# Space Complexity: O(1)
# Because only a few constant-size variables are used