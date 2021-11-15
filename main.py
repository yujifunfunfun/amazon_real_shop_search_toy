from engine.biccamera import *
from engine.edion import *
from engine.kojima import *
from engine.ks import *
from engine.laox import *
from engine.matsuya import *
from engine.nojima import *
from engine.yamada import *
from engine.yodobashi import *
from engine.amazon import *
from engine.cal_profit import *
from common.csv import *
from common.chromedriver import *
import multiprocessing
from multiprocessing import freeze_support



def fetch_biccamera_edion_kojima_data(driver,model_number_list,amazon_price_url_list):
    biccamera_item_data = fetch_biccamera_data(driver,model_number_list)
    edion_item_data = fetch_edion_data(driver,model_number_list)
    kojima_item_data = fetch_kojima_data(driver,model_number_list)
    driver.quit()
    
    biccamera_edion_kojima_cal_profit(biccamera_item_data,edion_item_data,kojima_item_data,amazon_price_url_list)

def fetch_ks_laox_matsuya_data(driver,model_number_list,amazon_price_url_list):
    ks_item_data = fetch_ks_data(driver,model_number_list)
    laox_item_data = fetch_laox_data(driver,model_number_list)
    matsuya_item_data = fetch_matsuya_data(driver,model_number_list)
    driver.quit()
    
    ks_laox_matsuya_cal_profit(ks_item_data,laox_item_data,matsuya_item_data,amazon_price_url_list)
    
def fetch_nojima_yamada_yodobashi_data(driver,model_number_list,amazon_price_url_list):
    nojima_item_data = fetch_nojima_data(driver,model_number_list)
    yamada_item_data = fetch_yamada_data(driver,model_number_list)
    yodobashi_item_data = fetch_yodobashi_data(driver,model_number_list)
    driver.quit()
    
    nojima_yamada_yodobashi_cal_profit(nojima_item_data,yamada_item_data,yodobashi_item_data,amazon_price_url_list)



def main():
    model_number_list = load_model_number()
    amazon_price_url_list = fetch_amaozn_price_url()
    driver = start_chrome()

    p0 = multiprocessing.Process(target=fetch_biccamera_edion_kojima_data,args=(driver,model_number_list,amazon_price_url_list))
    p1 = multiprocessing.Process(target=fetch_ks_laox_matsuya_data,args=(driver,model_number_list,amazon_price_url_list))
    p2 = multiprocessing.Process(target=fetch_nojima_yamada_yodobashi_data,args=(driver,model_number_list,amazon_price_url_list))
    
    # プロセス開始
    p0.start()
    p1.start()
    p2.start()
    
    # プロセス終了待ち合わせ
    p0.join()
    p1.join()
    p2.join()
    
    join_csv()
    
    
    
    
if __name__ == "__main__":
    freeze_support()
    main()