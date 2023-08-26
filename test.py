from tradingview_ta import Interval, get_multiple_analysis, TA_Handler
from pprint import pprint as pp
import time
# tesla = TA_Handler(
#     symbol="SBER",
#     screener="russia",
#     exchange="MOEX",
#     interval=Interval.INTERVAL_1_DAY,

# )
# tesla = tesla.get_analysis()
# pp(str(tesla.time.time())[:-7])
# analys = TA_Handler(
#     symbol=symbol,
#     screener="russia",
#     exchange="MOEX",
#     interval=Interval.INTERVAL_1_DAY,

# )
# analys = analys.get_analysis()
# print(analys.indicators['change'], str(analys.time.time())[:-7])
# def get_day_change(symbol):
#     sep = symbol.find(':')
#     f_symbol = symbol[sep+1:]
#     s_symbol = symbol[:sep]
#     analys = TA_Handler(
#         symbol=f_symbol,
#         screener="russia",
#         exchange=s_symbol,
#         interval=Interval.INTERVAL_1_DAY,

#     )
#     analys = analys.get_analysis()
#     return analys.indicators['change']

pp(time.localtime().tm_hour)