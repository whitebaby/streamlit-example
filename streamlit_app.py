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

r = requests.get(url="https://www.okx.com/priapi/v5/rubik/web/public/spread-arbitrage?t=1645165565597&ctType=linear&arbitrageType=futures_spot", headers=header, cookies=cookie)
rToJson = r.json()
rData= rToJson['data']


# import pandas as pd

df1=pd.DataFrame(rData)
st.header("Arbitrage Stragety Live Data ")
st.info("Users can click to zoom in ")
# df1
# = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

st.dataframe(df1, width=1200, height=500)


from datetime import datetime

def stamp2time(timestamp): #时间戳转日期函数

    time_local = time.localtime(timestamp/1000)

    dt = time.strftime("%Y-%m-%d", time_local)

    return dt
def convert_currency(value):
    new_value = np.float(value.replace(',', '').replace('￥', ''))
	# print(new_value)
    return new_value


r2 = requests.get(url="https://api.anchorprotocol.com/api/v1/deposit/1d", headers=header, cookies=cookie)
rToJson2 = r2.json()
rData2= rToJson2['total_ust_deposits']


df2=pd.DataFrame(rData2)

st.write("")
st.header("Deposit USD Amount Live Data ")
df2[['deposit']] = df2[['deposit']].astype('float')
df2['deposit'] = df2['deposit'].div(10000*10000*10)
df2["timestamp"]=df2["timestamp"].apply(stamp2time)

df2.set_index(['timestamp'],inplace=True)
df2 = df2.sort_index()
# data2 = df2.tail(50)
data2 = df2[-50:-3]
# print(data2)

st.bar_chart(data2)

r_apy = requests.get(url="https://apiv2.coindix.com/search?sort=-base&kind=stable", headers=header, cookies=cookie)
rToJson_apy = r_apy.json()
rData_apy= rToJson_apy['data']


# import pandas as pd

st.write("")
st.header("Platform revenue source")
df_apy=pd.DataFrame(rData_apy)
# print(df_apy)
# df_apy.drop(['icon', 'rewards'], inplace=True)
df_apy.drop(['icon', 'rewards','base','reward','link',"is_new","watched",'id'], axis=1, inplace=True) 
df_apy['apy']=df_apy['apy'].map(lambda x :'%.2f%%'  %  (x*100),)
df_apy['apy_7_day']=df_apy['apy_7_day'].map(lambda x :'%.2f%%'  %  (x*100),)
st.dataframe(df_apy, width=1200, height=500)


time.sleep(60)
st.experimental_rerun()
