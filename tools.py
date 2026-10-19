import os
import requests
from dotenv import load_dotenv

load_dotenv()




API_KEY = os.environ.get('API_KEY')
URL = os.environ.get('URL')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
WEATHER_URL = os.environ.get('WEATHER_URL')

print('Key loaded:', bool(WEATHER_API_KEY))
print('Key length:', len(WEATHER_API_KEY) if WEATHER_API_KEY else 0)

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

    rate = data.get('rates', {}).get(to_currency)
    if rate is None:
        return f'Could not reach {from_currency} to {to_currency} - is not valid currency '

    return f'1 {from_currency} = {rate} {to_currency}'

def get_weather(city):
    city = city.lower()
    try:
        response = requests.get(WEATHER_URL, params={
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
        })
    except requests.RequestException :
        return f'Could not reach weather for {city}'

    data = response.json()
    # if response.status_code != 200 or not data.get('success', True):
    #     return f'Could not reach weather for {city} result of cod is not 200'

    if response.status_code != 200:
        print('DEBUG STATUS:', response.status_code)
        print('DEBUG API RESPONSE:', data)
        return f'Could not get weather for {city}'

    city = data['name']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    weather_list = data.get('weather', [])

    if not weather_list:
        return f'Weather information is unavailable for {city}'

    weather = weather_list[0].get('description', 'Unknown')

    return (
        f"The weather in {city} is:\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind speed: {wind} m/s\n"
        f"Description: {weather}"
    )


TOOLS = {
    'get_exchange_rate': get_exchange_rate,
    'get_weather': get_weather,

}
