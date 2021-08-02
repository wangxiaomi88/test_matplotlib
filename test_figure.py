import numpy as np
import matplotlib.pyplot as mp

mp.figure("Figure A",facecolor="gray")
mp.plot([0,1],[0,1])
mp.title("Test Title",fontsize=16)
mp.xlabel("Date",fontsize=14)
mp.ylabel("Price",fontsize=14)
mp.grid(linestyle=":")
mp.tight_layout()


mp.figure("Figure B",facecolor="lightgray")
mp.plot([0,1],[1,0])


#重新绘制A窗口
mp.figure("Figure A")
mp.plot([1,2,3],[2,1,3])

mp.show()