import matplotlib.pyplot as plt
import numpy as np

a=0.1;
N=np.linspace(1,50,100);
w=16;
n=10;
AT=a*N;
x=np.power((1-a),N);
Nvesszo=N/w;
u1=Nvesszo*a*(1-a)**(Nvesszo-1);
u0=np.power((1-a),Nvesszo);
y=(u1*(1-u0**w))/(1-u0);
th=(y*n)/((1-x)*n+1)/AT;
plt.plot(N, th)
plt.title("DCF: közeghez való hozzáférés valószínűsége")
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlim(xmax=1)
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 ,0.8, 0.9, 1])
plt.xlabel("N")
plt.ylabel("P")
plt.show()
