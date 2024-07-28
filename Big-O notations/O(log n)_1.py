def log_func(n):
    if n <= 0:
        return
    print(n)
    n = n // 2
    log_func(n)

log_func(15)