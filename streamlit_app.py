import requests

header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
 
cookie = {
	"PSTM": "553180542",
	"HMACCOUNT": "BA4C08D999D27E4E"
}
 
r = requests.get(url="https://www.ouyicn.gift/priapi/v5/rubik/web/public/spread-arbitrage?t=1645165565597&ctType=linear&arbitrageType=futures_spot", headers=header, cookies=cookie)
rToJson = r.json()
rData= rToJson['data']
# print(r.json()) 
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# import pandas as pd

df=pd.DataFrame(rData)
st.write("这是我们使用数据创建表的首次尝试：")
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })
st.dataframe(df, width=800, height=None)

