import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,8,0.1)   # start,stop,step
y1 = 4-np.abs(x-4)
y2 = np.ones_like(x) * 2
y3 = np.ones_like(x) * 2.5
y4 = np.ones_like(x) * 1.5

plt.plot(x,y1, c="black", linewidth=3.0)
plt.plot(x,y2, c="red", linewidth=3.0)
plt.plot(x,y3, c="blue", linewidth=3.0)
plt.plot(x,y4, c="green", linewidth=3.0)


# plot axis
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

plt.grid(True)
plt.xlabel('Zeit')
plt.ylabel('Geschwindigkeit')
plt.title('Geschwindigkeit eines Autos')
# plt.legend(['cos(x)'])

plt.show()