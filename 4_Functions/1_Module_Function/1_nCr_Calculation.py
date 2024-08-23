n = int(input())
r = int(input())
"""
n_fact = 1
for i in range(1, n + 1):
    n_fact *= i

r_fact = 1
for i in range(1, r + 1):
    r_fact *= i

n_r_fact = 1
for i in range(1, n - r + 1):
    n_r_fact *= i
"""


def fact(n):
    n_fact = 1
    for i in range(1, n + 1):
        n_fact *= i
    return n_fact


n_fact = fact(n)
r_fact = fact(r)
n_r_fact = fact(n - r)
total_ways = n_fact / (r_fact * n_r_fact)
print(total_ways)


# Avoind Repetation
# Readibility Increased
# Testing Become Easier
