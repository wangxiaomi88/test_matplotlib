import numpy as np
import matplotlib.pyplot as mp

x=np.linspace(0,8*np.pi,1000)
sinx=np.sin(x)
cosx=0.5*np.cos(0.5*x)

mp.figure("Fill",facecolor="lightgray")
mp.title("Fill",fontsize=16)
mp.grid(linestyle=":")

ax=mp.gca()
step=1
xs=np.arange(0,8.1*np.pi,step*np.pi)
ts=[]
for i in range(len(xs)):
    ts.append("%sπ"%str(i*step))

mp.xticks(xs,ts)

mp.plot(x,sinx,color="dodgerblue",label=r"$y=sin(x)$")
mp.plot(x,cosx,color="orangered",label=r"$y=\frac{1}{2}cos(\frac{1}{2}x)$")

mp.fill_between(x,sinx,cosx,sinx>cosx,color="dodgerblue",alpha=0.3)
mp.fill_between(x,sinx,cosx,sinx<cosx,color="orangered",alpha=0.3)


mp.legend()
mp.show()






