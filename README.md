# 🌦️ Terminal Weather App (Python)

A simple terminal-based weather application built with Python that fetches real-time weather data using the OpenWeather API.

This is my first GitHub project, and it's currently a **work in progress** as I continue improving functionality, structure, and user experience.

---

## 🚀 Features (Current)

* 🌍 Search weather by city name
* 📍 Automatically fetches geographic coordinates using OpenWeather Geocoding API
* 🌡️ Displays:

  * Current weather description
  * Current temperature
  * Daily high and low temperatures
* 🔁 Input validation for incorrect or misspelled cities

---

## 🛠️ Tech Stack

* **Python**
* **Requests** (API calls)
* **python-dotenv** (environment variable management)
* **OpenWeather API**

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/axladomdza/OpenWeatherAPI.git
   cd weather-app
   ```

2. Install dependencies:

   ```bash
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the root directory:

   ```env
   API_KEY=Your own API KEY from the OpenWeather Website
   ```

4. Run the app:

   ```bash
   python RD_weatherapp.py
   ```

---

## 🔑 API Setup

* Get a free API key from: https://openweathermap.org/api
* Add it to your `.env` file as shown above

---

## 🧠 How It Works

1. User inputs a city name
2. App uses the **Geocoding API** to fetch latitude & longitude
3. Coordinates are passed into the **Weather API**
4. Weather data is parsed and displayed in the terminal

---

## 📌 Roadmap (What I'm Building Next)

* [-] Convert temperature units (F ↔ C)
* [ ] Add forecast (multi-day weather)
* [ ] Improve error handling (API failures, edge cases)
* [ ] Refactor into modular structure (separate files)
* [ ] Add CLI flags (e.g. `--city`, `--units`)
* [ ] Add caching to reduce API calls
* [ ] Package as a CLI tool (pip installable)

---

## ⚠️ Known Issues

* API always returns status 200 even for invalid cities (handled manually)
* Minimal exception handling (will improve)
* Output formatting is basic

---

## 🎯 Purpose

This project is part of my journey into software engineering and API-based applications. The goal is to:

* Learn how to work with real-world APIs
* Practice clean Python code structure
* Build projects that reflect practical, industry-relevant skills

---

## 🤝 Contributions

This is a personal learning project, but feedback and suggestions are welcome.

---

## 📄 License

MIT License (will be added)

---

