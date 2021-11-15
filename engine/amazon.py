import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from common.logger import set_logger
logger = set_logger(__name__)
from sp_api.api import ProductFees
from sp_api.base.marketplaces import Marketplaces
from common.config import *
from common.csv import *
from time import sleep


credentials=dict(
        refresh_token=SP_API_REFRESH_TOKEN,
        lwa_app_id=LWA_APP_ID,
        lwa_client_secret=LWA_CLIENT_SECRET,
        aws_secret_key=SP_API_SECRET_KEY,
        aws_access_key=SP_API_ACCESS_KEY,
        role_arn=SP_API_ROLE_ARN,
    )

def cal_fba_fee(price,asin):
    try:
        fees_data = ProductFees(Marketplaces.JP,credentials=credentials).get_product_fees_estimate_for_asin(asin=asin,price=price,currency='JPY',is_fba=True)
        fba_fee = fees_data.payload.get('FeesEstimateResult').get('FeesEstimate').get('TotalFeesEstimate').get('Amount')
    except Exception as e:
        logger.info(e)
        fba_fee = 999999
    return fba_fee

def fetch_amaozn_price_url():
    buybox_asin_list = load_buybox_asin()
    amazon_price_url_list = []
    for buybox_asin in buybox_asin_list:
        try:
            buybox = buybox_asin[0]
            asin = buybox_asin[1]            
            url = f'https://www.amazon.co.jp/gp/product/{asin}'
            fba_fee = cal_fba_fee(buybox,asin)
            sleep(1)
            amazon_price = int(buybox) - int(fba_fee)
        except Exception as e:
            amazon_price = 0
            url = 'NOne'
        
        amazon_price_url_list.append([amazon_price,url])
        
    return amazon_price_url_list


if __name__ == "__main__":
    fetch_amaozn_price_url()