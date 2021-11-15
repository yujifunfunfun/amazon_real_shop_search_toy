import pandas as pd


def cal_profit(biccamera_item_data,edion_item_data,kojima_item_data,ks_item_data,laox_item_data,matsuya_item_data,nojima_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list):
    cols = ['amazonカート価格-FBA','amazonURL','ビックカメラ商品名','ビックカメラ価格','ビックカメラ利益','ビックカメラURL','エディオン商品名','エディオン価格','エディオン利益','エディオンURL','コジマ商品名','コジマ価格','コジマ利益','コジマURL','ケーズ商品名','ケーズ価格','ケーズ利益','ケーズURL','ラオックス商品名','ラオックス価格','ラオックス利益','ラオックスURL','マツヤ電気商品名','マツヤ電気価格','マツヤ電気利益','マツヤ電気URL','ノジマ商品名','ノジマ価格','ノジマ利益','ノジマURL','ヤマダ商品名','ヤマダ価格','ヤマダ利益','ヤマダURL','ヨドバシ商品名','ヨドバシ価格','ヨドバシ利益','ヨドバシURL',]
    profit_df = pd.DataFrame(index=[], columns=cols)
    for biccamera_item,edion_item,kojima_item,ks_item,laox_item,matsuya_item,nojima_item,yamada_item,yodobashi_item,amazon_price in zip(biccamera_item_data,edion_item_data,kojima_item_data,ks_item_data,laox_item_data,matsuya_item_data,nojima_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list):
        biccamera_profit = int(amazon_price[0]) - int(biccamera_item[1])
        edion_profit = int(amazon_price[0]) - int(edion_item[1])
        kojima_profit = int(amazon_price[0]) - int(kojima_item[1])
        ks_profit = int(amazon_price[0]) - int(ks_item[1])
        laox_profit = int(amazon_price[0]) - int(laox_item[1])
        matsuya_profit = int(amazon_price[0]) - int(matsuya_item[1])
        nojima_profit = int(amazon_price[0]) - int(nojima_item[1])
        yamada_profit = int(amazon_price[0]) - int(yamada_item[1])
        yodobashi_profit = int(amazon_price[0]) - int(yodobashi_item[1])
        
        record = pd.Series([amazon_price[0],amazon_price[1],biccamera_item[0],biccamera_item[1],biccamera_profit,biccamera_item[2],edion_item[0],edion_item[1],edion_profit,edion_item[2],kojima_item[0],kojima_item[1],kojima_profit,kojima_item[2],ks_item[0],ks_item[1],ks_profit,ks_item[2],laox_item[0],laox_item[1],laox_profit,laox_item[2],matsuya_item[0],matsuya_item[1],matsuya_profit,matsuya_item[2],nojima_item[0],nojima_item[1],nojima_profit,nojima_item[2],yamada_item[0],yamada_item[1],yamada_profit,yamada_item[2],yodobashi_item[0],yodobashi_item[1],yodobashi_profit,yodobashi_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/profit.csv",encoding="utf_8-sig",index=False)
        
def biccamera_edion_kojima_cal_profit(biccamera_item_data,edion_item_data,kojima_item_data,amazon_price_url_list):
    cols = ['amazonカート価格-FBA','amazonURL','ビックカメラ商品名','ビックカメラ価格','ビックカメラ利益','ビックカメラURL','エディオン商品名','エディオン価格','エディオン利益','エディオンURL','コジマ商品名','コジマ価格','コジマ利益','コジマURL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for biccamera_item,edion_item,kojima_item,amazon_price_url in zip(biccamera_item_data,edion_item_data,kojima_item_data,amazon_price_url_list):
        biccamera_profit = int(amazon_price_url[0]) - int(biccamera_item[1])
        edion_profit = int(amazon_price_url[0]) - int(edion_item[1])
        kojima_profit = int(amazon_price_url[0]) - int(kojima_item[1])
        
        record = pd.Series([amazon_price_url[0],amazon_price_url[1],biccamera_item[0],biccamera_item[1],biccamera_profit,biccamera_item[2],edion_item[0],edion_item[1],edion_profit,edion_item[2],kojima_item[0],kojima_item[1],kojima_profit,kojima_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/biccamera_edion_kojima_profit.csv",encoding="utf_8-sig",index=False)
        

def ks_laox_matsuya_cal_profit(ks_item_data,laox_item_data,matsuya_item_data,amazon_price_url_list):
    cols = ['ケーズ商品名','ケーズ価格','ケーズ利益','ケーズURL','ラオックス商品名','ラオックス価格','ラオックス利益','ラオックスURL','マツヤ電気商品名','マツヤ電気価格','マツヤ電気利益','マツヤ電気URL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for ks_item,laox_item,matsuya_item,amazon_price_url in zip(ks_item_data,laox_item_data,matsuya_item_data,amazon_price_url_list):

        ks_profit = int(amazon_price_url[0]) - int(ks_item[1])
        laox_profit = int(amazon_price_url[0]) - int(laox_item[1])
        matsuya_profit = int(amazon_price_url[0]) - int(matsuya_item[1])

        record = pd.Series([ks_item[0],ks_item[1],ks_profit,ks_item[2],laox_item[0],laox_item[1],laox_profit,laox_item[2],matsuya_item[0],matsuya_item[1],matsuya_profit,matsuya_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/ks_laox_matsuya_profit.csv",encoding="utf_8-sig",index=False)
       
def nojima_yamada_yodobashi_cal_profit(nojima_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list):
    cols = ['ノジマ商品名','ノジマ価格','ノジマ利益','ノジマURL','ヤマダ商品名','ヤマダ価格','ヤマダ利益','ヤマダURL','ヨドバシ商品名','ヨドバシ価格','ヨドバシ利益','ヨドバシURL',]
    profit_df = pd.DataFrame(index=[], columns=cols)
    for nojima_item,yamada_item,yodobashi_item,amazon_price_url in zip(nojima_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list):

        nojima_profit = int(amazon_price_url[0]) - int(nojima_item[1])
        yamada_profit = int(amazon_price_url[0]) - int(yamada_item[1])
        yodobashi_profit = int(amazon_price_url[0]) - int(yodobashi_item[1])
        
        record = pd.Series([nojima_item[0],nojima_item[1],nojima_profit,nojima_item[2],yamada_item[0],yamada_item[1],yamada_profit,yamada_item[2],yodobashi_item[0],yodobashi_item[1],yodobashi_profit,yodobashi_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/nojima_yamada_yodobashi_profit.csv",encoding="utf_8-sig",index=False)

        
if __name__ == "__main__":
    cal_profit()