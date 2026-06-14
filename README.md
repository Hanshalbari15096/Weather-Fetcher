# Weather CLI

A simple command-line weather app using the OpenWeatherMap API.

## Requirements

```
pip install requests
```

## Usage

```
python Weather.py
```

Enter a city name when prompted.

## Example

```
Enter your City: Mumbai

🌍 Weather in Mumbai:
Weather: light rain
Temperature: 29.3
Humidity: 83%
```

## Output Fields

| Field | Description |
|-------|-------------|
| Weather | Sky condition description |
| Temperature | Current temp in °C |
| Humidity | Relative humidity (%) |

## Config

- **API Key:** Hardcoded in script (`API_KEY`)
- **Units:** Metric (°C)
- **API:** [OpenWeatherMap Current Weather](https://openweathermap.org/current)
