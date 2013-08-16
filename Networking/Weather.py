import urllib.request
import json
import datetime

str = input('Please enter your city name: ')
city = str.split()
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ('%'.join(city))

response = urllib.request.urlopen(url).read()
data = json.loads(response.decode('utf-8'))
weather = data['weather']

print()
print('City: %s' % data['name'])
print('Weather: %s' % data['weather'][0]['main'])
print('Description: %s' % data['weather'][0]['description'])
print('Current Temp: %.2f%s' % (((data['main']['temp']-273.15)*(9/5) + 32), '°F'))
print('Hi: %.2f%s | Low: %.2f%s' % (((data['main']['temp_max']-273.15)*(9/5) + 32), 
	'°F', ((data['main']['temp_min']-273.15)*(9/5) + 32), '°F'))
print('Wind: %d%s' % (data['wind']['speed'], ' MPH'))
print('Humidity: %d%s' % (data['main']['humidity'], '%'))
print('Cloudiness: %d%s' % (data['clouds']['all'], '%'))
print('Sunrise: ' + datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M') 
	+ ' AM EST')
print('Sunset: ' + (datetime.datetime.fromtimestamp(data['sys']['sunset']) 
	+ datetime.timedelta(hours=-12)).strftime('%H:%M') + ' PM EST')
print()
