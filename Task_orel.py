import random
import numpy as np

#1
def get_percentile(values, bucket_number):
    i = 100/bucket_number
    C = [0.0]
    while i < 100:
        C.append(np.percentile(values, i))
        i += 100/bucket_number
    return C

A = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
n = 4
print(get_percentile(A, n))

#2


def get_percentile_number(value, percentiles):
    m = len(percentiles)
    for i in range(m-1, -1, -1):
        #print(percentiles[i], value)
        if percentiles[i] <= value:
            return i
    return 0

values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles = get_percentile(A, n)
print(percentiles)
print(get_percentile_number(2.5, percentiles))
print(get_percentile_number(5.5, percentiles))
print(get_percentile_number(100, percentiles))

#3

def value_equalization(value, percentiles):
    idx = get_percentile_number(value, percentiles)
    step = 1 / len(percentiles)
    return idx * step
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles = get_percentile(values, 5)
print(percentiles)
print(value_equalization(5.5, percentiles))
