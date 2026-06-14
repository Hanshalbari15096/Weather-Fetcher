import requests
API_KEY="9f49dbcaf204daf47302f01141c3faab"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city=input("Enter your City:")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code== 200:
    data=response.json()
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"\n🌍 Weather in {city.title()}:")
    print(f"Weather:{weather}")
    print(f"Temperture:{temperature}")
    print(f"Humidity: {humidity}%")
    
else:
    print("An error occurred.")
