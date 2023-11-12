import requests


city_list = [
    'Лондоне',
    'Шереметьево',
    'череповец',
]

params = {
    'n': '',
    'T': '',
    'M': '',
    'q': '',
    'lang': 'ru',
}


def get_weather():

    for city in city_list:

        url = f'https://wttr.in/{city}'

        res = requests.get(url, params=params, timeout=5)

        res.raise_for_status()

        print(res.text)


if __name__ == '__main__':
    get_weather()
