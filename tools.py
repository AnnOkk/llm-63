import os

import requests
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.environ.get('API_KEY')
URL = os.environ.get('URL')

if not API_KEY:
    raise RuntimeError('API_KEY not set')


def get_exchange_rate(from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    try:
        response = requests.get(URL, params={
            'base': from_currency,
            'symbols': to_currency,

        },headers={'apikey': API_KEY})
    except requests.RequestException :
        return f'Could not reach {from_currency} to {to_currency} '

    data = response.json()
    if response.status_code != 200 or not data.get('success', True):
        return f'Could not reach {from_currency} to {to_currency} result of success is not true'
    # rate = data['rate'][to_currency]
    rate = data.get('rates', {}).get(to_currency)
    if rate is None:
        return f'Could not reach {from_currency} to {to_currency} - is not valid currency '

    return f'1 {from_currency} = {rate} {to_currency}'


TOOLS = {
    'get_exchange_rate': get_exchange_rate,

}
