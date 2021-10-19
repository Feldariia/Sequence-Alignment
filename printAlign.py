import calc as c


# Outputting the sequence alignments
def print_alignment(g, h, align_arg):
    # Print a slash for any item that does not match within the sequence
    print("".join(
        "/" if a is None else g[a] for a, _ in align_arg
    ))

    print("".join(
        "/" if b is None else h[b] for _, b in align_arg
    ))
