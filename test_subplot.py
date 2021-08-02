import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

#矩阵式布局
mp.figure("Subplot",facecolor="lightgray")

for i in range(1,10):
    mp.subplot(3,3,i)
    mp.text(0.5,0.5,str(i)+"p",ha="center",va="center",size=36,alpha=0.6)
    mp.xticks([]) #隐藏x轴
    mp.yticks([]) #隐藏y轴
    mp.tight_layout()


#网格式布局
mp.figure("GripSpec",facecolor="lightgray")
gs=mg.GridSpec(3,3)
mp.subplot(gs[0, :2])
mp.text(0.5,0.5,1,ha="center",va="center",size=36,alpha=0.6)
mp.xticks([]) #隐藏x轴
mp.yticks([]) #隐藏y轴
mp.tight_layout()

mp.subplot(gs[:2, 2])
mp.text(0.5,0.5,2,ha="center",va="center",size=36,alpha=0.6)
mp.xticks([]) #隐藏x轴
mp.yticks([]) #隐藏y轴
mp.tight_layout()

# mp.subplot(3,3,5)
mp.subplot(gs[1, 1])
mp.text(0.5,0.5,3,ha="center",va="center",size=36,alpha=0.6)
mp.xticks([]) #隐藏x轴
mp.yticks([]) #隐藏y轴
mp.tight_layout()

mp.subplot(gs[1:, 0])
mp.text(0.5,0.5,4,ha="center",va="center",size=36,alpha=0.6)
mp.xticks([]) #隐藏x轴
mp.yticks([]) #隐藏y轴
mp.tight_layout()

mp.subplot(gs[2, 1:])
mp.text(0.5,0.5,5,ha="center",va="center",size=36,alpha=0.6)
mp.xticks([]) #隐藏x轴
mp.yticks([]) #隐藏y轴
mp.tight_layout()



#自由布局
mp.figure("Free Layout",facecolor="lightgray")
mp.axes([0.06,0.03,0.6,0.4]) #[起始点横坐标，起始点纵坐标，窗口宽，窗口高]
mp.axes([0.33,0.33,0.5,0.5])


mp.show()