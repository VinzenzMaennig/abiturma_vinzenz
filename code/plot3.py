import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4,4,0.05)   # start,stop,step
y1 = ((x**2-1)*(x**2-9))/((x**2-4)*x)

plt.plot(x,y1, c="black", linewidth=3.0)

# plot axis
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

plt.grid(True)
# plt.xlabel('x-Achse')
# plt.ylabel('y-Achse')
# plt.title('Geschwindigkeit eines Autos')
# plt.legend(['cos(x)'])

ax = plt.gca()
ax.set_ylim([-5, 5])

plt.show()