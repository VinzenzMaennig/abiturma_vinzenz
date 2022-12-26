import matplotlib.pyplot as plt
import numpy as np

scaling = 1.5
x = np.arange(-scaling*np.pi,scaling*np.pi,0.1)   # start,stop,step
y1 = np.exp(x)
y2 = np.exp(-x)
y3 = -np.exp(x)

plt.plot(x,y1, c="black", linewidth=3.0)
plt.plot(x,y2, c="red", linewidth=3.0)
plt.plot(x,y3, c="blue", linewidth=3.0)

# plot axis
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

plt.grid(True)
# plt.xlabel('x-Achse')
# plt.ylabel('y-Achse')
plt.title('Spiegeln')
plt.legend(['e(x)', 'e(-x)', '-e(x)'])

plt.show()