import pandas as pd
import re


def load_model_number():
    df = pd.read_csv('Product_Finder.2021_11_7.products.csv',usecols=['Model'])
    df = df.fillna('None')
    df = df.values.tolist()
    model_number_list = []
    for model_number in df:
        model_number_list.append(model_number[0])

    return model_number_list

def load_buybox_asin():
    df = pd.read_csv('Product_Finder.2021_11_7.products.csv',usecols=['ASIN','Buy Box 🚚: 現在価格'])
    df = df.fillna('None')
    df = df.values.tolist()
    buybox_asin_list = []
    for buybox_asin in df:
        buybox = buybox_asin[0]
        buybox = re.sub(r'\D', '', buybox) 
        buybox_asin_list.append([buybox,buybox_asin[1]])
        
    return buybox_asin_list

def join_csv():
    biccamera_edion_kojima_profit_df = pd.read_csv("~/Desktop/biccamera_edion_kojima_profit.csv")
    ks_laox_matsuya_profit_df = pd.read_csv("~/Desktop/ks_laox_matsuya_profit.csv")
    nojima_yamada_yodobashi_profit_df = pd.read_csv("~/Desktop/nojima_yamada_yodobashi_profit.csv")
    data_list = []
    data_list.append(biccamera_edion_kojima_profit_df)
    data_list.append(ks_laox_matsuya_profit_df)
    data_list.append(nojima_yamada_yodobashi_profit_df)
    
    df = pd.concat(data_list, axis=0, sort=True)

    df.to_csv("~/Desktop/profit.csv",encoding="utf_8-sig",index=False)