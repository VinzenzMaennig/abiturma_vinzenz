import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2,6,0.1)   # start,stop,step
y1 = 0.5*(x-2)**2-2

plt.plot(x,y1, c="black", linewidth=3.0)

# plot axis
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

plt.grid(True)
# plt.xlabel('x-Achse')
# plt.ylabel('y-Achse')
# plt.title('Geschwindigkeit eines Autos')
# plt.legend(['cos(x)'])

plt.show()