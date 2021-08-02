import numpy as np
import matplotlib.pyplot as mp

#从-π到π拆1000个点
x=np.linspace(-np.pi,np.pi,1000)
y1=np.sin(x)
y2=np.cos(x)/2

#修改x轴刻度文本
names=["-π","-π/2","0","π/2","π"]
names=[r"$-\pi$",r"$-\frac{\pi}{2}$","0",r"$\frac{\pi}{2}$",r"$\pi$"] #latex表达式
mp.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi], names)

mp.plot(x,y1,linestyle="--",linewidth=2,alpha=0.7,color="dodgerblue")
mp.plot(x,y2,linestyle=":",linewidth=3,color=(0.8,0.8,0.2,0.25))



mp.show()




