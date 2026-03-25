import requests

def get_weather(lat: float, lon: float, tz: str = "Asia/Seoul"):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation"],
        "daily": ["weathercode", "temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": tz
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

data = get_weather(37.5665, 126.9780)

cw = data["current_weather"]
print(f"Temperature: {cw['temperature']}°C  Wind speed: {cw['windspeed']} m/s  Weather code: {cw['weathercode']}  Time: {cw['time']}")

daily = data["daily"]
print(f"Today max/min: {daily['temperature_2m_max'][0]} / {daily['temperature_2m_min'][0]} °C")
print(f"Total precipitation today: {daily['precipitation_sum'][0]} mm")

for t, temp in list(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))[:5]:
    print(t, temp, "°C")
