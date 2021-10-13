
import sys

input = sys.stdin.readline


n = input().strip()

stack = []
for i in range(len(n)) :
    print(n[i], end="")
    if (i+1) % 10 == 0 and i != 0 :
        print()

