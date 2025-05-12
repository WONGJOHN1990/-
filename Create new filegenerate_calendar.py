import datetime
from chinese_calendar import lunar2solar, is_leap_month
from ics import Calendar, Event

def generate_lunar_calendar(year):
    c = Calendar()
    ten_days = [1, 8, 14, 15, 18, 23, 24, 28, 29, 30]
    six_days = [8, 14, 15, 23, 29, 30]

    # 农历十斋日和六斋日
    for month in range(1, 13):
        for day in ten_days:
            try:
                solar_date = lunar2solar(year, month, day)
                e = Event(name="十斋日", begin=solar_date)
                c.events.add(e)
            except ValueError:
                pass  # 跳过农历不存在的日期
        for day in six_days:
            try:
                solar_date = lunar2solar(year, month, day)
                e = Event(name="六斋日", begin=solar_date)
                c.events.add(e)
            except ValueError:
                pass

    # 特殊佛教节日
    buddhist_festivals = {
        (1, 1): "弥勒佛圣诞",
        (1, 6): "定光佛圣诞",
        (2, 8): "释迦牟尼佛出家",
        (2, 9): "帝释天尊圣诞日",
        (2, 15): "释迦牟尼佛涅槃",
        (2, 19): "观世音菩萨圣诞",
        (2, 21): "普贤菩萨圣诞",
        (3, 16): "准提菩萨圣诞",
        (4, 4): "文殊菩萨圣诞",
        (4, 8): "释迦牟尼佛圣诞",
        (4, 15): "佛吉祥日——释迦牟尼佛诞生、成道、涅槃三期同一庆",
        (4, 15): "药王菩萨圣诞日",
        (5, 8): "善慧菩萨圣诞日",
        (5, 13): "伽蓝菩萨圣诞",
        (6, 3): "护法韦驮尊天菩萨圣诞",
        (6, 10): "金粟如来圣诞日",
        (6, 19): "观世音菩萨成道——此日放生、念佛，功德殊胜",
        (7, 13): "大势至菩萨圣诞",
        (7, 15): "佛欢喜日、盂兰盆节",
        (7, 24): "龙树菩萨圣诞",
        (7, 30): "地藏菩萨圣诞",
        (8, 15): "月光菩萨圣诞日",
        (8, 22): "燃灯佛圣诞",
        (9, 9): "摩利支天菩萨圣诞日 重阳节",
        (9, 19): "观世音菩萨出家纪念日",
        (9, 30): "药师琉璃光如来圣诞",
        (10, 5): "达摩祖师圣诞",
        (10, 11): "憨山德清大师圆寂日",
        (10, 20): "文殊师利菩萨出家日",
        (11, 17): "阿弥陀佛圣诞",
        (11, 19): "日光菩萨圣诞",
        (12, 8): "释迦如来成道日",
        (12, 22): "文殊师利菩萨成道日",
        (12, 23): "监斋菩萨圣诞日",
        (12, 29): "华严菩萨圣诞",
    }

    for (lunar_month, lunar_day), festival_name in buddhist_festivals.items():
        try:
            solar_date = lunar2solar(year, lunar_month, lunar_day)
            e = Event(name=festival_name, begin=solar_date)
            c.events.add(e)
        except ValueError:
            pass

    # 保存到文件
    with open("lunar_calendar.ics", "w", encoding='utf-8') as f:
        f.writelines(c.serialize())

if __name__ == "__main__":
    now = datetime.datetime.now()
    generate_lunar_calendar(now.year)
