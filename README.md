# Weather App

A simple Python CLI app that fetches weather data from OpenWeather API.

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file in the project root:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

5. Run the app:
   ```bash
   python weather.py "New Delhi"
   ```
