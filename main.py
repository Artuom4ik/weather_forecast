import requests 


weather = {
    "q": "",
    "n": "",
    "T": "",
    "lang": "ru",
    "M": ""
    }
locations = ["Аэропорт Шереметьево", "Лондон", "Череповец"]
for location in locations:
    url = f'https://wttr.in/{location}'
    response = requests.get(url, params=weather)
    response.raise_for_status()
    print(response.text)
