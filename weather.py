import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    data = requests.get(url).json()
    print(data)  # Debug

    if data.get("cod") != 200:
        return f"Error: {data.get('message')}"

    temp = data['main']['temp']
    desc = data['weather'][0]['description']

    return f"{city} temperature is {temp}°C with {desc}"