# Name: Shannon Mong/Michelle Golden
# Summary: Sequence Alignment
# Date: 17 Oct 2021
# Version: 2.0
# Class: SCS341
# Time complexity: O(n!) *Can use Needleman-Wunsch for O(nm), but is not necessary for 6 items of data


#Import packages
from collections import deque
from functools import partial


#Ask user for input
input = str(input("Please insert word to match: "))
print("Starting Sequence Alignment on", input)


# Alignment of two sequences
def alignments(x, y):
    # Recursion method for alignment sequences
    def alignment_recursion(x, y):

        if len(x) == 0 and len(y) == 0:
            yield deque()


        #Appending sequences to search for a match
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

    alignments = alignment_recursion(range(len(x)), range(len(y)))
    return map(list, alignments)

#Push alignments into a list
list(alignments)


# Outputting the sequence alignments
def print_alignment(x, y, alignment):
    print("".join(
        "-" if i is None else x[i] for i, _ in alignment
    ))
    print("".join(
        "-" if j is None else y[j] for _, j in alignment
    ))


x = "CAT"
y = "CT"
for alignment in alignments(x, y):
    print_alignment(x, y, alignment)
    print()

    #Scoring an alignment based on sequences
    def alignment_score(x, y, match):

        #Score variables
        score_same = +1
        score_different = -1
        gap_penalty = -1

        score = 0
        for i, j in match:
            if (i is None) or (j is None):
                score += gap_penalty
            elif x[i] == y[j]:
                score += score_same
            elif x[i] != y[j]:
                score += score_different

        return score



    data = open("datafile.txt", "w")
    items = ["Watch", "Cat", "Mouse", "Lay", "Sing", "Draw"]

    x = items
    y = items
    match = [(0, 0), (1, None), (2, 1)]
    alignment_score(x, y, match)


def align_calc(x, y):
    return max(
        alignments(x, y),
        key=partial(alignment_score, x, y),
    )


print(items)
print(alignments)
align_calc("CAT", "CT")
print_alignment("CAT", "CT", align_calc("CAT", "CT"))

