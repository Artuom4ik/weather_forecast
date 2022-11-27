import requests 


params = {
    "qnTM": "",
    "lang": "ru"
    }
locations = ["Аэропорт Шереметьево", "Лондон", "Череповец"]
for location in locations:
    url = f'https://wttr.in/{location}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
