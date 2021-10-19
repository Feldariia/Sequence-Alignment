import calc as c
import printAlign as p
from collections import deque


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
