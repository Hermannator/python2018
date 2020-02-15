def fakultet(n):
    if n==0:
        return 1
    return n*fakultet(n-1)
print(fakultet(5))