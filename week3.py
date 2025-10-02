Session 1 standard set version 1

###Problem 1

I chose problem 1 because it’s a classic use of stacks that helps students practice with opening/closing logic early!

#Understand
How can we keep track of opening tags so we know which closing tag matches?
What data structure lets us “look back” to the most recent tag we opened?

I – One string of tags like ()[]{}
O – Boolean (True if properly formatted, False otherwise)
C – Tags must be closed in the correct order
E – Empty string (valid), unclosed or misordered tags (invalid)

#Plan
Use a stack to track opening tags.
Use a mapping dict from closing → opening.
Iterate through characters: push on open, on closing check stack top, etc.

#Implement

def is_valid_post_format(posts):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in posts:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0

###Problem 2

I chose this because reversing using a stack is a clean demonstration of LIFO behavior.

#Understand
How can we reverse a list using only stack logic?
What should we return if the list is empty?

I – A list of strings (comments)
O – A list of strings in reversed order
C – Must use a stack (no built-in reverse or slicing)
E – Empty list should return empty list

#Plan
Push all items onto stack.
Pop all items into new list to reverse.

#Implement

def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comment)
    reversed_comments = []
    while stack:
        reversed_comments.append(stack.pop())
    return reversed_comments

###Problem 3

I chose this because it mixes string cleanup and the two‑pointer technique in a neat way.

#Understand
Which characters to ignore (spaces, punctuation)?
How to check symmetry by comparing ends inward?

I – A string (post title)
O – Boolean (True if symmetric, False otherwise)
C – Must use two‑pointer method
E – Empty string is valid; case and non-alphanumerics ignored

#Plan
Clean string: remove non-alphanumeric, lowercase.
Use two pointers at ends, move inward comparing.
If any mismatch return False; else True.

#Implement

def is_symmetrical_title(title):
    clean = ''.join(c.lower() for c in title if c.isalnum())
    left, right = 0, len(clean) - 1
    while left < right:
        if clean[left] != clean[right]:
            return False
        left += 1
        right -= 1
    return True



Session 2 standard set version 1

###Problem 4: Festival Booth Navigation

I chose this problem because it's good to reinforce stack fundamentals, especially when it's such an important data structure and could be confusing for some students initially.

#Understand
How does the "back" instruction affect the sequence of visited booths?
Which data structure is suitable for tracking the current sequence of visited booths where the most recent visit is the one to "backtrack" from?

I - A list clues containing integers (booth numbers) and the string "back".
O - A list of integers representing the final sequence of booths visited.
C - The sequence must correctly handle the "back" instruction by removing the last visited booth.
E - The list of clues is empty. An attempt is made to "backtrack" when no booths have been visited yet.

#Plan
A stack (implemented using a Python list) is the ideal data structure. Visiting a booth is a push operation, and "back" is a pop operation.

Initialize an empty list, visited_booths.

Iterate through the clues list.

If a clue is an integer, append it to visited_booths.

If a clue is "back", check if visited_booths is not empty. If it's not empty, remove the last element. If it is empty, ignore the instruction.

Return visited_booths.

#Implement

Python

def booth_navigation(clues):
    visited_booths = []
    
    for clue in clues:
        if isinstance(clue, int):
            visited_booths.append(clue)
        elif clue == "back":
            if visited_booths:
                visited_booths.pop()
                
    return visited_booths

    
###Problem 5: Merge Performance Schedules

I chose this problem because it’s a natural use case for two-pointer merging. This could also be a tricky concept for students.

#Understand
What is the core merging logic?
How are the remaining performances from the longer schedule handled?
How can we use two pointers to manage the alternating access?

I - Two strings, schedule1 and schedule2.
O - A single string representing the merged schedule.
C - Must alternate performances starting with schedule1. Any remainder is appended.
E - One or both schedules are empty strings.

#Plan
Use two index pointers, i and j, initialized to 0, for schedule1 and schedule2.

Initialize an empty list, merged.

Use a while loop that continues as long as i<len(schedule1) or j<len(schedule2).

Inside the loop:

Check if i is within bounds: if so, append schedule1[i] to merged and increment i.

Check if j is within bounds: if so, append schedule2[j] to merged and increment j.

Return the joined string from the merged list.

#Implement

Python

def merge_schedules(schedule1, schedule2):
    merged = []
    i = 0
    j = 0
    
    while i < len(schedule1) or j < len(schedule2):
        
        if i < len(schedule1):
            merged.append(schedule1[i])
            i += 1
            
        if j < len(schedule2):
            merged.append(schedule2[j])
            j += 1
            
    return "".join(merged)


###Problem 6: Next Greater Event

I chose this problem because it introduces map-based indexing and forward searching in arrays. This could be a good example for students to practice using the enumerate function!

#Understand
What defines the "Next Greater Event"?
How do we efficiently find the starting point in schedule2 for the search?

I - Two integer arrays: schedule1 (subset) and schedule2.
O - An array ans with the next greater popularity score for each event in schedule1, or −1.
C - The search in schedule2 must start immediately after the current event's position.
E - schedule1 is empty. No greater event is found.

#Plan

Pre-process schedule2: Create a dictionary, schedule2_map, to store the index of each event's score in schedule2.

Initialize an empty list ans.

Iterate and Search: Loop through each score in schedule1.

Get the starting index in schedule2: start_index = schedule2_map[score].

Search through schedule2 starting from start_index + 1.

The first score found that is greater than the current score is the answer. Append it to ans and break the inner search.

If no greater score is found, append −1 to ans.

Return ans.

#Implement

Python

def next_greater_event(schedule1, schedule2):
    schedule2_map = {score: index for index, score in enumerate(schedule2)}
    
    ans = []
    
    for score in schedule1:
        current_score = score
        start_index = schedule2_map[current_score]
        
        next_greater = -1
        
        for k in range(start_index + 1, len(schedule2)):
            if schedule2[k] > current_score:
                next_greater = schedule2[k]
                break
                
        ans.append(next_greater)
        
    return ans