import pandas as pd


def fetch_biccamera_yamada_yodobashi_cal_profit(biccamera_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list):
    cols = ['amazonカート価格-FBA','amazonURL','ビックカメラ商品名','ビックカメラ価格','ビックカメラ利益','ビックカメラURL','ヤマダ商品名','ヤマダ価格','ヤマダ利益','ヤマダURL','ヨドバシ商品名','ヨドバシ価格','ヨドバシ利益','ヨドバシURL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for biccamera_item,yamada_item,yodobashi_item,amazon_price_url in zip(biccamera_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list):
        biccamera_profit = int(amazon_price_url[0]) - int(biccamera_item[1])
        yamada_profit = int(amazon_price_url[0]) - int(yamada_item[1])
        yodobashi_profit = int(amazon_price_url[0]) - int(yodobashi_item[1])

        record = pd.Series([amazon_price_url[0],amazon_price_url[1],biccamera_item[0],biccamera_item[1],biccamera_profit,biccamera_item[2],yamada_item[0],yamada_item[1],yamada_profit,yamada_item[2],yodobashi_item[0],yodobashi_item[1],yodobashi_profit,yodobashi_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/biccamera_yamada_yodobashi_profit.csv",encoding="utf_8-sig",index=False)
        

def edion_kojima_nojima_cal_profit(edion_item_data,kojima_item_data,nojima_item_data,amazon_price_url_list):
    cols = ['エディオン商品名','エディオン価格','エディオン利益','エディオンURL','コジマ商品名','コジマ価格','コジマ利益','コジマURL','ノジマ商品名','ノジマ価格','ノジマ利益','ノジマURL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for edion_item,kojima_item,nojima_item,amazon_price_url in zip(edion_item_data,kojima_item_data,nojima_item_data,amazon_price_url_list):

        edion_profit = int(amazon_price_url[0]) - int(edion_item[1])
        kojima_profit = int(amazon_price_url[0]) - int(kojima_item[1])
        nojima_profit = int(amazon_price_url[0]) - int(nojima_item[1])

        record = pd.Series([edion_item[0],edion_item[1],edion_profit,edion_item[2],kojima_item[0],kojima_item[1],kojima_profit,kojima_item[2],nojima_item[0],nojima_item[1],nojima_profit,nojima_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/edion_kojima_nojima_profit.csv",encoding="utf_8-sig",index=False)
       

        
if __name__ == "__main__":
    edion_kojima_nojima_cal_profit()