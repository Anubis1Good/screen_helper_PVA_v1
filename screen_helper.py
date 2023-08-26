from tradingview_ta import Interval, get_multiple_analysis
from time import sleep,time,ctime,localtime
import os
from symbols import my_symbols, vol_my_symbols
from colorama import Fore, init

init()



def my_needs(interval):
    analysis = get_multiple_analysis(screener='russia',interval=interval, symbols=my_symbols)
    return analysis


def work():
    
    analys5 = my_needs(Interval.INTERVAL_5_MINUTES)
    analysD = my_needs(Interval.INTERVAL_1_DAY)
    current_list5 = dict(analys5)
    current_listD = dict(analysD)

    for i in my_symbols:
        # c_open = current_list5[i].indicators['open']
        c_close = current_list5[i].indicators['close']
        # c_high = current_list5[i].indicators['high']
        # c_low = current_list5[i].indicators['low']
        c_change = current_list5[i].indicators['change']
        c_bbupper = current_list5[i].indicators['BB.upper']
        c_bblow = current_list5[i].indicators['BB.lower']
        # c_range = c_high/c_low * 100-100
        c_vol = current_list5[i].indicators['volume']
        c_close = round(c_close,2)
        c_change = round(c_change,2)
        c_bbupper = round(c_bbupper,2)
        c_bblow = round(c_bblow,2)

        d_change = current_listD[i].indicators['change']
        d_change = round(d_change,2)

        d_vol = current_listD[i].indicators['volume']

        if abs(c_change) > vol_my_symbols[i]:
            if c_change > 0:
                print(Fore.YELLOW + 'chg: ',c_change,i, 'd_change:',d_change)
            else:
                print(Fore.RED +'chg:',c_change,i, 'd_change:',d_change)

        if c_close > c_bbupper:
            print(Fore.CYAN + 'bbU: ', round(c_close-c_bbupper,2),i, 'd_change:',d_change)

        if c_close < c_bblow:
            print(Fore.MAGENTA + 'bbD:',round(c_close-c_bblow,2),i, 'd_change:',d_change)

        if localtime().tm_hour > 11:
            if c_vol/d_vol > 0.04:
                print(Fore.BLUE + 'vol: ',round((c_vol/d_vol)*100,2),i, 'd_change:',d_change)
        # if c_range > vol_my_symbols[i]:
        #     if c_open-c_close * 3  < c_close-c_low:
        #         print(i,'spring')
        #     if c_open-c_close * 3  < c_high-c_open:
        #         print(i,'uptrust')




while True:
    for i in range(60):
        print(ctime(time()))
        work()
        sleep(1)
        print(Fore.RESET + ' ')
    os.system('cls')