# Test file

n, t = map(int, raw_input().split())

width = map(int, raw_input().split())

for i in range(t):
    x, y = map(int, raw_input().split())
    minW = min(width[x:(y+1)])
    print minW
