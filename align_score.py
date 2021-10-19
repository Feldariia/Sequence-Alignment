# Scoring an alignment based on sequences
from functools import partial
import alignment as al


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


# Calculating the sequence alignments in accordance to score
def align_calc(d, e):
    return max(
        al.alignments(d, e),
        key=partial(alignment_score, d, e),
    )
