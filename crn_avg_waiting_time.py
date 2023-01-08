import matplotlib.pyplot as plt
import numpy as np

xp = np.linspace(0.1, 0.4, 100)
xs=0.5
mu=1
rop=xp/mu
ros=xs/mu
yp=1+(0.5/(1-rop))
ys=1+(0.5/((1-rop)*(1-rop-ros)))
plt.plot(xp, yp,label="Elsődleges felhasználó")
plt.plot(xp,ys,label="Kognitív felhasználó")
plt.legend(loc="upper right")
plt.title("CRN")
plt.ylim(ymin=0)
plt.xlim(xmin=0.1)
plt.xlim(xmax=0.4)
#plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1])
plt.xlabel("ELsődleges érkezési intenzitás")
plt.ylabel("Átlagos várakozási idő")
plt.show()
