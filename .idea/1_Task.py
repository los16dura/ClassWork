import random
import matplotlib.pyplot as plt

random.seed(0)
n = 100
plt.subplot(4,1,1)
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
#plt.show()
plt.subplot(4,1,2)
n = 1000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
#plt.show()
plt.subplot(4,1,3)
n = 10000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
#plt.show()
plt.subplot(4,1,4)
n = 100000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
plt.show()
