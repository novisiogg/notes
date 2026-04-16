import os
import json
import requests
from requests import RequestException
from dotenv import load_dotenv


class WeatherManager:
    def __init__(self, filename="weather.json"):
        self.research = {"cities": []}
        self.filename = filename

    def load_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.research = data

        except FileNotFoundError:
            print("File not found.")
            print("Initial setup..")
            with open(self.filename, "w") as f:
                self.research = {"cities": []}
                self.save_file()

    def save_file(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.research, f, indent=4)
                return f"Successfully saved data to {f.name}"

        except FileNotFoundError:
            print("File does not exist.")

    def get_response(self, city: str):
        base_url = "http://api.weatherapi.com/v1/forecast.json"
        payload = {"key": os.getenv("key"), "q": city}
        response = requests.get(base_url, params=payload)
        if response:
            data = response.json()
            city_name = data["location"]["name"]
            local_time = data["location"]["localtime"]
            temp_c = data["current"]["temp_c"]
            feels_like = data["current"]["feelslike_c"]
            city_data = {
                "city": city_name,
                "local time": local_time,
                "temperature in celsius": temp_c,
                "feels like": feels_like,
            }
            print(
                f"Currently in {city_name} it's {local_time}, the temperature in celsius is {temp_c} and it feels like {feels_like}"
            )
            self.research["cities"].append(city_data)
            self.save_file()
        else:
            print(f"{city} does not exist.")
