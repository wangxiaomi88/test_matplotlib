import numpy as np
import matplotlib.pyplot as mp


def loadcsv(filepath):
    header = []
    data = []
    with open(filepath, "r") as f:
        for index, line in enumerate(f.readlines()):
            if index == 0:
                header = line[:-1].split(",")
            else:
                data.append(tuple(line[:-1].split(",")))

    result = np.array(data, dtype={"names": header,
                                   "formats": ["f8", "f8", "f8", "f8", "f8", "f8"]})  # 构建一个一维数组，每个元素是一个元组且起好了名字
    return result


if __name__ == '__main__':
    data = loadcsv("data.csv")  # index,pack_type,extra_time,extra_flow,use_month,loss
    print(data[0]["extra_time"], data.shape)

    extra_time_col = data["extra_time"]
    print("extra_time min value: ", min(extra_time_col), "extra_time max value: ", max(extra_time_col), "mean: ",
          sum(extra_time_col) / len(extra_time_col))
    extra_flow_col = data["extra_flow"]
    print("extra_flow min value: ", min(extra_flow_col), "extra_flow max value: ", max(extra_flow_col), "mean: ",
          sum(extra_flow_col) / len(extra_flow_col))
    use_month_col = data["use_month"]
    print("use_month min value: ", min(use_month_col), "use_month max value: ", max(use_month_col), "mean: ",
          sum(use_month_col) / len(use_month_col))

    print("有剩余通话时间的人数占比：", data[data["extra_time"] > 0].size / data.size)
    print("有剩余流量的人数占比：", data[data["extra_flow"] > 0].size / data.size)

    kinds = set(data["pack_type"])
    for k in kinds:
        print(k, "套餐占比：", data[data["pack_type"] == k].size / data.size)

    # 整理剩余流量、剩余通话时间与用户流失之间的关系
    extra_flow_col = data["extra_flow"]
    extra_time_col = data["extra_time"]
    loss_col = data["loss"]
    mp.figure("extra_flow & loss", facecolor="lightgray")
    mp.title("extra_flow & loss", fontsize=16)
    mp.xlabel("extra_flow", fontsize=14)
    mp.ylabel("loss", fontsize=14)
    mp.grid(linestyle=":")

    mp.subplot(2, 1, 1)
    mp.scatter(extra_flow_col, loss_col, marker="o", s=80, label="Samples", c=extra_flow_col, cmap="jet", alpha=0.5)

    mp.subplot(2, 1, 2)
    mp.scatter(extra_time_col, loss_col, marker="o", s=80, label="Samples", c=extra_time_col, cmap="jet", alpha=0.5)

    mp.legend()


    #费流失用户剩余流量与剩余通话之间的关系
    extra_flow_user_col=extra_flow_col[loss_col==0]
    extra_time_user_col=extra_time_col[loss_col==0]
    mp.figure("extra_flow & extra_time", facecolor="lightgray")
    mp.title("extra_flow & extra_time", fontsize=16)
    mp.xlabel("extra_flow", fontsize=14)
    mp.ylabel("extra_time", fontsize=14)
    mp.grid(linestyle=":")
    mp.scatter(extra_flow_user_col,extra_time_user_col,color="dodgerblue",alpha=0.7)

    ax = mp.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")

    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))

    mp.xlim(-500,500)
    mp.ylim(-2000,2000)

    mp.show()
