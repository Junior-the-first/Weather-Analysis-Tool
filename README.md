# Weather Data Analysis Tool

This Python script provides an analysis of historical weather data for a specified location (city). It fetches data for the past 7 days using the Visual Crossing Weather API, calculates the average, median, and mode of the maximum temperatures, and saves the data and statistics to a CSV file.

# Requirements

Before you begin, ensure you have the following:
- Python 3.x installed on your system.
- An API key from Visual Crossing Weather, which you can obtain by signing up at [Visual Crossing Weather](https://www.visualcrossing.com/).

# Installation

To set up the Weather Data Analysis Tool, follow these steps:

1. Obtain th repository from Github.
2. Navigate to the project directory in your terminal or command prompt.
3. Install the required Python packages using pip:
 
pip install requests

# Configuration

Before running the script, you need to insert your Visual Crossing Weather API key into the script. Open the `weather_analysis.py` file in a text editor and replace `API_Key` with your actual API key.

# Running the Script

To run the script, follow these instructions:

1. Open your terminal or command prompt.
2. Navigate to the `src` directory where the `weather_analysis.py` file is located.
3. Execute the script by running:
 	python weather_analysis.py

4. When prompted, enter the location you want to get weather data for.

# Output

The script will create a CSV file named `<location>_weather_statistics.csv` in the current directory. This file will contain:
- A record of the maximum temperature for each of the past 7 days.
- The calculated average, median, and mode of the maximum temperatures.
