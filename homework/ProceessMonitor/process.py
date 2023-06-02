import psutil,time,schedule
from mail import sendmail
from config import config
# 获取网卡WLAN的mac地址
def get_mac_add(name):
    nics = psutil.net_if_addrs()
    mac_add = (
        [
            j.address
            for i in nics
            for j in nics[i]
            if i == name and j.family == psutil.AF_LINK
        ]
    )[0]
    return mac_add.replace("-", ":")

# 获取进程和内存占用率的字典
def get_proccess_dict():
    # 查看所有进程
    pid = psutil.pids()

    # 创建进程字典
    process_dict = {}

    for k, i in enumerate(pid):
        try:
            proc = psutil.Process(i)
            # 循环更新字典
            process_dict.update({proc.name(): proc.memory_percent()})
        except psutil.AccessDenied:
            pass
    # 返回字典
    return process_dict

# 获取进程排名
def rank():
    # 第一次
    procees_dict1 = get_proccess_dict()
    # 睡眠10秒
    time.sleep(1)

    # 第二次
    procees_dict2 = get_proccess_dict()
    time.sleep(1)
    
    # 第三次
    procees_dict3 = get_proccess_dict()

    # 提取3个dic中key出现3的key-value,并转化成列表
    proc_name = list(procees_dict1.keys() & procees_dict2.keys() & procees_dict3.keys())

    # 生成新的字典
    proc_dict = {}
    for i in proc_name:
        proc_dict.update({i: float(procees_dict3[i])})

    # 整理词典，排序越大的越靠前
    new_dict = sorted(proc_dict.items(), key=lambda x: x[1], reverse=True)
    return new_dict


def proc_info():
    # 获取MAC地址
    mac_add = get_mac_add(config.network_name)
    # 获取进程字典
    process_dict = rank()
    # 内存占用
    memory = format(psutil.virtual_memory().percent, ".2f")+ "%"

    str1 = "MAC地址                告警类型                  排名前2的进程         内存占用率\n"

    str2 = "{}        {}        {},{}        {}\n".format(
        mac_add,
        "内存告警",
        # 读取前两个进程
        process_dict[0][0],
        process_dict[1][0],
        memory,
    )

    # 返回两行字符串的拼接
    return str1 + str2

def nowarning(memory):
    # 获取MAC地址
    mac_add = get_mac_add(config.network_name)
    str1 = "MAC地址           告警类型            内存占用率\n"
    str2 = "{}        {}           {}%s\n".format(mac_add,"内存告警",memory)
    return str1 + str2

def job():
    # 内存占用
    memory = format(psutil.virtual_memory().percent, ".2f")
    # 判断占用情况
    if float(memory) > 70:
        sendmail(proc_info(), "内存告警")
    else:
        sendmail(nowarning(memory), "内存告警")

# 定时任务，每10s执行一次
schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
