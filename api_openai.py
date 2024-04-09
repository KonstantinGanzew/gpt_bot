import requests as r
import json
from config import TOKEN, URL, URL_OPENAI, MODELS
from openai import OpenAI

HEADERS = {'Authorization': f'Bearer {TOKEN}'}

TEMPERATURE = 0.5
MAX_TOKENS = 1000
TOP_P = 1.0
FREQUENCY_PENALTY = 0.5
PRESENCE_PENALTY = 0.0

client = OpenAI(
    api_key=TOKEN,
    base_url=URL_OPENAI,
)

async def balance() -> str:
    return r.get(url=f'{URL}proxyapi/balance', headers=HEADERS).json()['balance']

async def get_messages_list(ask: list) -> str: 
    answer = json.loads(client.chat.completions.create(
        model = MODELS,
        messages=ask,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY
    ).json())['choices'][0]['message']
    ask.append({'role': answer['role'], 'content': answer['content']})
    return ask
