Session 1 standard set version 1
###Problem 1
I chose problem 1 and problem 2 because students tend to get stuck in the beginning problems until they get into the groove of it!

#Understand
How can we use dictionaries to map the artist to their set time?

What can we do to ensure both strings are the same length?

I - Two lists of strings
O - One dictionary mapping artist to their set time
C - Must use a dictionary only
E - Both lists are empty, only one is empty, or the lists are not the same length

#Plan

We must use initialize a dictionary pairings = {} which will then store the values of each paired string in the list to be accessed 

for i in artists, set_times.... then if the len(artist) == len(set_times) then in that order we append it to the dictionary


#Implement

def lineup(artists, set_times):
    pairings = {}
    for i in range(len(artists)):
        if artists[i] is not None and set_times[i] is not None:
            pairings[artists[i]] = set_times[i]
    return pairings




###Problem 2

#Understand
How can we access dictionary values?
What happens when the artist we're searching for does not exist in the dictionary?

I - A string artist + a dictionary 
O - The dictionary schedule for the specific artist
C - 
E - The dictionary is empty, artist is not found, artist is not entered as a string

#Plan

First we need to check if the artist is in festival schedule, and if it's not then return {"message": "Artist not found"}... 
if it is found in the dictionary, then return that schedule

#Implement

def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {"message": "Artist not found"}



###Problem 5
I chose this because it is a little more in depth with dictionaries and students might need more help navigating this.

#Understand
How do we tally the votes for comparison later on?
What do we do in the case that there is a tie?


I - A dictionary marked by the name "votes"
O - Most popular artist(s) by vote
C - 
E - There's a tie

#Plan

We want to first make sure the artist is in the dictionary, and if it is then we add 1 to their vote count to keep track of the scores
returning the max of the vote counts will help us find the highest value to return the artist attached to that 

#Implement

def best_set(votes):
    vote_counts = {}

    for artist in votes.values():
        if artist in vote_counts:
            vote_counts[artist] += 1
        else:
            vote_counts[artist] = 1

    return max(vote_counts, key=vote_counts.get)



Session 2 standard set version 1


###Problem 2
I chose these for the same reason as before... usually students need a little nudge at first. I skipped over question 1 because 
it covered the same topic as session 1

#Understand
How do we make sure that our function is case-sensitive?
How do we compare both strings to ensure that observed_species is also contained in the endangered_species set?


I - Two sets of strings
O - The number of endangered species (in common)
C - 
E - There is nothing in common, empty set

#Plan

We need to establish an endangered_set first.. either by initializing endangered_set = [], or endangered_set = set(endangered_species) which is a faster algorithm
we also need a count for every char that is common between the observed and endangered sets

#Implement

def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)  
    count = 0

    for char in observed_species:
        if char in endangered_set:
            count += 1

    return count




###Problem 3


#Understand
What should we do to return the total time it takes to visit all observed points while retaining the order?
How do we iterate back and forth between the characters in the string?

I - Two strings of different lengths
O - Total time to visit all observed points (an int)
C - Use only enumerate()
E - Empty string(s)

#Plan

we need to use a dictionary that will map each char to their index, then we can say...
for index, char in enumerate(station_layout) so that we can define index and char for the station_layout string
we need to document the total time it takes and we need to establish a current_index variable so we can move through the string (the same way we do with nodes)
if char is in observations.. then we define the next index to be the next char in the string... 
also adding to the total time (calculated by the formula |i - j| or in this case current_idx - next_idx)
now set the current to be the next index so we can keep moving through the string in that way


#Implement

def navigate_research_station(station_layout, observations):
    position_map = {char: idx for idx, char in enumerate(station_layout)}
    
    total_time = 0
    current_index = 0  

    for char in observations:
        next_index = position_map[char]
        total_time += abs(current_index - next_index)
        current_index = next_index  

    return total_time



###Problem 4


#Understand


I - Two sets of strings
O - A sorted set of strings 
C - Use only extend()
E - 

#Plan

first, establish a set to store the finalized list of strings.. priority_set = []
then we need to make sure species is in priority species, where we then use the extend function to add all priority strings to the list first

then we call extend again for the items not in common / not prioritized to add to the end of the list

#Implement

def prioritize_observations(observed_species, priority_species):
    priority_set = []

    for species in priority_species:
        priority_set.extend([s for s in observed_species if s == species])

    non_priority = sorted([s for s in observed_species if s not in priority_species])
    priority_set.extend(non_priority)

    return priority_set
