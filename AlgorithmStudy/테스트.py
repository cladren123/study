
tmp = list(map(int, input().split()))
res = [tmp[i:i+3] for i in range(0,16,3)]

print(res)