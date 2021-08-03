import matplotlib.pyplot as mp

mp.figure("Locators",facecolor="lightgray")
mp.title("Locators",fontsize=16)

#设置x轴的可视区域

locators=["mp.NullLocator()","mp.MultipleLocator(1)","mp.MaxNLocator(nbins=4)","mp.FixedLocator(locs=[2,4,8,10])"]


#设置刻度定位器
# ax.xaxis.set_major_locator(mp.MultipleLocator(1))


for i ,locator in enumerate(locators):
    mp.subplot(len(locators),1,i+1)
    mp.xlim(1, 10)
    ax = mp.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_color("none")
    ax.spines["bottom"].set_color("black")

    ax.spines["bottom"].set_position(("data", 0.5))
    mp.yticks([])

    eval("ax.xaxis.set_major_locator(%s)"%locator)
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))


mp.show()



# def fun1():
#     print("haha1")
#
# def fun2():
#     print("haha2")
#
# t=[fun1,fun2]
# for i in t:
#     i()