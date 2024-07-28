def logn(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

print(logn(16))