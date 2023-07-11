from sdk import DataGolfSDK
import os
from dotenv import load_dotenv


# load api key from .env file or pass it below
if load_dotenv() == True:
    api_token = os.getenv("apikey")
else:
    api_token = "YOUR_API_TOKEN"
dg = DataGolfSDK(api_token)


# get all field updates for pga
my = dg.get_field_updates("pga")
print(my)
