# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k = map(int, input().split())
l = map(int, input().split())
b = int(input())

tot = sum(l) - l[k]
if 2*b == tot: print("Bon Appetit")
else: print(b - tot / 2)
