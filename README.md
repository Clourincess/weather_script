## Требования

- Python 3.7 или выше
- Аккаунт на [WeatherAPI.com](https://www.weatherapi.com/) для получения API ключа

## Установка

1. **Клонируйте репозиторий**

```bash
git clone https://github.com/Clourincess/weather_script
cd weather_script
```

2. **Установите зависимости**

```bash
pip install -r requirements.txt
```

3. **Настройте API ключ**

3.1. Зарегистрируйтесь на WeatherAPI.com, получите бесплатный API ключ.
3.2. создайте файл .env в корневой директории проекта и вставьте строку:

```bash
API_KEY=ваш_api_ключ
```

## Запуск

1. Из корневой папки проекта выполните

```bash
python weather.py название_города
```