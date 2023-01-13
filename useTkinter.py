from tkinter import *
from tkinter import ttk
import datetime

def set_today():
    dt_now = datetime.datetime.now()
    dt_nowMonth = "0" + str(dt_now.month)
    dt_nowDay = "0" + str(dt_now.day)
    timeFrom = '{}-{}-{}T{}:{}:{}'.format(dt_now.year, dt_nowMonth[len(dt_nowMonth) - 2:],
                                          dt_nowDay[len(dt_nowDay) - 2:], "00", "00", "00")
    timeTo = '{}-{}-{}T{}:{}:{}'.format(dt_now.year, dt_nowMonth[len(dt_nowMonth) - 2:],
                                        dt_nowDay[len(dt_nowDay) - 2:], "23", "59", "59")

    return [timeFrom, timeTo]


def get_conf(combo_mode, combo_car, tx_stime, tx_etime, tx_key):
    com_mode = combo_mode.get()
    com_car = combo_car.get()
    text_stime = tx_stime.get()
    text_etime = tx_etime.get()
    text_key = tx_key.get()

    print("mode: " + com_mode)
    print("car: " + com_car)
    print("stime: " + text_stime)
    print("etime: " + text_etime)
    print("key: " + text_key)

    return [com_mode, com_car, text_stime, text_etime, text_key]

def make_gui():
    timeFromTo = set_today()
    root = Tk()
    root.title("Use Tkinter")

    label_mode = ttk.Label(root, text="モード選択")
    combo_mode = ttk.Combobox(root, state="readonly")
    combo_mode["values"] = ("A", "B", "C", "D")
    combo_mode.current(0)

    label_car = ttk.Label(root, text="車両選択")
    combo_car = ttk.Combobox(root, state='readonly')
    combo_car["values"] = ("AA", "BB", "CC", "DD")
    combo_car.current(1)

    tx_stime = StringVar(value=timeFromTo[0])
    label_stime = ttk.Label(root, text="開始時刻")
    entry_stime = ttk.Entry(root, textvariable=tx_stime)

    tx_etime = StringVar(value=timeFromTo[1])
    label_etime = ttk.Label(root, text="終了時刻")
    entry_etime = ttk.Entry(root, textvariable=tx_etime)

    tx_key = StringVar()
    label_key = ttk.Label(root, text="API Key")
    entry_key = ttk.Entry(root, textvariable=tx_key)
    tx_key2 = StringVar()
    label_key2 = ttk.Label(root, text="API Key")
    entry_key2 = ttk.Entry(root, textvariable=tx_key2)

    button = ttk.Button(root, text="OK", command=lambda: get_conf(combo_mode, combo_car, tx_stime, tx_etime, tx_key))

    combo = ttk.Combobox(root, state='readonly')

    combo["values"] = ("A", "B", "C")

    combo.current(0)

    label_mode.grid(row=0, column=0)
    combo_mode.grid(row=0, column=1)
    label_car.grid(row=1, column=0)
    combo_car.grid(row=1, column=1)
    label_stime.grid(row=2, column=0)
    entry_stime.grid(row=2, column=1)
    label_etime.grid(row=3, column=0)
    entry_etime.grid(row=3, column=1)
    label_key.grid(row=4, column=0)
    entry_key.grid(row=4, column=1)

    button.grid(row=5, column=0)
    label_key2.grid(row=6, column=0)
    entry_key2.grid(row=6, column=1)

    root.mainloop()


make_gui()