import MetaTrader5 as mt
from datetime import datetime
import pandas as pd
import plotly.express as plt

mt.initialize()

Login = 51635206
Password = '7Of9@dYEDzclmi'
Server = 'ICMarketsSC-Demo'

mt.login(Login,Password,Server)

ticker = 'AUDJPY'
interval = mt.TIMEFRAME_D1
fromtime = datetime.now()
no_of_rows = 50

rates = mt.copy_rates_from(ticker,interval,fromtime,no_of_rows)
account_info = mt.account_info()

ohlc = pd.DataFrame(mt.copy_rates_range('AUDJPY',mt.TIMEFRAME_M1,datetime(2024,2,16),datetime.now()))
ohlc['time'] = pd.to_datetime(ohlc['time'],unit='s')

fig = plt.line(ohlc,x = ohlc['time'],y = ohlc['close'])
fig.show()

symbol = 'AUDJPY'

request = {
    "action": mt.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 1,
    "type": mt.ORDER_TYPE_BUY,
    "price": mt.symbol_info_tick(symbol).ask,
    "sl": 70.0,
    "tp": 100.0,
    "comment": "Python Script Buy",
    "type_time": mt.ORDER_TIME_GTC,
    "type_filling": mt.ORDER_FILLING_IOC,
}

try:
    # send a trading request
    result = mt.order_send(request)
    print("Order sent successfully:", result)
except Exception as e:
    print("Error sending order:", e)

# Logging
print("Request:", request)
print("Response:", result)


print(account_info.balance)
print(account_info._asdict())
print(ohlc)


