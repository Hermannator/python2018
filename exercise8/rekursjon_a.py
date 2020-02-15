def recursive_sum(n):
    if n==0:
        return 0
    return n + recursive_sum(n-1)
print(recursive_sum(53))