n = int(input())
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
# One can prove the following:
# sum_cards == n * (n + 1) // 2
# However, we'll calculate that using the loop.
for i in range(n - 1):
    sum_cards -= int(input())
print(sum_cards)
