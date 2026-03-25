import tkinter as tk
from tkinter import ttk, messagebox
import threading
import requests

API_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather(lat: float, lon: float, tz: str = "Asia/Seoul"):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": ["temperature_2m"],
        "daily": ["weathercode", "temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": tz
    }
    r = requests.get(API_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather GUI")
        self.geometry("420x300")
        self.resizable(False, False)

        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="Latitude").grid(row=0, column=0, sticky="w", padx=(0,8), pady=(0,8))
        self.lat_var = tk.StringVar(value="37.5665")
        ttk.Entry(container, textvariable=self.lat_var, width=18).grid(row=0, column=1, sticky="w")

        ttk.Label(container, text="Longitude").grid(row=1, column=0, sticky="w", padx=(0,8), pady=(0,8))
        self.lon_var = tk.StringVar(value="126.9780")
        ttk.Entry(container, textvariable=self.lon_var, width=18).grid(row=1, column=1, sticky="w")

        self.btn = ttk.Button(container, text="Get Weather", command=self.on_get_weather)
        self.btn.grid(row=2, column=0, columnspan=2, pady=(12,8), sticky="ew")

        sep = ttk.Separator(container)
        sep.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(8,8))

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(container, textvariable=self.status_var).grid(row=4, column=0, columnspan=2, sticky="w")

        self.out_current = tk.Text(container, height=4, width=44, state="disabled")
        self.out_current.grid(row=5, column=0, columnspan=2, pady=(8,4), sticky="nsew")

        self.out_daily = tk.Text(container, height=3, width=44, state="disabled")
        self.out_daily.grid(row=6, column=0, columnspan=2, pady=(4,0), sticky="nsew")

        for i in range(2):
            container.columnconfigure(i, weight=1)

    def on_get_weather(self):
        try:
            lat = float(self.lat_var.get().strip())
            lon = float(self.lon_var.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Invalid latitude/longitude")
            return
        self.btn.config(state="disabled")
        self.status_var.set("Fetching...")
        threading.Thread(target=self._fetch_and_update, args=(lat, lon), daemon=True).start()

    def _fetch_and_update(self, lat: float, lon: float):
        try:
            data = fetch_weather(lat, lon, "Asia/Seoul")
            cw = data["current_weather"]
            daily = data.get("daily", {})
            cur_text = (
                f"Time: {cw.get('time','')}\n"
                f"Temperature: {cw.get('temperature','')} °C\n"
                f"Wind: {cw.get('windspeed','')} m/s\n"
                f"Weather code: {cw.get('weathercode','')}"
            )
            day_text = ""
            if daily:
                tmax = daily.get("temperature_2m_max", [""])[0]
                tmin = daily.get("temperature_2m_min", [""])[0]
                prcp = daily.get("precipitation_sum", [""])[0]
                wcode = daily.get("weathercode", [""])[0]
                day_text = f"Today Max/Min: {tmax} / {tmin} °C\nPrecipitation: {prcp} mm\nWeather code: {wcode}"
            self.after(0, lambda: self._update_outputs(cur_text, day_text, "Done"))
        except Exception as e:
            self.after(0, lambda: self._handle_error(e))

    def _update_outputs(self, cur_text: str, day_text: str, status: str):
        self._set_text(self.out_current, cur_text)
        self._set_text(self.out_daily, day_text)
        self.status_var.set(status)
        self.btn.config(state="normal")

    def _handle_error(self, e: Exception):
        self.status_var.set("Error")
        messagebox.showerror("Error", str(e))
        self.btn.config(state="normal")

    def _set_text(self, widget: tk.Text, content: str):
        widget.config(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", content)
        widget.config(state="disabled")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
