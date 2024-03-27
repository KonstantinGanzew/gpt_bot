import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKKEN_FOR_PROXY_API')
URL = os.getenv('URL')
URL_OPENAI = os.getenv('URL_OPENAI')
MODELS = os.getenv('MODELS')
ID_TG_ADMINS = list(map(int, os.getenv('ID_TG_ADMINS').split(' ')))
BOT_TOKEN = os.getenv('BOT_TOKEN')
