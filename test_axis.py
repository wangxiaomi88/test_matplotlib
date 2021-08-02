import numpy as np
import matplotlib.pyplot as mp

#从-π到π拆1000个点
x=np.linspace(-np.pi,np.pi,1000)
y1=np.sin(x)
y2=np.cos(x)/2

#修改x轴刻度文本
# names=["-π","-π/2","0","π/2","π"]
names=[r"$-\pi$",r"$-\frac{\pi}{2}$","0",r"$\frac{\pi}{2}$",r"$\pi$"] #latex表达式
mp.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi], names)

#设置坐标轴
ax=mp.gca() #坐标轴对象
ax.spines["top"].set_color("none") #上轴隐藏
ax.spines["right"].set_color("none") #右轴隐藏
ax.spines["left"].set_color("red")
ax.spines["bottom"].set_color("green")

#移位置 设为原点相交
# ax.yaxis.set_ticks_position('left')
ax.spines["left"].set_position(("data",0))
# ax.xaxis.set_ticks_position('bottom')
ax.spines["bottom"].set_position(("data",0))

#绘制曲线
mp.plot(x,y1,linestyle="--",linewidth=2,alpha=0.7,color="dodgerblue",label=r"$y=sin(x)$")
mp.plot(x,y2,linestyle=":",linewidth=3,color=(0.8,0.8,0.2,0.5),label=r"$y=\frac{1}{2}cos(x)$")



#绘制特殊点
xs,ys=[np.pi/2,np.pi/2],[0,1]
mp.scatter(xs,ys,marker="D",edgecolors="blue",facecolor="yellow",s=100,label="Points",zorder=3) #zorder为图层

# 设置备注
mp.annotate(r"$[\frac{\pi}{2},1]$",xycoords="data",xy=(np.pi/2,1),
                    textcoords="offset points",xytext=(20,30),fontsize=14,
                    arrowprops=dict(arrowstyle="-|>",connectionstyle="angle3"))


#设置图例
mp.legend()





mp.show()




