import requests
# print(r.json()) 
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time

header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
 
cookie = {
	"PSTM": "553180542",
	"HMACCOUNT": "BA4C08D999D27E4E"
}

r = requests.get(url="https://www.ouyicn.gift/priapi/v5/rubik/web/public/funding-rate-arbitrage?t=1645165302774&ctType=linear&arbitrageType=futures_spot", headers=header, cookies=cookie)
rToJson = r.json()
rData= rToJson['data']


# import pandas as pd

df=pd.DataFrame(rData)
st.header("Arbitrage Stragety Live Data ")
st.info("Users can click to zoom in ")
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

st.dataframe(df, width=1200, height=500)

from pyecharts.charts import Bar
from pyecharts.faker import Faker
import streamlit_echarts
from pyecharts import options as opts
from pyecharts.globals import ThemeType

def stamp2time(timestamp): #时间戳转日期函数

    time_local = time.localtime(timestamp/1000)

    dt = time.strftime("%Y-%m-%d", time_local)

    return dt
def convert_currency(value):
    new_value = np.float(value.replace(',', '').replace('￥', ''))
	# print(new_value)
    return new_value

header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
 
cookie = {
	"PSTM": "553180542",
	"HMACCOUNT": "BA4C08D999D27E4E"
}

r = requests.get(url="https://api.anchorprotocol.com/api/v1/deposit/1d", headers=header, cookies=cookie)
rToJson = r.json()
rData= rToJson['total_ust_deposits']


df_line=pd.DataFrame(rData)
# xData =df_line["timestamp"].values.tolist()

# df_line=pd.DataFrame(rData)

df_line["timestamp"]=df_line["timestamp"].apply(stamp2time)

df_line[['deposit']] = df_line[['deposit']].astype('float')
df_line['deposit'] = df_line['deposit'].div(10000*10000*10)
df_line[['deposit']] = df_line[['deposit']].astype('int')

df_line = df_line.sort_index(ascending=False)
df_line= df_line.tail(60)
xData =df_line["timestamp"].values.tolist()
yData =df_line["deposit"].values.tolist()

st.header("Deposit USD Amount Live Data ")
bar = Bar()
bar.add_xaxis(xData)
bar.add_yaxis("Deposit Amount USD", yData)
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(title_opts=opts.TitleOpts(title="AMOUNT", subtitle="USD"))
streamlit_echarts.st_pyecharts(
    bar,
    theme=ThemeType.DARK
)

# time.sleep(10)
st.experimental_rerun()



