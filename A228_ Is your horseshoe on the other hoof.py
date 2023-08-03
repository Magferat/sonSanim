# https://codeforces.com/problemset/problem/228/A

shoes = [int(i) for i in input().split()]
diffrent = []

for colors in shoes:
    if colors not in diffrent:
        diffrent.append(colors)
print(len(shoes)-len(diffrent))
