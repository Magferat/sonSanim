# https://codeforces.com/problemset/problem/236/A
name = input()
unique = ''
for ch in name:
    if ch not in unique:
        unique += ch
if len(unique)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
