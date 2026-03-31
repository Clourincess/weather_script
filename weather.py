import requests
import os
from dotenv import load_dotenv

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
        print("Нет сети. Проверьте интернет-соединение")
        return None
    except requests.exceptions.RequestException as e:
        return None

def display_weather(data):
    if not data:
        return

    current = data['current']
    condition = current['condition']
    
    print(f"Температура: {current['temp_c']} °C, {condition['text']}")

def main():
    if not API_KEY:
        return
    
    while True:
        try:
            input_city = input("\nВведите город, в котором хотите узнать текущую погоду: ").strip()
        
            if not input_city:
                print("Пожалуйста, введите название города")
                continue
            
            weather_data = get_current_weather(input_city)
            
            if weather_data:
                display_weather(weather_data)
            else:
                print(f"Не удалось найти город '{input_city}'")
                
        
        except Exception as e:
            print(f"Возникла неожиданная ошибка. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
