import pandas as pd
import re


def load_model_number():
    df = pd.read_csv('~/Desktop/amazon.csv',usecols=['Product Codes: PartNumber'])
    df = df.fillna('None')
    df = df.values.tolist()
    model_number_list = []
    for model_number in df:
        model_number_list.append(model_number[0])
    return model_number_list

def load_jan():
    df = pd.read_csv('~/Desktop/amazon.csv',usecols=['Product Codes: EAN'])
    df = df.fillna('None')
    df = df.values.tolist()
    jan_list = []
    for jan in df:
        jan_list.append(jan[0])
    return jan_list

def load_buybox_asin_name():
    df = pd.read_csv('~/Desktop/amazon.csv',usecols=['ASIN','新品: 現在価格'])
    df = df.fillna('None')
    df = df.values.tolist()
    buybox_asin_name_list = []
    for buybox_asin_name in df:
        buybox = buybox_asin_name[1]
        buybox = re.sub(r'\D', '', buybox) 
        buybox_asin_name_list.append([buybox,buybox_asin_name[2],buybox_asin_name[0]])
    return buybox_asin_name_list


def join_csv():
    biccamera_edion_kojima_profit_df = pd.read_csv("~/Desktop/biccamera_edion_kojima_profit.csv")
    ks_laox_matsuya_profit_df = pd.read_csv("~/Desktop/ks_laox_matsuya_profit.csv")
    nojima_yamada_yodobashi_profit_df = pd.read_csv("~/Desktop/nojima_yamada_yodobashi_profit.csv")
    data_list = []
    data_list.append(biccamera_edion_kojima_profit_df)
    data_list.append(ks_laox_matsuya_profit_df)
    data_list.append(nojima_yamada_yodobashi_profit_df)
    
    df = pd.concat(data_list, axis=1, sort=True)

    df.to_csv("~/Desktop/profit.csv",encoding="utf_8-sig",index=False)

if __name__ == "__main__":
    join_csv()



