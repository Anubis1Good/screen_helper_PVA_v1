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
    text = ''
    for i in range(10):
        leader = str(leaders[i])
        loser = str(losers[i])
        text += Fore.YELLOW + leader + ' ' + Fore.RED + loser + Fore.RESET + '\n'
    os.system('cls')
    print(ctime(time()))
    print(Fore.YELLOW + '------LEADERS------', Fore.RED + '------LOSERS------')
    print(text)


while True:
    work()
    sleep(30)

