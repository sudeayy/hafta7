from pylab import *
import matplotlib.pyplot as plt

x = [2, -3, -1.5, 3]
y = [3, 1, -2.5, -2]
color = ['m', 'g', 'r', 'b']
fig = plt.figure()
ax = fig.add_subplot(111)
scatter(x, y, s=100, marker='o', c=color)
a = [2, 3]
b = [3, -2]
for i in range(len(x)):
    if i < len(x) - 1:
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], 'ro-')
        plt.plot([x[0], x[3]], [y[0], y[3]], 'ro-')

left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)
xpoints = ypoints = ax.get_xlim()
ax.plot(xpoints, ypoints, linestyle='-', color='k', lw=3, scalex=False, scaley=False)
grid()
show()
