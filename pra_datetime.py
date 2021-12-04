import datetime


def pra_datetime():
    # 現在時刻
    dt_now = datetime.datetime.now()
    print("======= datetime(dt_now) =======")
    print(type(dt_now))
    print("dt_now: ", dt_now)
    print("year: ", dt_now.year)
    print("hour: ", dt_now.hour)

    # datetimeのコンストラクタ(year,month,dayは必須、hour以下は省略可)
    dt = datetime.datetime(1993, 11, 21)
    print("======= datetime(dt) =======")
    print(type(dt))
    print("dt: ", dt)
    print("year: ", dt.year)
    print("hour: ", dt.hour)

def pra_date():
    d_today = datetime.date.today()
    print("======= date(d_today) =======")
    print(d_today)
    print(type(d_today))
    print('d_today: ', d_today)
    print("year: ", d_today.year)
    print("month: ", d_today.month)
    print("day: ", d_today.day)


if __name__ == "__main__":
    pra_datetime()
    pra_date()
