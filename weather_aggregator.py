import requests
import json
import os
from datetime import datetime

def fetch_weather_data(api_key, api_url, key_param):
    response = requests.get(api_url, params={key_param: api_key})
    return response.json()

def aggregate_weather_data():
    # Replace 'YOUR_OPENWEATHERMAP_API_KEY' and 'YOUR_WEATHERSTACK_API_KEY' with your actual API keys
    openweathermap_api_key = os.environ['OPENWEATHERMAP_API_KEY']
    weatherstack_api_key = os.environ['WEATHERSTACK_API_KEY']

    openweathermap_url = "http://api.openweathermap.org/data/2.5/weather?q=Nairobi"
    weatherstack_url = "http://api.weatherstack.com/current?query=Nairobi"

    start_time = datetime.now()

    data_source_openweathermap = fetch_weather_data(openweathermap_api_key, openweathermap_url, 'appid')
    data_source_weatherstack = fetch_weather_data(weatherstack_api_key, weatherstack_url, 'access_key')

    end_time = datetime.now()
    execution_time = end_time - start_time

    # Combine data from different sources (Example: Merge current weather details)
    aggregated_data = {
        'openweathermap': data_source_openweathermap,
        'weatherstack': data_source_weatherstack,
        'execution_time': execution_time.total_seconds() 
    }


    return aggregated_data

if __name__ == "__main__":
    aggregated_data = aggregate_weather_data()

    with open('aggregated_weather.json', 'w') as outfile:
        json.dump(aggregated_data, outfile)


    # Update the README file with the timestamp and execution duration
    with open('README.md', 'w') as readme_file:
        readme_file.write(f"# Weather Data Aggregation\n\n")
        readme_file.write(f"Last Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        readme_file.write(f"Execution Time: {aggregated_data['execution_time']} seconds\n")
