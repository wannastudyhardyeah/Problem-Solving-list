n = 1260
count = 0

coins = [500, 100, 50, 10]
print(f"count: {count}, n: {n}")
for coin in coins:
    count += n // coin
    n %= coin
    print(f"count: {count}, n: {n}")

'''
==> 
    count: 0, n: 1260
    count: 2, n: 260
    count: 4, n: 60
    count: 5, n: 10
    count: 6, n: 0
'''