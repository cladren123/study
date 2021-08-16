import sys

input = sys.stdin.readline



str2 = input().strip()
str1 = list(str2)

n = len(str1)

print(str1)
print(n)

start = 0
end = 0

flag = 0

for i in range(n) :
    if str1[i] == '<' :
        flag = 1
    if str1[i] == '>' :
        flag = 0

    if flag == 1 :
        continue


    if str1[i] == " " :
        end = i-1
        one = str1[start:end:-1]
        start = i+1

print(str1)











