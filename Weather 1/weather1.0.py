import requests
import json
import os
from datetime import datetime, timedelta

LATITUDE = 53.3498
LONGITUDE = -6.2603
CACHE_FILE = "../Rain forecast/weather_cache.json"


class WeatherForecast:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def get_weather_from_api(self, date):
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

            result = response.json()

            if (
                "daily" in result
                and "precipitation_sum" in result["daily"]
                and len(result["daily"]["precipitation_sum"]) > 0
            ):
                return result["daily"]["precipitation_sum"][0]

            return None

        except requests.RequestException:
            return None

    def __getitem__(self, date):
        if date not in self.data:
            self.data[date] = self.get_weather_from_api(date)
            self.save_data()

        return self.data[date]

    def __setitem__(self, date, weather):
        self.data[date] = weather
        self.save_data()

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for item in self.data.items():
            yield item


def main():
    weather_forecast = WeatherForecast(CACHE_FILE)

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

    precipitation = weather_forecast[search_date]

    if precipitation is None or precipitation < 0:
        print("I don't know")
    elif precipitation == 0:
        print("It will not rain")
    else:
        print(f"It will rain ({precipitation} mm)")

    print("\nSaved forecasts:")
    for date, weather in weather_forecast.items():
        print(date, "->", weather)


if __name__ == "__main__":
    main()