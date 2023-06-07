import pandas as pd
from datetime import datetime, timedelta


def last_week_dates():
    # 获取当前日期
    current_date = datetime.now()

    # 计算上个星期的起止日期
    start_of_last_week = current_date - timedelta(days=current_date.weekday() + 7)
    end_of_last_week = start_of_last_week + timedelta(days=6)

    # 格式化日期为年月日
    start_date = start_of_last_week.strftime("%Y-%m-%d")
    end_date = end_of_last_week.strftime("%Y-%m-%d")

    # 生产date_list
    date_list = []
    for i in range(7):
        date_list.append((start_of_last_week + timedelta(days=i)).strftime("%Y-%m-%d"))
    return start_date, end_date, date_list


def setup_run_environment(self, env):
    env.prepend_path(
        "LD_LIBRARY_PATH",
        "/sh3/ysuanbase/share/software/public/readline-8.1-6wg6vx4635ds6c2tienwdsml6sokr5le/lib:/sh3/ysuanbase/share/software/public/fftw-3.3.9-qbmz3ufglofkghlwgu7pdjum3xkce52v/lib:/sh3/ysuanbase/share/software/public/openblas-0.3.20-wgqpnutgjezfev4byhffsl3blrwyrnbj/lib",
    )


def calculate_fee():
    # 调用函数并输出结果
    start_date, end_date, date_list = last_week_dates()

    file = "data\shanhe\按资源类型统计_202305.xls"
    df = pd.read_excel(file, sheet_name=0, header=0, index_col=0)

    # 将时间列转换为datetime类型
    df["时间"] = pd.to_datetime(df["时间"])

    # 筛选出上个星期的数据
    df = df[df["时间"].isin(date_list)]

    # print(df)
    # 根据资源类型分类求费用总和
    fee = df.groupby("资源类型")["费用"].sum()

    # 保存结果到excle文件,文件名为 山河云start_date-end_date.
    fee.to_csv("data\shanhe\山河云" + start_date + "-" + end_date + "费用统计.csv")


if __name__ == "__main__":
    calculate_fee()
    # test()
