import tkinter as tk
from tkinter import ttk

class WeatherTestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather GUI (Test)")
        self.geometry("420x300")
        self.resizable(False, False)

        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="Latitude").grid(row=0, column=0, sticky="w", padx=(0,8), pady=(0,8))
        self.lat_var = tk.StringVar(value="37.5665")
        ttk.Entry(container, textvariable=self.lat_var, width=20).grid(row=0, column=1, sticky="w")

        ttk.Label(container, text="Longitude").grid(row=1, column=0, sticky="w", padx=(0,8), pady=(0,8))
        self.lon_var = tk.StringVar(value="126.9780")
        ttk.Entry(container, textvariable=self.lon_var, width=20).grid(row=1, column=1, sticky="w")

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(container, textvariable=self.status_var).grid(row=3, column=0, columnspan=2, sticky="w", pady=(12,0))

        action = ttk.Button(container, text="Test GUI", command=self.on_test)
        action.grid(row=2, column=0, columnspan=2, pady=(12,0), sticky="ew")

        for i in range(2):
            container.columnconfigure(i, weight=1)

    def on_test(self):
        lat = self.lat_var.get().strip()
        lon = self.lon_var.get().strip()
        self.status_var.set(f"Test OK — lat={lat}, lon={lon}")

if __name__ == "__main__":
    app = WeatherTestApp()
    app.mainloop()
