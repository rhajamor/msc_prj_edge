# pip install openmeteo-requests
import openmeteo_requests
from openmeteo_sdk.Variable import Variable

om = openmeteo_requests.Client()

params = {
    "latitude": 52.54,  # Latitude of Berlin
    "longitude": 13.41,  # Longitude of Berlin
    "hourly": ["temperature_2m", "precipitation"],  # Requested weather variables
    "current": ["temperature_2m"],  # Current temperature
}

responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
response = responses[0]  # Consider the first location (Berlin) in the response

print(f"Coordinates: {response.Latitude()}°E, {response.Longitude()}°N")
print(f"Elevation: {response.Elevation()} meters above sea level")
print(f"Timezone: {response.Timezone()} ({response.TimezoneAbbreviation()})")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()} seconds")

# Current values
current = response.Current()
current_variables = list(
    map(
        lambda i: current.Variables(i),
        range(0, current.VariablesLength()),
    )
)

current_temperature_2m = next(
    filter(
        lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2,
        current_variables,
    )
)

print(f"Current time: {current.Time()}")
print(f"Current temperature at 2m: {current_temperature_2m.Value()}°C")
