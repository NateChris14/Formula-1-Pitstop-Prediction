import requests
import csv

# Fetch race data from API
def fetch_race_data(season, round_number):
    BASE_URL = "http://api.jolpi.ca/ergast/f1"
    url = f"{BASE_URL}/{season}/{round_number}/results.json"
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request is successful
    return response.json()

# Process race data
def process_data(data):
    race_table = data['MRData']['RaceTable']
    races = race_table['Races']
    rows = []

    for race in races:
        year = race_table['season']
        round_number = race['round']
        race_name = race['raceName']

        for result in race['Results']:
            driver_name = f"{result['Driver']['givenName']} {result['Driver']['familyName']}"
            constructor_name = result['Constructor']['name']
            grid = result['grid']
            position = result['position']
            time = result.get('Time', {}).get('time', "N/A")
            fastest_lap_time = result.get('FastestLap', {}).get('Time', {}).get('time', "N/A")
            points = result['points']
            status = result['status']
            laps = result['laps']

            rows.append([
                year, round_number, race_name, driver_name, constructor_name,
                grid, position, time, fastest_lap_time, points, status, laps
            ])
    return rows

# Save data to CSV
def save_to_csv(rows, filename="race_results_all_seasons.csv"):
    headers = [
        "Year", "Round", "Race Name", "Driver Name", "Constructor Name",
        "Grid Position", "Final Position", "Time", "Fastest Lap Time",
        "Points", "Status", "Number of Laps"
    ]
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

# Main Function
def main():
    all_data = []
    max_rounds = 24  # Adjust based on the maximum number of rounds for each season

    # Loop through each season from 2019 to 2024
    for season in range(2019, 2025):
        print(f"Fetching data for season {season}...")
        for round_number in range(1, max_rounds + 1):
            print(f"  Fetching data for round {round_number}...")
            try:
                race_data = fetch_race_data(season, round_number)
                round_data = process_data(race_data)
                all_data.extend(round_data)
            except requests.exceptions.RequestException as e:
                print(f"    Error fetching data for round {round_number}: {e}")
            except KeyError as e:
                print(f"    Data missing for round {round_number}: {e}")

    if all_data:
        save_to_csv(all_data)
        print(f"All race results from 2019 to 2024 saved to race_results_all_seasons.csv")
    else:
        print("No data available for the requested seasons.")

if __name__ == "__main__":
    main()
