import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi,2*np.pi,0.1)   # start,stop,step
y = np.cos(x)

plt.plot(x,y, c="red", linewidth=3.0)

# plot axis
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

plt.grid(True)
# plt.xlabel('x-Achse')
# plt.ylabel('y-Achse')
plt.title('Natürlicher Cosinus')
plt.legend(['cos(x)'])

plt.show()