import requests
import pandas as pd

def fetch_lap_data(year, round_number):
    """Fetch lap data for a specific race round."""
    url = f"http://ergast.com/api/f1/{year}/{round_number}/laps.json?limit=2000"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_lap_data(lap_data, year, round_number):
    """Process lap data to extract relevant fields."""
    races = lap_data.get("MRData", {}).get("RaceTable", {}).get("Races", [])
    if not races:
        return []

    processed_data = []
    for race in races:
        race_name = race.get("raceName", "Unknown")
        laps = race.get("Laps", [])
        for lap in laps:
            lap_number = lap.get("number")
            for timing in lap.get("Timings", []):
                processed_data.append({
                    "Year": year,
                    "Round": round_number,
                    "Race Name": race_name,
                    "Lap Number": lap_number,
                    "Driver ID": timing.get("driverId"),
                    "Position": timing.get("position"),
                    "Lap Time": timing.get("time"),
                })
    return processed_data

def main():
    """Main function to fetch, process, and save lap data for all rounds and all seasons from 2019 to 2024."""
    total_rounds = 23  # Adjust based on the season length
    all_data = []

    # Loop through each season from 2019 to 2024
    for year in range(2019, 2025):
        print(f"Processing data for {year}...")

        for round_number in range(1, total_rounds + 1):
            try:
                print(f"  Fetching lap data for Round {round_number}...")
                lap_data = fetch_lap_data(year, round_number)
                round_data = process_lap_data(lap_data, year, round_number)
                all_data.extend(round_data)
            except requests.RequestException as e:
                print(f"  Failed to fetch lap data for Round {round_number} of {year}: {e}")

    # Save to CSV
    df = pd.DataFrame(all_data)
    csv_file = "f1_lap_times_2019_2024.csv"
    df.to_csv(csv_file, index=False)
    print(f"Data saved to {csv_file}")

if __name__ == "__main__":
    main()
