import requests
import pandas as pd

def fetch_race_data_with_weather(year, openweather_api_key):
    """
    Fetches race details with weather information for a specific year.
    """
    race_url = f"http://api.jolpi.ca/ergast/f1/{year}/races"
    
    try:
        # Fetch race details
        race_response = requests.get(race_url)
        race_response.raise_for_status()
        race_data = race_response.json()

        # Extract races and initialize list for enriched data
        races = race_data['MRData']['RaceTable']['Races']
        enriched_data = []

        for race in races:
            lat = race['Circuit']['Location']['lat']
            lon = race['Circuit']['Location']['long']
            race_date = race['date']
            race_name = race['raceName']
            
            # Fetch weather data using OpenWeather API
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}&units=metric"
            weather_response = requests.get(weather_url)
            weather_response.raise_for_status()
            weather_data = weather_response.json()

            # Extract relevant weather details
            weather = weather_data.get('weather', [{}])[0].get('description', 'Unknown')
            temperature = weather_data.get('main', {}).get('temp', 'Unknown')
            humidity = weather_data.get('main', {}).get('humidity', 'Unknown')
            wind_speed = weather_data.get('wind', {}).get('speed', 'Unknown')
            rain = weather_data.get('rain', {}).get('1h', 'No rain')

            # Append enriched data
            enriched_data.append({
                "Race Name": race_name,
                "Date": race_date,
                "Latitude": lat,
                "Longitude": lon,
                "Weather": weather,
                "Temperature (°C)": temperature,
                "Humidity (%)": humidity,
                "Wind Speed (m/s)": wind_speed,
                "Rain (mm)": rain,
                "Year": year  # Add the year to the data
            })

        return enriched_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching race or weather data for year {year}: {e}")
        return []

# Get weather data for seasons from 2019 to 2024
openweather_api_key = "a007d04d4b8ff5c0b9939c8e04a81db8"  # Replace with your OpenWeather API key

all_enriched_data = []

# Loop through each year from 2019 to 2024 and fetch data
for year in range(2019, 2025):
    print(f"Fetching data for year {year}...")
    enriched_data = fetch_race_data_with_weather(year, openweather_api_key)
    all_enriched_data.extend(enriched_data)

# Save all the data to a single CSV file
df = pd.DataFrame(all_enriched_data)
df.to_csv("f1_race_weather_all_seasons_2019_to_2024.csv", index=False)
print("All race and weather data saved to f1_race_weather_all_seasons_2019_to_2024.csv")
