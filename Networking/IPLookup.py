import urllib.request
import json

ip = input('Please enter an IP Address (hit enter to use your own): ')

if not ip:
	url = 'http://ipinfo.io/json'
else:
	url = ('http://ipinfo.io/' + ip + '/json')

response = urllib.request.urlopen(url).read()
data = json.loads(response.decode('utf-8'))

print()
print('IP Address: %s' % data['ip'])
print('Hostname: %s' % data['hostname'])
print('Location: %s' % data['loc'])
print('Organization: %s' % data['org'])
print('City: %s' % data['city'])
print('Region: %s' % data['region'])
print('Country: %s' % data['country'])
print('Area Code: %d' % data['phone'])
print()
