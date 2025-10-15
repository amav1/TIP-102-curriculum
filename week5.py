Session 1 standard set version 1
###Problem 10
I chose this example is key to understanding the ways in implementing linked lists

#Understand
Why do we need to define a Node class?

#Plan

We need to change the order of the given function and insert a node between tom_nook and tommy
tom_nook -> timmy -> tommy should be the desired output


#Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tom_nook = Node("Tom Nook")
timmy = Node("Timmy")
tommy = Node("Tommy") 
tom_nook.next = timmy
timmy.next = tommy 

print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)



###Problem 11
I chose this because it's important to understand how to implement linked lists, especially key components like defining the nodes themselves.


#Understand
How do we define nodes?
Are there other ways to go about implementing a linked list?

#Plan

We have to remove one of the nodes from the previous question, append a new node to the end, and change the order again
___. = Node("") then ___.next = ___



#Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

timmy = Node("Timmy")
tommy = Node("Tommy") 
saharah = Node("Saharah")
timmy.next = tommy 
tommy.next = saharah


print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 



###Problem 12
I chose this problem because Linked Lists are very important data structures to cover, and I wanted to ensure that I could explain it 
in the best way to students, since originally I learned how to implement linked lists using the C language

#Understand
How do we traverse a linked list algorithm?
What can we do to store the node values and then convert them into a string?

I - Head that points to the leading node in a list
O - String that links together the values of each node
C - 
E - Empty list, duplicate nodes

#Plan

For a traversal algorithm, we need to start with defining the current node, which is the start of the linked list, and setting that equal to the 
head variable which is the head of the list... head pointer points to first item

Then while there's still a current value, we have to append each value during traversal to the list

Current needs to be updated constantly so that we can make our way to the end of the list 

In the end, we need to return the values in string form 
(e.g.  Isabelle -> Saharah -> C.J.)


#Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(head):
    lst = []
    current = head
    while(current):
        lst.append(current.value)
        current = current.next
        return "->".join(lst)
        




Session 2 standard set version 1


###Problem 8
I chose this question because anything with linked lists is important, and knowing how to move around nodes is key as well

#Understand

I - head of a singly linked list
O - new head of the list with the tail moved to the front
C - must handle lists of any length
E - empty list → None, single node → no change

#Plan

If list is empty or has one node, return head

Traverse to find second-to-last and last node

Detach tail from the end

Point tail's next to the old head

Return tail as new head

#Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def tail_to_head(head):
    if head is None or head.next is None:
        return head

    prev = None
    current = head
    while current.next:
        prev = current
        current = current.next

    prev.next = None
    current.next = head
    return current


###Problem 9
I chose this because doubly-linked lists are just as important to cover as regular linked lists, and people might overthink a lot in the
implementation stage

#Understand

I - node values to link in a doubly linked list
O - linked list where each node has next and prev pointers
C - must connect nodes in both directions
E - empty list → no nodes, single node → next and prev are None

#Plan

Add a prev attribute to Node constructor

Create two nodes (head and tail)

Link head.next to tail and tail.prev to head

Print both directions to confirm links

#Implement

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)


###Problem 10

#Understand

I - tail of a doubly linked list
O - print node values in reverse order separated by spaces
C - must traverse backward using prev pointer
E - empty list → print nothing, single node → print value

#Plan

Start at tail

Print current node's value

Move backward using prev

Stop when current is None

#Implement

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail):
    current = tail
    while current:
        print(current.value, end=" " if current.prev else "\n")
        current = current.prev

