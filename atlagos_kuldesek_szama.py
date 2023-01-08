import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 0.3, 100)
N=5
y = np.exp(-2*x*N)
res = 1/y
AT=x*N
plt.plot(AT, res)
#plt.legend(loc="upper right")
plt.title("Sikeres küldéshez szükséges próbálkozások átlagos száma")
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlim(xmax=1.5)
plt.xlabel("Bejövő forgalom")
plt.ylabel("Próbálkozások")
plt.show()
