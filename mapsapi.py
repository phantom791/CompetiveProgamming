import requests
from urllib.parse import urlencode


''' 
data_type = 'json'
endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
params = {'address': '1600 Amphitheatre Parkway, Mountain View, CA', 'key': api_key}

url_params = urlencode(params)
url = f'{endpoint}?{url_params}'
print(url_params)


https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,
+Mountain+View,+CA&key=YOUR_API_KEY'''

def extractLatLang(address_or_postalcode, data_type = 'json'):
	endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
	params = {'address': address_or_postalcode, 'key': api_key}
	url_params = urlencode(params)
	url = f'{endpoint}?{url_params}'
	r = requests.get(url)

	if r.status_code not in range(200,299):
		return {}
	latlng = {} 
	try:
		latlng = r.jaon()['results'][0]['geometry']['location']
	except:
		pass
	return latlng.get('lat'), latlng.get('lng')


api_key = 'AIzaSyDcDXbD6bpnEnutVXGdZRkRLjz0iKy6aLQ'

#print(extractLatLang('1600 Amphitheatre Parkway, Mountain View, CA'))

print(requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDcDXbD6bpnEnutVXGdZRkRLjz0iKy6aLQ'))
