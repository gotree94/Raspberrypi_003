import tkinter as tk
from tkinter import ttk, messagebox
import threading
import json
import urllib.request

IPAPI_URL = "https://ipapi.co/json/"

FIELDS = [
    ("IP", "ip"),
    ("City", "city"),
    ("Region", "region"),
    ("Country", "country_name"),
    ("Country Code", "country"),
    ("Latitude", "latitude"),
    ("Longitude", "longitude"),
    ("Org/ISP", "org"),
    ("Timezone", "timezone"),
]

def fetch_ip_info(timeout=10):
    req = urllib.request.Request(IPAPI_URL, headers={"User-Agent": "python-ip-gui"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8"))

class IPInfoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IP & Location (ipapi)")
        self.geometry("460x340")
        self.resizable(False, False)

        outer = ttk.Frame(self, padding=16)
        outer.pack(fill="both", expand=True)

        title = ttk.Label(outer, text="Public IP & Geo (ipapi.co)", font=("Segoe UI", 12, "bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

        self.btn = ttk.Button(outer, text="Refresh", command=self.on_refresh)
        self.btn.grid(row=0, column=2, sticky="e")

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(outer, textvariable=self.status_var).grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 8))

        self.value_vars = {}
        for i, (label, key) in enumerate(FIELDS, start=2):
            ttk.Label(outer, text=label, width=14).grid(row=i, column=0, sticky="w", pady=4)
            v = tk.StringVar(value="-")
            self.value_vars[key] = v
            entry = ttk.Entry(outer, textvariable=v, width=40)
            entry.grid(row=i, column=1, columnspan=2, sticky="ew", pady=4)

        for c in range(3):
            outer.columnconfigure(c, weight=1)

        self.after(200, self.on_refresh)

    def on_refresh(self):
        self.btn.config(state="disabled")
        self.status_var.set("Fetching...")
        threading.Thread(target=self._fetch_and_update, daemon=True).start()

    def _fetch_and_update(self):
        try:
            data = fetch_ip_info()
            self.after(0, lambda: self._update_fields(data))
        except Exception as e:
            self.after(0, lambda: self._handle_error(e))

    def _update_fields(self, data: dict):
        for _, key in FIELDS:
            self.value_vars[key].set(str(data.get(key, "-")))
        self.status_var.set("Done")
        self.btn.config(state="normal")

    def _handle_error(self, e: Exception):
        self.status_var.set("Error")
        self.btn.config(state="normal")
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = IPInfoApp()
    app.mainloop()