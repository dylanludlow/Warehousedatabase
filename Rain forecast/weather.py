import requests
import json
import os
from datetime import datetime, timedelta

# Coordinates (Dublin, Ireland)
LATITUDE = 53.3498
LONGITUDE = -6.2603

CACHE_FILE = "../weather_cache.json"


def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file, indent=4)


def get_weather(date):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        f"&daily=precipitation_sum"
        f"&timezone=Europe%2FLondon"
        f"&start_date={date}"
        f"&end_date={date}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if (
            "daily" in data
            and "precipitation_sum" in data["daily"]
            and len(data["daily"]["precipitation_sum"]) > 0
        ):
            return data["daily"]["precipitation_sum"][0]
        else:
            return None

    except requests.RequestException:
        print("Error connecting to the weather service.")
        return None


def main():
    user_input = input(
        "Enter a date (YYYY-MM-DD) or press Enter for tomorrow: "
    ).strip()

    if user_input == "":
        search_date = (
            datetime.today() + timedelta(days=1)
        ).strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(user_input, "%Y-%m-%d")
            search_date = user_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    cache = load_cache()

    if search_date in cache:
        print("Using saved result...")
        precipitation = cache[search_date]
    else:
        precipitation = get_weather(search_date)
        cache[search_date] = precipitation
        save_cache(cache)

    if precipitation is None or precipitation < 0:
        print("I don't know")
    elif precipitation == 0:
        print("It will not rain")
    else:
        print(f"It will rain ({precipitation} mm)")


if __name__ == "__main__":
    main()