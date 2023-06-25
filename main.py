import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={open_weather_token}&q={city}")
        data = r.json()
        pprint(data)
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        feels_like_c = data["current"]["feelslike_c"]
        wind = data["current"]["wind_kph"]
        precip_mm = data["current"]["precip_mm"]
        pressure_mb = data["current"]["wind_kph"]
        cur_time = data["location"]["localtime"]
        location = data["location"]["name"]
        print(f"Текущая время: {cur_time}"
              f"Температура: {temp} по цельсии"
              f"Чувствуется как: {feels_like_c} по цельсии"
              f"Влажность воздуха: {humidity}%"
              f"Ветер движется со скоростью {wind} км/час"
              f"Количество осадков {precip_mm} мм"
              f"Давление {pressure_mb} милибар")


    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
