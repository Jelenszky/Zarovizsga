import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
N=10
y = N*x*np.exp(-x*N)
AT=x*N
plt.plot(AT, y)
#plt.legend(loc="upper right")
plt.title("Kihasználtság időszeletelt ALOHA esetén")
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlim(xmax=10)
plt.xlabel("Bejövő forgalom")
plt.ylabel("Kihasználtság")
plt.show()
