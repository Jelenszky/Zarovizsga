import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
N=20
y = N*x*np.exp(-2*x*N)
AT=x*N
plt.plot(x, y)
#plt.legend(loc="upper right")
plt.title("Kihasználtság  ALOHA esetén")
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlim(xmax=1)
plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1])
plt.xlabel("Érkezési intenzitás")
plt.ylabel("Kihasználtság")
plt.show()
