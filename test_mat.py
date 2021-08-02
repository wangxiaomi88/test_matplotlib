import numpy as np
import matplotlib.pyplot as mp

x=np.arange(1,6)
y=np.array([34,5,73,32,60])

#绘制水平线
mp.hlines(20,2,4)
#绘制垂直线
mp.vlines(4,10,50)

mp.plot(x,y)
mp.show()



