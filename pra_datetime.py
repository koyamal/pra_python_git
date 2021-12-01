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
    print("dt_now: ", dt)
    print("year: ", dt.year)
    print("hour: ", dt.hour)


if __name__ == "__main__":
    pra_datetime()
