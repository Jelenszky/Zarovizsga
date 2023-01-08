import matplotlib.pyplot as plt
import numpy as np
import math

x = 0.2
N=10
j=np.linspace(1 , 10, 10)
y = np.exp(-2*x*N)*np.power((1-np.exp(-2*x*N)),j-1)
plt.plot(j, y)
#plt.legend(loc="upper right")
plt.title("Prob{L=j}")
plt.ylim(ymin=0)
plt.xlim(xmin=1)
plt.xlim(xmax=10)
plt.xlabel("Próbálkozások száma")
plt.ylabel("P")
plt.show()
