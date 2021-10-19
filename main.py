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
inp = str(input("Please insert word to match: "))
print("Starting Sequence Alignment on", inp)


# Alignment of two sequences
def alignments(w, z):
    # Recursion method for alignment sequences
    def alignment_recursion(s, t):

        if len(s) == 0 and len(t) == 0:
            yield deque()

        # Appending sequences to search for a match
        sequences = []
        if len(s) > 0 and len(t) > 0:
            sequences.append((s[0], s[1:], t[0], t[1:]))
        if len(s) > 0:
            sequences.append((s[0], s[1:], None, t))
        if len(t) > 0:
            sequences.append((None, s, t[0], t[1:]))

        # Head: Front of Sequence
        # Tail: Back of Sequence
        for head1, tail1, head2, tail2 in sequences:
            for a_elem in alignment_recursion(tail1, tail2):
                a_elem.appendleft((head1, head2))
                yield a_elem

    # Return alignment recursion and append to list
    align_items = alignment_recursion(range(len(w)), range(len(z)))
    return map(list, align_items)


# Outputting the sequence alignments
def print_alignment(g, h, align_arg):
    # Print a slash for any item that does not match within the sequence
    print("".join(
        "/" if a is None else g[a] for a, _ in align_arg
    ))

    print("".join(
        "/" if b is None else h[b] for _, b in align_arg
    ))


# Collect input
x = inp
y = inp

# Append input and print
for alignment in alignments(x, y):
    print_alignment(x, y, alignment)
    print()


    # Scoring an alignment based on sequences
    def alignment_score(x, y, match):

        # Score variables
        score_match = +1
        score_nomatch = -1
        gap_penalty = -1

        # Scoring method for no matches, a match, and a gap penalty of 1.
        score = 0
        for a, b in match:
            if (a is None) or (b is None):
                score += gap_penalty
            elif x[a] == y[b]:
                score += score_match
            elif x[a] != y[b]:
                score += score_nomatch

        return score


    # Create data file and append six items to an array
    data = open("datafile.txt", "w")
    items = ["Watch", "Cat", "Mouse", "Lay", "Sing", "Draw"]
    print(items)

    # Add matching array for scoring alignments
    y = items
    match = [(0, 0), (1, None), (2, 1)]
    alignment_score(x, y, match)


# Calculating the sequence alignments in accordance to score
def align_calc(d, e):
    return max(
        alignments(d, e),
        key=partial(alignment_score, d, e),
    )


# Print statements of items and sequence alignments/calculations

print(alignments)
align_calc(x, y)
print_alignment(x, y, align_calc(x, y))
