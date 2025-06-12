import requests

url = "http://api.openweathermap.org/data/2.5/forecast"
params = {
    "id" : 524901, 
    "appid" : "99cd4fe64c7ac230a93cc09002d102fd"
}

response = requests.get(url, params = params)
data = response.json()
# for i in data.keys():
    # print(i)
# print(data)

city_name = input("enter the city name : ")
forecast = data["list"][0]

main = forecast["main"]
weather = forecast["weather"][0]
wind = forecast["wind"]

print("Date:", forecast["dt_txt"])
print("Temperature:", main["temp"])
print("Feels Like:", main["feels_like"])
print("Weather:", weather["description"])
print("Wind Speed:", wind["speed"])
