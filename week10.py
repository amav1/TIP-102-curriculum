Session 1 standard set version 1

###Problem 1

#Understand
I: Given a graph of airports and undirected edges representing flights
O: An adjacency dictionary named flights
C: Undirected → each connection must appear in both nodes' adjacency lists
E: 

#Plan
Represent each airport as a key in a dictionary
Its value is a list of airports it connects to


Edges:
- JFK <-> LAX
- JFK <-> DFW
- DFW <-> ATL



#Implement
flights = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["JFK", "ATL"],
    "ATL": ["DFW"]
}


###Problem 2

#Understand
I: Given adjacency list flights.. flights[i] is a list of destinations reachable from i  
O: Return True if every flight i -> j also has a return flight j 
C: 
E: Empty lists are fine

#Plan
Loop through each node i
For each neighbor j in flights[i], check if i is in flights[j]
If any are missing, return False
Otherwise return True

#Implement
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


###Problem 3

#Understand
I: Given adjacency matrix flights.. flights[i][j] = 1 means flight i->j exists.  
O: Return list of all destinations reachable directly from source  
C: 
E: If none reachable, return empty list.

#Plan
Check the row flights[source]
For each index j where value is 1, append j to result
Return result

#Implement
def get_direct_flights(flights, source):
    result = []
    for j in range(len(flights[source])):
        if flights[source][j] == 1:
            result.append(j)
    return result






Session 2 standard set version 1

###Problem 1

#Understand
I: Given adjacency matrix flights where flights[i][j] = 1 means a flight exists i -> j
O: True if a path exists, otherwise False
C: Use BFS 
E: 

#Plan
Use BFS starting from source
Use a queue and visited set
Pop from queue, check if equals dest
Otherwise add all neighbors where flights[u][v] == 1 and v not visited
If queue empties, return False

#Implement
from collections import deque

def can_rebook(flights, source, dest):
    if source == dest:
        return True

    n = len(flights)
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        curr = queue.popleft()
        for nxt in range(n):
            if flights[curr][nxt] == 1 and nxt not in visited:
                if nxt == dest:
                    return True
                visited.add(nxt)
                queue.append(nxt)

    return False


###Problem 2

#Understand
I: Same task as Problem 1 
O: Return True if any path exists, False otherwise
C: Use recursion or stack-based DFS
E: If source == dest then True

#Plan
Implement DFS:
If curr == dest → True
Mark visited
For each neighbor where flights[curr][nxt] == 1, DFS into nxt
If any returns True → return True
Otherwise return False

#Implement
def can_rebook(flights, source, dest):
    if source == dest:
        return True

    n = len(flights)
    visited = set()

    def dfs(node):
        if node == dest:
            return True
        visited.add(node)

        for nxt in range(n):
            if flights[node][nxt] == 1 and nxt not in visited:
                if dfs(nxt):
                    return True
        return False

    return dfs(source)


###Problem 3

#Understand
I: Given adjacency matrix flights and start i and destination j
O: Number of edges in shortest path; if none exists -> -1
C: Use BFS because BFS finds the shortest path in unweighted graphs
E: If i == j then 0 flights needed

#Plan
If i == j return 0
Use BFS (queue holds (node, distance))
Visited set prevents cycles
For each neighbor where flights[node][nxt] == 1, enqueue with distance+1
If reach j, return distance
If BFS ends without reaching j -> return -1

#Implement
from collections import deque

def counting_flights(flights, i, j):
    if i == j:
        return 0

    n = len(flights)
    visited = set([i])
    queue = deque([(i, 0)]) 

    while queue:
        curr, dist = queue.popleft()
        for nxt in range(n):
            if flights[curr][nxt] == 1 and nxt not in visited:
                if nxt == j:
                    return dist + 1
                visited.add(nxt)
                queue.append((nxt, dist + 1))
    return -1
