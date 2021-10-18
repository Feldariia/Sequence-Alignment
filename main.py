# Name: Shannon Mong/Michelle Golden
# Summary: Sequence Alignment
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

    alignments = alignment_recursion(range(len(x)), range(len(y)))
    return map(list, alignments)

    # Push alignments into a list
    list(alignments(x, y))


# Outputting the sequence alignments
def print_alignment(x, y, alignment):
    print("".join(
        "/" if a is None else x[a] for a, _ in alignment
    ))
    print("".join(
        "/" if b is None else y[b] for _, b in alignment
    ))


x = input
y = input
for alignment in alignments(x, y):
    print_alignment(x, y, alignment)
    print()


    # Scoring an alignment based on sequences
    def alignment_score(x, y, match):

        # Score variables
        score_match = +1
        score_nomatch = -1
        gap_penalty = -1

        score = 0
        for a, b in match:
            if (a is None) or (b is None):
                score += gap_penalty
            elif x[a] == y[b]:
                score += score_match
            elif x[a] != y[b]:
                score += score_nomatch

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
align_calc(x, y)
print_alignment(x, y, align_calc(x, y))


