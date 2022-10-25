# Recursion

def sum_recursion(n):
    if n<=0:
        return 0
    return n+sum_recursion(n-1)

print(sum_recursion(6))