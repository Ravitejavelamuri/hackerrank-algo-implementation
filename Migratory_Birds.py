import sys

n = int(input().strip())
t = list(map(int, input().strip().split(' ')))
m = 0
v = 0
for i in range(1,6):
    t1 = t.count(i)
    if t1 > m:
        v = i
        m = t1
print(v)
