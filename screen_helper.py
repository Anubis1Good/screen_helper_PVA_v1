from tradingview_ta import Interval, get_multiple_analysis
from time import sleep,time,ctime
import os
from symbols import my_symbols, vol_my_symbols
from colorama import Fore, init

init()


def my_needs(interval):
    analysis = get_multiple_analysis(screener='russia',interval=interval, symbols=my_symbols)
    return analysis


def work():
    
    analys5 = my_needs(Interval.INTERVAL_5_MINUTES)

    current_list5 = dict(analys5)

    for i in my_symbols:
        # c_open = current_list5[i].indicators['open']
        c_close = current_list5[i].indicators['close']
        # c_high = current_list5[i].indicators['high']
        # c_low = current_list5[i].indicators['low']
        c_change = current_list5[i].indicators['change']
        c_bbupper = current_list5[i].indicators['BB.upper']
        c_bblow = current_list5[i].indicators['BB.lower']
        # c_range = c_high/c_low * 100-100
        c_close = round(c_close,2)
        c_change = round(c_change,2)
        c_bbupper = round(c_bbupper,2)
        c_bblow = round(c_bblow,2)
        s_time = ctime(time())
        if abs(c_change) > vol_my_symbols[i]:
            if c_change > 0:
                print(Fore.YELLOW + s_time,i,'change:',c_change)
            else:
                print(Fore.RED +s_time,i,'change:',c_change)

        if c_close > c_bbupper:
            print(Fore.GREEN + s_time,i,'bbU:', round(c_close-c_bbupper,2))
        if c_close < c_bblow:
            print(Fore.MAGENTA + s_time,i,'bbD:',round(c_close-c_bblow,2))
        # if c_range > vol_my_symbols[i]:
        #     if c_open-c_close * 3  < c_close-c_low:
        #         print(i,'spring')
        #     if c_open-c_close * 3  < c_high-c_open:
        #         print(i,'uptrust')




while True:
    for i in range(60):
        work()

        sleep(1)
        print(Fore.RESET + ' ')
    os.system('cls')