"""
Использование:

    $ curl wttr.in          # текущее местоположение
    $ curl wttr.in/svo      # погода в аэропорту Шереметьево (код ICAO: SVO)

Поддерживаемые типы местоположений:

    /paris                  # город
    /~Eiffel+tower          # любое местоположение
    /Москва                 # юникодное имя любого местоположения на любом языке
    /muc                    # код аэропорта ICAO (3 буквы)
    /@stackoverflow.com     # доменное имя
    /94107                  # почтовый индекс (только для США)
    /-78.46,106.79          # GPS-координаты

Специальные условные местоположения:

    /moon                   # Фаза Луны (добавьте ,+US или ,+France для города Moon в США/Франции)
    /moon@2016-10-25        # Фаза Луны для указанной даты (@2016-10-25)

Единицы измерений:

    ?m                      # метрические (СИ) (используются везде кроме США)
    ?u                      # USCS (используются в США)
    ?M                      # показывать скорость ветра в м/с

Опции отображения:

    ?0                      # только текущая погода
    ?1                      # погода сегодня + 1 день
    ?2                      # погода сегодня + 2 дня
    ?n                      # узкая версия (только день и ночь)
    ?q                      # тихая версия (без текста "Прогноз погоды")
    ?Q                      # сверхтихая версия (без "Прогноз погоды", нет названия города)
    ?T                      # отключить терминальные последовательности (без цветов)

PNG-опции:

    /paris.png              # сгенерировать PNG-файл
    ?p                      # добавить рамочку вокруг
    ?t                      # transparency=150 (прозрачность 150)
    transparency=...        # прозрачность от 0 до 255 (255 = не прозрачный)

Опции можно комбинировать:

    /Paris?0pq
    /Paris?0pq&lang=fr
    /Paris_0pq.png          # в PNG-запросах опции указываются после _
    /Rome_0pq_lang=it.png   # длинные опции разделяются знаком подчёркивания _

Локализация:

    $ curl fr.wttr.in/Paris
    $ curl wttr.in/paris?lang=fr
    $ curl -H "Accept-Language: fr" wttr.in/paris

Поддерживаемые языки:

    am ar af be bn ca da de el et fr fa gl hi hu ia id it lt mg nb nl oc pl pt-br ro ru ta tr th uk vi zh-cn zh-tw (поддерживаются)
    az bg bs cy cs eo es eu fi ga hi hr hy is ja jv ka kk ko ky lv mk ml mr nl fy nn pt pt-br sk sl sr sr-lat sv sw te uz zh zu he (в процессе)

Специальные страницы:

    /:help                  # показать эту страницу
    /:bash.function         # показать рекомендованную функцию wttr()
    /:translation           # показать список переводчиков wttr.in

"""

import requests


city = input('Укажите город или место: \n')

url = f'https://wttr.in/{city}?1nTMqm&lang=ru'

res = requests.get(url, timeout=5)

print(res.text)
