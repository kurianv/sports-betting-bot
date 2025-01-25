import requests
api_key = 'f5feac717a84104b29f452b195338d03'

user = input("Enter the city name: ")

weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user}&appid={api_key}').json()


print(f"City: {weather_data['name']}")
print(f"Temperature: {round((9/5)*(weather_data['main']['temp'])-459.67)}°F")
print(f"Humidity: {weather_data['main']['humidity']}%")
print(f"Pressure: {((weather_data['main']['pressure'])/33.864):.2f} inHg")
print(f"Wind Speed: {round((weather_data['wind']['speed'])*2.237)} mph")
print(f"Weather: {weather_data['weather'][0]['description']}")
print(f"Pressure: {(weather_data['main']['pressure'])}")