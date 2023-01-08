import matplotlib.pyplot as plt
import numpy as np

a=0.5;
N=np.linspace(20,50,100);
w=20;
n=10;
AT=a*N;
x=np.power((1-a),N);
Nvesszo=N/w;
u1=Nvesszo*a*(1-a)**(Nvesszo-1);
u0=np.power((1-a),Nvesszo);
y=(u1*(1-u0**w))/(1-u0);
th=1-x-y;
plt.plot(N, th)
plt.title("DCF: ütközés valószínűsége")
plt.ylim(ymin=0)
plt.xlim(xmin=20)
plt.xlim(xmax=50)
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1])
plt.xlabel("N")
plt.ylabel("P")
plt.show()
