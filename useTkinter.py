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

    output = "This is output value"

    thi = "s value of proof"

    value = "test value"

    return_value = "this is return value"

    return [timeFrom, timeTo, output, "test", value, return_value]

def coount(target, now):
    if target <= now:
        print("over target value")
        return
    now += 1

def get_conf(combo_mode, combo_car, tx_stime, tx_etime, tx_key, com_2):
    com_mode = combo_mode.get()
    com_car = combo_car.get()
    text_stime = tx_stime.get()
    text_etime = tx_etime.get()
    text_key = tx_key.get()
    coms_2 = com_2.get()

    print("mode: " + com_mode)
    print("car: " + com_car)
    print("stime: " + text_stime)
    print("etime: " + text_etime)
    print("key: " + text_key)
    print("com2:" + coms_2)
    print("This is test code.")

    return [com_mode, com_car, text_stime, text_etime, text_key]

def make_gui():
    timeFromTo = set_today()
    root = Tk()
    root.title("1st App by tkinter")

    label_mode = ttk.Label(root, text="Select mode")
    combo_mode = ttk.Combobox(root, state="readonly")
    combo_mode["values"] = ("A", "B", "C", "D", "E", "F")
    combo_mode.current(2)

    label_car = ttk.Label(root, text="Select Code")
    combo_car = ttk.Combobox(root, state='readonly')
    combo_car["values"] = ("AA", "BB", "CC", "DD", "EE", "FF", "GG")
    combo_car.current(4)

    tx_stime = StringVar(value=timeFromTo[0])
    label_stime = ttk.Label(root, text="Start Time")
    entry_stime = ttk.Entry(root, textvariable=tx_stime)

    tx_etime = StringVar(value=timeFromTo[1])
    label_etime = ttk.Label(root, text="End Time")
    entry_etime = ttk.Entry(root, textvariable=tx_etime)

    tx_key = StringVar()
    label_key = ttk.Label(root, text="Key Code value")
    entry_key = ttk.Entry(root, textvariable=tx_key)
    tx_key2 = StringVar(value="02 value")
    label_key2 = ttk.Label(root, text="Code 02 value")
    entry_key2 = ttk.Entry(root, textvariable=tx_key2)

    label_2 = ttk.Label(root, text="2nd")
    combo_2 = ttk.Combobox(root, state='readonly')
    combo_2["values"] = ("A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2")
    combo_2.current(6)

    label_3 = ttk.Label(root, text="3rd")
    combo_3 = ttk.Combobox(root, state='readonly')
    combo_3["values"] = ("A2AA", "B2BB", "C2CC", "D2DD", "E2EE", "F2FF")
    combo_3.current(4)

    print("after instance making")

    button = ttk.Button(root, text="OK", command=lambda: get_conf(combo_mode, combo_car, tx_stime, tx_etime, tx_key, combo_2))

    combo = ttk.Combobox(root, state='readonly')

    combo["values"] = ("A", "B", "C", "D", "E", "F" , "G")
    print(combo["values"][0])

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
    label_key2.grid(row=5, column=1)
    entry_key2.grid(row=5, column=2)
    label_2.grid(row=7, column=2)
    combo_2.grid(row=7, column=1)
    label_3.grid(row=8, column=0)
    combo_3.grid(row=8, column=1)

    root.mainloop()


make_gui()
print("end of code")