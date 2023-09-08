from tradingview_ta import Interval, get_multiple_analysis
from time import sleep, time, ctime
import os
from symbols import my_symbols
from colorama import Fore, init

init()


def my_needs(interval):
    analysis = get_multiple_analysis(
        screener="russia", interval=interval, symbols=my_symbols
    )
    return analysis


def work():
    analys5 = my_needs(Interval.INTERVAL_5_MINUTES)
    analysD = my_needs(Interval.INTERVAL_1_DAY)
    current_list5 = dict(analys5)
    sleep(0.1)
    current_listD = dict(analysD)

    work_list = list()

    for i in my_symbols:
        c_close = current_list5[i].indicators["close"]
        c_change = current_list5[i].indicators["change"]
        c_vol = current_list5[i].indicators["volume"]
        c_close = round(c_close, 2)
        c_change = round(c_change, 2)
        d_change = current_listD[i].indicators["change"]
        d_change = round(d_change, 2)
        d_vol = current_listD[i].indicators["volume"]
        per_vol = (c_vol / d_vol)*100
        work_list.append([i, per_vol, c_change, d_change])


    work_list = sorted(work_list, key=lambda item: item[1], reverse=True)
    text = ''
    for i in range(15):
        title = work_list[i][0]
        vol = str(round(work_list[i][1],3))
        c_change = work_list[i][2]
        d_change = work_list[i][3]
        c_change_str = str(work_list[i][2])
        d_change_str = str(work_list[i][3])
        title = title if len(title) == 10 else title + " "
        c_color = Fore.YELLOW if c_change > 0 else Fore.RED
        d_color = Fore.YELLOW if d_change > 0 else Fore.RED
        text += title + " vol: " + vol + ' cc: ' + c_color + c_change_str + Fore.RESET+' dc: ' + d_color + d_change_str + Fore.RESET + '\n'
    os.system('cls')
    print(ctime(time()))    
    print(text)

while True:
    work()
    sleep(1)   


