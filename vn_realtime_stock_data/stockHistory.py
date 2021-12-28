def getStockHistoryData(ticker):
    from datetime import datetime
    from datetime import date
    from dateutil.relativedelta import relativedelta

    # print("Start:", datetime.fromtimestamp(1606237200).strftime("%m/%d/%Y, %H:%M:%S"))
    # print("End:", datetime.fromtimestamp(1640312010).strftime("%m/%d/%Y, %H:%M:%S"))
    # print(datetime.strptime('12/24/2021, 09:13:30', "%m/%d/%Y, %H:%M:%S").timestamp())

    today = date.today().strftime("%m/%d/%Y")
    yesterday = date.today() + relativedelta(days=-1)
    three_months = date.today() + relativedelta(months=-3)

    endTime = datetime.strptime(yesterday.strftime("%m/%d/%Y") + ', 00:00:00', "%m/%d/%Y, %H:%M:%S").timestamp()
    startTime = datetime.strptime(three_months.strftime("%m/%d/%Y") + ', 00:00:0', "%m/%d/%Y, %H:%M:%S").timestamp()
    import requests

    url = 'https://iboard.ssi.com.vn/dchart/api/history?resolution=D&symbol='+str(ticker)+'&from='+str(startTime)+'&to='+str(endTime)
    # print(url)
    x = requests.get(url)
    response = x.json()

    import numpy as np
    import pandas as pd

    timestamp = np.array(response['t']).astype(int)
    close = np.array(response['c']).astype(float)
    open = np.array(response['o']).astype(float)
    high = np.array(response['h']).astype(float)
    low = np.array(response['l']).astype(float)
    volume = np.array(response['v']).astype(int)

    dataset = pd.DataFrame({'Time': timestamp, 'Open': list(open), 'High': list(high), 'Low': list(low), 'Close': list(close), 'Volume': list(volume)}, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
    return dataset


