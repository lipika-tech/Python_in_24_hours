"""
Lab 5 · Real-Time Data Analytics Dashboard — STARTER          (~45–60 minutes)

Goal: consume a public API, process the JSON with Pandas, analyze it, and build an
interactive Streamlit dashboard.

Run from this folder (and keep it running while you work — save the file to refresh):
    streamlit run lab5_dashboard_starter.py

Work through TODO 1 → TODO 7 in order. The app runs at every step and tells you
which TODO comes next. Reuse your code from Labs 1–4!

Definition of done
  [ ] live data from the API (with a friendly fallback if it fails)
  [ ] a clean DataFrame with real datetimes
  [ ] widgets that change what is shown (city, variable, days)
  [ ] at least 3 metric cards
  [ ] at least 2 labelled charts
  [ ] a data table with a CSV download
Stretch: headline insight sentence · compare cities · refresh button
"""
import json
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

URL = "https://api.open-meteo.com/v1/forecast"
SAMPLE_DIR = Path(__file__).resolve().parents[1] / "sample_data"

CITIES = {
    "Delhi": (28.61, 77.21),
    "Mumbai": (19.08, 72.88),
    "Bengaluru": (12.97, 77.59),
    "Kolkata": (22.57, 88.36),
}
VARIABLES = {  # API field -> (friendly name, unit)
    "temperature_2m": ("Temperature", "°C"),
    "relative_humidity_2m": ("Humidity", "%"),
    "precipitation": ("Rain", "mm"),
    "wind_speed_10m": ("Wind speed", "km/h"),
}

st.set_page_config(page_title="Real-Time Weather Dashboard", page_icon="🌦", layout="wide")


def load_sample(city):
    """Offline backup: the saved sample for a city (same shape as the real API response)."""
    return json.loads((SAMPLE_DIR / f"weather_{city.lower()}.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# TODO 1 · COLLECT: fetch the forecast for a city
#   - build params: latitude, longitude,
#       current="temperature_2m,relative_humidity_2m,wind_speed_10m",
#       hourly=",".join(VARIABLES), timezone="Asia/Kolkata"
#   - requests.get(URL, params=params, timeout=10), then r.raise_for_status() and r.json()
#   - if anything fails (requests.RequestException or ValueError), use load_sample(city)
#     and set source to something like "offline sample"
#   - return data, source, datetime.now()
#   - add @st.cache_data(ttl=600) above the function so we don't call the API on every click
# ---------------------------------------------------------------------------
def fetch_weather(city):
    lat, lon = CITIES[city]
    return None, None, None          # ← replace this line


# ---------------------------------------------------------------------------
# TODO 2 · PROCESS: hourly JSON → DataFrame
#   - pd.DataFrame(data["hourly"]) and convert "time" with pd.to_datetime
# ---------------------------------------------------------------------------
def to_dataframe(data):
    return None                      # ← replace this line


# ---------------------------------------------------------------------------
# TODO 3 · Sidebar widgets
#   city is done for you. Add:
#   - var  = st.sidebar.selectbox("Variable", list(VARIABLES),
#                                 format_func=lambda v: VARIABLES[v][0])
#   - days = st.sidebar.slider("Days to show", 1, 7, 7)
# ---------------------------------------------------------------------------
st.sidebar.header("⚙️ Controls")
city = st.sidebar.selectbox("City", list(CITIES))
var = "temperature_2m"               # ← replace with a selectbox
days = 7                             # ← replace with a slider
name, unit = VARIABLES[var]

st.title(f"🌦 Real-Time Weather Dashboard · {city}")

data, source, fetched_at = fetch_weather(city)
if data is None:
    st.info("👉 Start with **TODO 1**: make `fetch_weather()` return the API data.")
    st.stop()

st.caption(f"Source: Open-Meteo ({source}) · fetched {fetched_at:%d %b %Y, %H:%M}")

df = to_dataframe(data)
if df is None:
    st.info("👉 Next: **TODO 2** — turn `data['hourly']` into a DataFrame.")
    with st.expander("Peek at the raw JSON"):
        st.json({k: v for k, v in data.items() if k != "hourly"})
    st.stop()

# keep only the first `days` days
df = df[df["time"] < df["time"].min() + pd.Timedelta(days=days)]
series = df[var]

# ---------------------------------------------------------------------------
# TODO 4 · Metric cards (st.columns + .metric)
#   Show at least 3, for example: current temperature (data["current"]["temperature_2m"]),
#   current humidity, and the max / average of the selected variable (series.max(), series.mean()).
# ---------------------------------------------------------------------------
st.info("👉 **TODO 4**: add metric cards here.")

# ---------------------------------------------------------------------------
# TODO 5 · Chart 1: hourly trend of the selected variable
#   st.subheader(...) and st.line_chart(df.set_index("time")[var])
# ---------------------------------------------------------------------------
st.info("👉 **TODO 5**: add a line chart of the selected variable over time.")

# ---------------------------------------------------------------------------
# TODO 6 · ANALYZE + Chart 2: daily summary
#   daily = df.resample("D", on="time")[var].agg(["min", "max", "mean"]).round(1)
#   show it with st.bar_chart(daily["max"]) and st.dataframe(daily)
# ---------------------------------------------------------------------------
st.info("👉 **TODO 6**: add the daily summary table and a bar chart.")

# ---------------------------------------------------------------------------
# TODO 7 · Data table + CSV download
#   st.dataframe(df) and
#   st.download_button("Download CSV", df.to_csv(index=False), file_name=f"{city}.csv")
# ---------------------------------------------------------------------------
st.info("👉 **TODO 7**: show the data table and a download button.")

# ---------------------------------------------------------------------------
# ⭐ STRETCH GOALS
#   a) Headline insight: find the peak row (df.loc[series.idxmax()]) and show
#      st.success(f"{name} peaks at ... on ...")
#   b) Compare cities: st.sidebar.multiselect, fetch each city, build one DataFrame with a
#      column per city, and st.line_chart it (use st.tabs to keep the page tidy)
#   c) Refresh button: if st.sidebar.button("Refresh"): st.cache_data.clear(); st.rerun()
#   d) Show a warning when you're on offline sample data
# ---------------------------------------------------------------------------
