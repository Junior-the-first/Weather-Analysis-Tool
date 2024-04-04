# weather_data_analysis.py
import requests
from datetime import datetime, timedelta
import math
import csv

# Use API Key from visual Crossing Waether API Data
API_KEY = 'S3UEQ84XHD92CQ77AGLCC4J4L'
# Base URL for Visual Crossing Weather API Timeline endpoint
BASE_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start}/{end}'

def fetch_historical_weather(location, start_date, end_date):
    """Fetches historical weather data for the specified location and date range."""
    url = f"{BASE_URL.format(location=location, start=start_date, end=end_date)}?unitGroup=metric&include=days&key={API_KEY}&contentType=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['days']
    else:
        print(f"Failed to fetch historical weather data: HTTP Status Code {response.status_code}")
        return []

def calculate_statistics(temperatures):
    """Calculates and returns the average, median, and mode of a list of temperatures."""
    avg_temp = sum(temperatures) / len(temperatures)
    median_temp = calculate_median(temperatures)
    mode_temp = max(set(temperatures), key=temperatures.count)  # Simple mode calculation
    return avg_temp, median_temp, mode_temp

def calculate_median(data):
    """Calculates the median of a list of numbers."""
    data.sort()
    n = len(data)
    midpoint = n // 2
    if n % 2 == 0:
        return (data[midpoint - 1] + data[midpoint]) / 2
    else:
        return data[midpoint]

def save_to_csv(location, weather_data, statistics):
    """Saves the historical weather data and calculated statistics to a CSV file."""
    filename = f"{location}_weather_data.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Writing header for the daily weather data
        writer.writerow(["Date", "Max Temperature (°C)"])
        # Writing the daily max temperature for each day
        for day in weather_data:
            writer.writerow([day['datetime'], day['tempmax']])
        # Writing the statistics
        writer.writerow([])  # Adding a blank row for separation
        writer.writerow(["Statistic", "Average Temperature", "Median Temperature", "Mode Temperature"])
        writer.writerow(["Value", statistics[0], statistics[1], statistics[2]])
    print(f"Weather data and statistics saved to {filename}")

def main():
    location = input("Enter the city you would like to retrieve weather data from: ")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # Format dates in YYYY-MM-DD format
    formatted_start_date = start_date.strftime('%Y-%m-%d')
    formatted_end_date = end_date.strftime('%Y-%m-%d')
    
    historical_weather_data = fetch_historical_weather(location, formatted_start_date, formatted_end_date)
    
    if historical_weather_data:
        max_temps = [day['tempmax'] for day in historical_weather_data]
        statistics = calculate_statistics(max_temps)
        print(f"Weather Data for {location}:")
        print(f"Average: {statistics[0]}°C, Median: {statistics[1]}°C, Mode: {statistics[2]}°C")
        save_to_csv(location, historical_weather_data, statistics)
    else:
        print("Unable to retrieve weather data.")

if __name__ == "__main__":
    main()