import requests
from config import open_weather_token, tg_token
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

bot = Bot(token=tg_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(
        "Привет, я бот от Xolonvr'a! Ты можешь написать мне название своего города, и я скину тебе прогноз погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={open_weather_token}&q={message.text}")
        data = r.json()
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        feels_like_c = data["current"]["feelslike_c"]
        wind = data["current"]["wind_kph"]
        precip_mm = data["current"]["precip_mm"]
        pressure_mb = data["current"]["wind_kph"]
        cur_time = data["location"]["localtime"]
        location = data["location"]["name"]
        await message.reply(f"Текущее время: {cur_time}\n Город: {location}"
                            f"Температура: {temp} по цельсии\n"
                            f"Чувствуется как: {feels_like_c} по цельсии\n"
                            f"Влажность воздуха: {humidity}%\n"
                            f"Ветер движется со скоростью {wind} км/час\n"
                            f"Количество осадков {precip_mm} мм\n"
                            f"Давление {pressure_mb} милибар\n"
                            f"Хорошего дня!")

    except Exception:
        await message.reply("Проверьте название города")


if __name__ == "__main__":
    executor.start_polling(dp)
