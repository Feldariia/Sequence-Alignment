# Name: Shannon Mong/Michelle Golden
# Summary: Sequence Alignment (Brute-Force)
# Date: 18 Oct 2021
# Version: 2.0
# Class: SCS341
# Time complexity: O(n!) *Can use Needleman-Wunsch for O(nm), but is not necessary for 6 items of data


# Import packages
from collections import deque
from functools import partial

# Ask user for input
input = str(input("Please insert word to match: "))
print("Starting Sequence Alignment on", input)


# Alignment of two sequences
def alignments(x, y):
    # Recursion method for alignment sequences
    def alignment_recursion(x, y):

        if len(x) == 0 and len(y) == 0:
            yield deque()

        # Appending sequences to search for a match
        sequences = []
        if len(x) > 0 and len(y) > 0:
            sequences.append((x[0], x[1:], y[0], y[1:]))
        if len(x) > 0:
            sequences.append((x[0], x[1:], None, y))
        if len(y) > 0:
            sequences.append((None, x, y[0], y[1:]))

        # Head: Front of Sequence
        # Tail: Back of Sequence
        for head1, tail1, head2, tail2 in sequences:
            for alignment in alignment_recursion(tail1, tail2):
                alignment.appendleft((head1, head2))
                yield alignment


    #Return alignment recursion and append to list
    alignments = alignment_recursion(range(len(x)), range(len(y)))
    return map(list, alignments)




# Outputting the sequence alignments
def print_alignment(x, y, alignment):
    #Print a slash for any item that does not match within the sequence
    print("".join(
        "/" if a is None else x[a] for a, _ in alignment
    ))
    
    print("".join(
        "/" if b is None else y[b] for _, b in alignment
    ))


#Collect input
x = input
y = input

#Append input and print
for alignment in alignments(x, y):
    print_alignment(x, y, alignment)
    print()


    # Scoring an alignment based on sequences
    def alignment_score(x, y, match):

        # Score variables
        score_match = +1
        score_nomatch = -1
        gap_penalty = -1

        #Scoring method for no matches, a match, and a gap penalty of 1.
        score = 0
        for a, b in match:
            if (a is None) or (b is None):
                score += gap_penalty
            elif x[a] == y[b]:
                score += score_match
            elif x[a] != y[b]:
                score += score_nomatch

        return score


    #Create data file and append six items to an array
    data = open("datafile.txt", "w")
    items = ["Watch", "Cat", "Mouse", "Lay", "Sing", "Draw"]


    #Add matching array for scoring alignments
    y = items
    match = [(0, 0), (1, None), (2, 1)]
    alignment_score(x, y, match)


#Calculating the sequence alignments in accordance to score
def align_calc(x, y):
    return max(
        alignments(x, y),
        key=partial(alignment_score, x, y),
    )


#Print statements of items and sequence alignments/calculations
print(items)
print(alignments)
align_calc(x, y)
print_alignment(x, y, align_calc(x, y))

