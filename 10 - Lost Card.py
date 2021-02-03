n = int(input())
s = (n + 1) * n / 2
for i in range(n-1):
    s -= int(input())
print(int(s))
