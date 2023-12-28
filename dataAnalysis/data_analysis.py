import pandas as pd

data = pd.read_csv("dataAnalysis/amazon_laptop_prices_v01.csv")

result = {}
for cols in ["brand" ,"harddisk","cpu","ram"] :
    result[cols] = data[cols].value_counts()[:10].to_dict()

