import time
import requests


def main():
    city_lat = 44.89
    city_lon = 37.31
    app_id = 'your app_id'
    time_delta = int(time.time()) + 432000
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/onecall",
                           params={'lat': city_lat, 'lon': city_lon, 'units': 'metric',
                                   'lang': 'ru', 'exclude': 'minutely,hourly,alerts',
                                   'APPID': app_id})
        data = res.json()
        for i in data['daily']:
            if time_delta >= i['dt']:
                morn += i['temp']['morn']
                max_temp.append(i['temp']['max'])
        print(f'average_morn: {morn/5}')
        print(f'average_max: {max(max_temp)}')
    except Exception as e:
        print("Exception (forecast):", e)
