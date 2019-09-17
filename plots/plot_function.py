"""
using matplotlib.pyplot to plot some basic functions.
jimmy shen

"""
import matplotlib.pyplot as plt
# y=2*x+1
xs = [-10+i for i in range(20)]
ys = [2*x+1 for x in xs]
ys1 = [x**2 for x in xs]
plt.scatter(xs, ys, c='r')
plt.scatter(xs, ys1, c='b')
plt.show()
