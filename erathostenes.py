sieve = []
n = 100
for i in range(2, n + 1):
    prime = True
    for j in sieve:
        if i % j == 0:
            prime = False
            break
    if prime:
        sieve += [i]
print(*sieve, sep=", ")