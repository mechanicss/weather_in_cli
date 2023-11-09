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


def get_status_response(res):

    if res.ok:
        status = 'ok'
    else:
        status = 'err'
        print('Страница не существует\n')

    return status


def get_weather():

    for city in city_list:

        url = f'https://wttr.in/{city}'

        res = requests.get(url, params=params, timeout=5)

        status = get_status_response(res)

        if status == 'ok':
            print(res.text)


if __name__ == '__main__':
    get_weather()
