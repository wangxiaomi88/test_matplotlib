import numpy as np
import matplotlib.pyplot as mp

n=200
x=np.random.normal(175,5,n)
y=np.random.normal(65,10,n)

mp.figure("Scatter",facecolor="lightgray")
mp.title("Scatter",fontsize=16)
mp.grid(linestyle=":")

# mp.scatter(x,y,marker="o",alpha=0.7,edgecolors="orange",facecolor="dodgerblue",label="Samples",s=80)
mp.scatter(x,y,marker="o",alpha=0.7,c=x,cmap="jet",label="Samples",s=80)

mp.show()



