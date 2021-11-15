import pandas as pd
import re
from sp_api.api import ProductFees
from sp_api.base.marketplaces import Marketplaces
from common.config import *



# df = pd.read_csv('Product_Finder.2021_11_7.products.csv',usecols=['Buy Box 🚚: 現在価格','ASIN'])
# df = df.fillna('None')

# df = df.values.tolist()
# price_asin_list = []
# for price_asin in df:
#     price = price_asin[0]
#     price = re.sub(r'\D', '', price) 
#     price_asin_list.append([price,price_asin[1]])
# print(price_asin_list)

credentials=dict(
        refresh_token=SP_API_REFRESH_TOKEN,
        lwa_app_id=LWA_APP_ID,
        lwa_client_secret=LWA_CLIENT_SECRET,
        aws_secret_key=SP_API_SECRET_KEY,
        aws_access_key=SP_API_ACCESS_KEY,
        role_arn=SP_API_ROLE_ARN,
    )

fees_data = ProductFees(Marketplaces.JP,credentials=credentials).get_product_fees_estimate_for_asin(asin='B078HFVMR8',price=3000,currency='JPY',is_fba=True)

print(fees_data)