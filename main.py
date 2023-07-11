from pathlib import Path
from sdk import DataGolfSDK
import os
from dotenv import load_dotenv


# load api key from .env file or pass it below

load_dotenv(Path(__file__).parent.joinpath(".env").as_posix())

# or paste it in "YOUR_API_TOKEN" below if you dont want to create a .env file
api_token = os.environ.get("apikey", "YOUR_API_TOKEN")

dg = DataGolfSDK(api_token)

# get all field updates for pga
my = dg.get_field_updates("pga")

# get all field updates for pga in csv format
my = dg.get_field_updates("pga", "csv")
