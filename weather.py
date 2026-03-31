import requests
from dotenv import load_dotenv
import os
import sys

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"

def get_current_weather(city):
    params = {
        'q': city,
        'key': API_KEY
    }
    
    try:
        response = requests.get(f"{BASE_URL}/current.json", params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print(f"Нет сети. Проверьте интернет-соединение")
        return None
    except requests.exceptions.Timeout:
        print(f"Превышено время ожидания ответа от сервера")
        return None
    except requests.exceptions.HTTPError as e:
        if hasattr(response, 'status_code') and response.status_code == 400:
            print(f"Город '{city}' не найден. Проверьте правильность написания города и повторите снова")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None

def display_weather(data):
    if not data:
        return
    try:
        current = data['current']
        condition = current['condition']
        print(f"Температура: {current['temp_c']}°C, {condition['text']}")
    except KeyError as e:
        print(f"Неожиданный формат данных от API ({e})")
    except Exception as e:
        print(f"Ошибка при отображении погоды: {e}")

def main():
    if not API_KEY:
        print(f"API ключ не найден. Убедитесь, что переменная API_KEY задана в файле .env")
        return
    
    if len(sys.argv) != 2:
        print(f"Проверьте правильность ввода команды: python weather.py название_города")
        return
    
    city = sys.argv[1].strip()
    
    if not city:
        print(f"Название города не может быть пустым")
        return
    
    weather_data = get_current_weather(city)
    
    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()