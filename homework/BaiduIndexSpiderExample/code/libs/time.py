from datetime import timedelta, datetime
import json


def generate_date(start_date, end_date):
    timemap = []
    for i in range((end_date - start_date).days + 1):
        day = start_date + timedelta(days=i)
        timemap.append(day.strftime("%Y-%m-%d"))
    with open(".\\data\\date_list.json", "w") as f:
        f.write(json.dumps(timemap))
    print("日期生成完成！")
    return timemap


def get_date_list():
    with open(".\\data\\date_list.json", "r") as f:
        data = json.loads(f.read())
        date_list = []
        start_day = datetime.strptime(data[0], "%Y-%m-%d")
        end_day = datetime.strptime(data[-1], "%Y-%m-%d")

    while start_day <= end_day:
        date_temp = start_day.strftime("%Y-%m")
        date_list.append(date_temp)
        start_day += timedelta(weeks=4)

    date_list = list(set(date_list))
    date_list.sort(reverse=False)
    return date_list
