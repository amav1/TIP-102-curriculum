

Session 1 advanced set version 1
###Problem 2
I chose this specific set because a lot of students tend to select the advanced set, since it challenges them more.

#Understand
What algorithm should we employ to increment / decrement the tigger variable based on the specific keywords?

How can we iterate through the list of strings to access the operations?

#Plan
We want to start with initializing tigger to 1 and increment based on the specific operations

Then we want to iterate through the list of strings, for key in operations, and return the final value of tigger after performing the operations

We have to increment or decrement tigger based on the operation 

#Implement

def final_value_after_operations(operations):
    tigger = 1
    for key in operations:
        if key in ("bouncy", "flouncy"): 
            tigger += 1
        elif key in ("trouncy", "pouncy"):
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))



##Problem 3
I chose this problem because I wanted to showcase an example using iteration through strings rather than lists or arrays.

#Understand
How can we scan through every character in a string?

How can we figure out what characters are left after removing the specified substrings? And how do we store it?

#Plan
We have to start by iterating through the string... for char in word .. 
if char does not equal whitespace (which could be an edgecase) then return a new string where the specified substrings are removed


#Implement


def tiggerfy(word):
    word = word.lower()
    for char in ["t", "i", "gg", "er"]:
        word = word.replace(char, "")
    return word


###Problem 4 Non-decreasing Array
I chose this problem because it could be a little complicated for students so I would like to hone in on that.

#Understand
How can we define a function to check the condition that a number could become decreasing by modifying one element?

How do we represent a number that could be defined as decreasing in code? 


#Plan
If i < i + 1 in the array then it is considered non-decreasing, we have to ensure that i throughout the array is < i + 1 to be considered non-decreasing

For each call, we have to monitor if a number in the array changes because it could potentially change the outcome....
we have to check that as we are incrementing, if i > n - 2 then it shifted the array to become decreasing

returns a boolean value after function call checks for non-decreasing or decreasing set
#Implement


def non_decreasing(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if count == 1:
                return False
            count += 1
            if i > 0 and nums[i - 1] > nums[i + 1]:
                nums[i + 1] = nums[i]
            else:
                nums[i] = nums[i + 1]
    return True

    


Session 2 standard set version 1

##Problem 8
This problem is not too challenging, but it gets students acquainted with lists and appending things to them.

#Understand
How do we compare lists to see if they have elements in common?

How do we rewrite list1 and list2 to omit the common elements?

#Plan

We want to have conditionals that iterate through each list concurrently and identify the values in common...

if element in list1 and list2 then remove that from both lists and return one list combining the two

#Implement

def exclusive_elements(lst1, lst2):
    newlst = []
    
    for element in lst1:
        if element not in lst2:
            newlst.append(element)
    
    for element in lst2:
        if element not in lst1:
            newlst.append(element)
    
    return newlst


##Problem 9
I chose this one because its a little more bulky in material and covers some good concepts.

#Understand
How do we go about merging the strings in alternating order?

What condition should we set in case a string is longer than the other?


#Plan

We need to start with the first char in word1 and then the first char in word2 
and continue that way, appending the chars to a new word variable in that order

if range(len(word1)) != range(len(word2)) then we append the extra chars to the end of the new word
we can easily take the max of the length of both strings to know how many chars we need to go through

#Implement

def merge_alternately(word1, word2):
    merged = []
    max_len = max(len(word1), len(word2))
    
    for i in range(max_len):
        if i < len(word1):
            merged.append(word1[i])
        if i < len(word2):
            merged.append(word2[i])
    
    return ''.join(merged)


##Problem 10
I chose this problem because it introduces students to using nested loops and that's also something very important in coding.

#Understand
How could we represent what a "good pair" is in code?

How can we check pile1 and pile2 simultaneously?


#Plan

we have to first scan through pile1 and pile2 at the same time and then set conditional statements 
after defining a good pair to be pile1[i] % (pile2[j] * k) == 0, meaning theres no remainder

we can include continue to ensure that pile2 is not 0, as an edge case

#Implement


def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile2[j] * k == 0:
                continue  
            if pile1[i] % (pile2[j] * k) == 0:
                count += 1
    return count

