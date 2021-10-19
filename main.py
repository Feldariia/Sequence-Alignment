# Name: Shannon Mong/Michelle Golden
# Summary: Sequence Alignment (Brute-Force)
# Date: 18 Oct 2021
# Version: 2.0
# Class: SCS341
# Time complexity: O(n!) *Can use Needleman-Wunsch for O(nm), but is not necessary for 6 items of data


# Import packages
# import calc as c
import printAlign as p
import alignment as al
import align_score as alsc

# Ask user for input
inp = str(input("Please insert word to match: "))
print("Starting Sequence Alignment on", inp)

# Collect input
x = inp
# y = inp

# Create data file and append six items to an array
data = open("datafile.txt", "w")
items = ["Watch", "Cat", "Mouse", "Lay", "Sing", "Draw"]
print(items)

# Add matching array for scoring alignments
y = items
match = [(0, 0), (1, None), (2, 1)]

for i in items:
    print(i)
    alsc.alignment_score(x, i, match)

# Append input and print
for y in items:
    for alignment in al.alignments(x, y):
        p.print_alignment(x, y, alignment)
        print()

# Print statements of items and sequence alignments/calculations
# print(alignments)
alsc.align_calc(x, y)
p.print_alignment(x, y, alsc.align_calc(x, y))
