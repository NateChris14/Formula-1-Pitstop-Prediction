# Pitstop Prediction Project

## Overview
The Pitstop Prediction Project is a machine learning-based solution designed to predict pitstop strategies in Formula 1 races. Using historical race data, the model predicts the number of stops a driver should make during the race, helping teams make data-driven decisions during races. This model was evaluated on weighted precision score during which it achieved a score of nearly 70% on the test data which means that 7 out of 10 times the model correctly predicts the number of stops that should be made, solely based on historical data.

## Features
- Multiclass classification to predict optimal pitstop strategies.
- Uses SMOTE for handling class imbalance in training data.

## Dataset
This project utilizes the Ergast Developer API for Formula 1 data:  
[Ergast F1 API](https://api.jolpi.ca/ergast/f1/)

The project utilizes Formula 1 race data, including:
- **Laps Data:** Information on lap times, tire usage, and positions.
- **Weather Data:** Conditions like track temperature, rain levels, and humidity.
- **Pitstops Data:** Timing and frequency of pitstops.
- **Results Data:** Final race outcomes and standings.

### Dataframes
- `df_laps`: Lap-specific data for each driver.
- `df_weather`: Weather conditions during the race.
- `df_pitstops`: Pitstop timings and strategies.
- `df_results`: Overall race results.

## Model
The project evaluates multiple classifiers to predict pitstop strategies. Key aspects:
- **Training Data:** Includes 18 features derived from the dataframes.
- **Feature Engineering:** Encodes categorical variables, normalizes numerical variables, and handles missing values.
- **Class Imbalance Handling:** Synthetic Minority Oversampling Technique (SMOTE) is applied.

### Evaluation Metrics
- Precision
- Recall
- F1-Score
- Learning Curve

## Installation
### Prerequisites
- Python 3.7+
- Flask
- XGBoost
- Pandas
- Scikit-learn

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pitstop-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pitstop-prediction
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Future Enhancements
- Expand dataset to include more seasons and tracks.
- Implement real-time data fetching from APIs .
- Deploy the app to a cloud platform for public access.
- Add support for additional models and comparison of their performances.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Formula 1 data from Ergast API.
- Machine learning libraries: XGBoost, Scikit-learn.

For any questions or issues, feel free to contact me.

