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
    analysD = my_needs(Interval.INTERVAL_1_DAY)

    current_listD = dict(analysD)

    for i in my_symbols:
        d_change = current_listD[i].indicators["change"]
        d_change = round(d_change, 2)
        current_listD[i] = d_change
    current_listD = sorted(
        current_listD.items(), key=lambda item: item[1], reverse=True
    )
    leaders = current_listD[:10]
    losers = current_listD[len(current_listD)-10:]
    losers = sorted(losers, key=lambda item: item[1])

    for i in range(10):
        print(Fore.YELLOW, leaders[i], Fore.RED, losers[i], Fore.RESET)


while True:
    print(ctime(time()))
    work()
    sleep(30)
    os.system('cls')
