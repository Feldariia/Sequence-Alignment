# Name: Shannon Mong/Michelle Golden
# Summary: Sequence Alignment
# Date: 16 Oct 2021
# Version: 1.0
# Class: SCS341
# Time complexity: O(mn)
from collections import deque
from functools import partial



def all_alignments(x, y):
    """Return an iterable of all alignments of two
    sequences.

    x, y -- Sequences.
    """

    def F(x, y):
        """A helper function that recursively builds the
        alignments.

        x, y -- Sequence indices for the original x and y.
        """
        if len(x) == 0 and len(y) == 0:
            yield deque()

        scenarios = []
        if len(x) > 0 and len(y) > 0:
            scenarios.append((x[0], x[1:], y[0], y[1:]))
        if len(x) > 0:
            scenarios.append((x[0], x[1:], None, y))
        if len(y) > 0:
            scenarios.append((None, x, y[0], y[1:]))

        # NOTE: "xh" and "xt" stand for "x-head" and "x-tail",
        # with "head" being the front of the sequence, and
        # "tail" being the rest of the sequence. Similarly for
        # "yh" and "yt".
        for xh, xt, yh, yt in scenarios:
            for alignment in F(xt, yt):
                alignment.appendleft((xh, yh))
                yield alignment

    alignments = F(range(len(x)), range(len(y)))
    return map(list, alignments)


list(all_alignments("CAT", "CT"))


def print_alignment(x, y, alignment):
    print("".join(
        "-" if i is None else x[i] for i, _ in alignment
    ))
    print("".join(
        "-" if j is None else y[j] for _, j in alignment
    ))


x = "CAT"
y = "CT"
for alignment in all_alignments(x, y):
    print_alignment(x, y, alignment)
    print()


    def alignment_score(x, y, alignment):
        """Score an alignment.

        x, y -- sequences.
        alignment -- an alignment of x and y.
        """
        score_gap = -1
        score_same = +1
        score_different = -1

        score = 0
        for i, j in alignment:
            if (i is None) or (j is None):
                score += score_gap
            elif x[i] == y[j]:
                score += score_same
            elif x[i] != y[j]:
                score += score_different

        return score


    x = "CAT"
    y = "CT"
    alignment = [(0, 0), (1, None), (2, 1)]
    alignment_score(x, y, alignment)


def align_bf(x, y):
    """Align two sequences, maximizing the
    alignment score, using brute force.

    x, y -- sequences.
    """
    return max(
        all_alignments(x, y),
        key=partial(alignment_score, x, y),
    )


align_bf("CAT", "CT")
print_alignment("CAT", "CT", align_bf("CAT", "CT"))
