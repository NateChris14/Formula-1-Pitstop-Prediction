import requests
import pandas as pd

def fetch_pitstop_data(start_year, end_year, max_rounds):
    """
    Fetch pitstop data for all rounds from start_year to end_year.
    Saves data to a CSV file.
    """
    all_pitstops = []
    
    for year in range(start_year, end_year + 1):
        for round_number in range(1, max_rounds + 1):
            url = f"http://api.jolpi.ca/ergast/f1/{year}/{round_number}/pitstops"
            print(f"Fetching data for year {year}, round {round_number}...")
            
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                try:
                    races = data.get("MRData", {}).get("RaceTable", {}).get("Races", [])
                    for race in races:
                        race_name = race.get("raceName")
                        season = race.get("season")
                        round_no = race.get("round")
                        pitstops = race.get("PitStops", [])
                        
                        for stop in pitstops:
                            stop_data = {
                                "Race Name": race_name,
                                "Season": season,
                                "Round": round_no,
                                "Driver ID": stop.get("driverId"),
                                "Lap": stop.get("lap"),
                                "Stop": stop.get("stop"),
                                "Time": stop.get("time"),
                                "Duration": stop.get("duration")
                            }
                            all_pitstops.append(stop_data)
                except Exception as e:
                    print(f"Error processing data for year {year}, round {round_number}: {e}")
            else:
                print(f"Error fetching data for year {year}, round {round_number}. HTTP Status Code: {response.status_code}")
    
    # Convert the data to a DataFrame and save to CSV
    if all_pitstops:
        df = pd.DataFrame(all_pitstops)
        df.to_csv("pitstop_data.csv", index=False)
        print("Pitstop data saved to 'pitstop_data.csv'")
    else:
        print("No pitstop data fetched.")

# Fetch pitstop data for 2019 to 2024, assuming 22 rounds per season
fetch_pitstop_data(2019, 2024, 22)
