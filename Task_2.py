import random

def f(N, a, b):
    values = [random.normalvariate(a, b) for i in range(N)]
    return (b-a)*sum(-values**2+4)/N

n = int(input())
A = int(input())
B = int(input())
print(f(n,A,B))