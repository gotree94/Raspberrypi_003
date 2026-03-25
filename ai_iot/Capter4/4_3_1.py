import json
import sys
import urllib.request

URL = "https://ipapi.co/json/"

def fetch_ip_info():
    req = urllib.request.Request(URL, headers={"User-Agent": "python-ip-check"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8"))

def main():
    try:
        info = fetch_ip_info()
        fields = [
            ("IP", info.get("ip")),
            ("City", info.get("city")),
            ("Region", info.get("region")),
            ("Country", f"{info.get('country_name')} ({info.get('country')})"),
            ("Latitude", info.get("latitude")),
            ("Longitude", info.get("longitude")),
            ("Org/ISP", info.get("org")),
            ("Timezone", info.get("timezone")),
        ]
        width = max(len(k) for k, _ in fields)
        for k, v in fields:
            print(f"{k:<{width}} : {v}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
