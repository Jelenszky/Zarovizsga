import matplotlib.pyplot as plt
import numpy as np

x = 0.1
N=np.linspace(1,100,100)
y = N*x*np.exp(-2*x*N)
AT=x*N
plt.plot(N, y)
#plt.legend(loc="upper right")
plt.title("Kihasználtság időszeletelt ALOHA esetén")
plt.ylim(ymin=0)
plt.xlim(xmin=1)
plt.xlim(xmax=100)
plt.xticks([10, 20, 30, 40, 50, 60, 70 ,80, 90, 100])
plt.xlabel("N")
plt.ylabel("Kihasználtság")
plt.show()
