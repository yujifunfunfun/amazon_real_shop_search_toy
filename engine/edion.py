import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
from common.csv import *
from common.logger import set_logger
import pandas as pd
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.chromedriver import *

logger = set_logger(__name__)



def start_chrome():
    global option

    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option = Options()                         
    # option.add_argument('--headless') 
    option.add_argument('--lang=ja-JP')
    option.add_argument('--user-agent=' + UA)
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--ignore-ssl-errors')
    option.add_argument("window-size=900,600")
    #ここで、バージョンなどのチェックをする
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)   

def fetch_edion_data(driver,model_number_list):
    wait = WebDriverWait(driver, 20)
    driver.get('https://www.edion.com/index.html?_rt=8ViuLsibTqRrxJUXf66gbngY9Y0mKRafyrLqM6Mo7c')
    element = wait.until(EC.presence_of_all_elements_located)
    edion_item_data = []
    for model_number in model_number_list:
        print(model_number)
        # 商品ページへ遷移
        if model_number != 'None':
            try:
                driver.find_element_by_id('searchtext').clear()
                driver.find_element_by_id('searchtext').send_keys(model_number)
                driver.find_element_by_class_name('hd_submit').click()
                element = wait.until(EC.presence_of_all_elements_located)
                name =driver.find_element_by_class_name('item').text
                price = driver.find_element_by_class_name('price2').text
                price = re.sub(r'\D', '', price) 
                url = driver.find_element_by_xpath('//*[@id="resultBox"]/ul/li/p[2]/a').get_attribute('href')
                p = r'p_cd=(.*)&'
                p_cd = re.search(p, url).group(1)
                q = r'_rt=(.*)&'
                _rt = re.search(q, url).group(1)
                stock_url = f'https://www.edion.com/stocklist.html?p_cd={p_cd}&_rt={_rt}&prefecture=13&searchBtnFlg=1'
            except Exception as e:
                logger.info(e)
                name = 'None'
                price = 999999
                url = 'None'
                stock_url = 'None'
        else:
            name = 'None'
            price = 999999
            url = 'None'
            stock_url = 'None'
        edion_item_data.append([name,price,url,stock_url])
        

    return edion_item_data

if __name__ == "__main__":
    start_chrome()
    fetch_edion_data()




        