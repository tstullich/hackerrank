# Test file
import sys

sys.stdin.readline()
width = sys.stdin.readline().split()

for line in sys.stdin.readlines():
    i = int(line[0])
    j = int(line[2])
    lowest = width[i]
    for idx in xrange(i, j + 1):
        if lowest > width[idx]:
            lowest = width[idx]

    print lowest
