# https://codeforces.com/problemset/problem/231/A

t = int(input())
submitted = 0
while t>0:
    lines = [int(i) for i in input().split()]
    n = 0
    for one_ in lines:
        if one_ == 1:
            n += 1
    if n >= 2:
        submitted += 1
    t -= 1
print(submitted)

