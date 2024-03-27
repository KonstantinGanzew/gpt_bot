import os
import csv
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('TOKKEN_FOR_PROXY_API')
URL = os.getenv('URL')
URL_OPENAI = os.getenv('URL_OPENAI')
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

cols = ['id', 'object', 'created', 'owned_by']

response = requests.get(url=f'{URL}openai/v1/models', headers=HEADERS).json()['data']

with open('models.csv', 'w') as f: 
    wr = csv.DictWriter(f, fieldnames = cols)
    wr.writeheader()
    wr.writerows(response)