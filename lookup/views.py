from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode + '&distance=5&API_KEY=64933201-FDC2-4B02-A5D8-53F6332543C1')
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'Error..... '


		if api[0]['Category']['Name'] == 'Good':
			c_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk.'
			c_color = 'good'

		elif api[0]['Category']['Name'] == 'Moderate':
			c_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
			c_color = 'moderate'

		elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
			c_description = '(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air'
			c_color = 'usg'

		elif api[0]['Category']['Name'] == 'Unhealthy':
			c_description = '(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
			c_color = 'unhealthy'

		elif api[0]['Category']['Name'] == 'Very Unhealthy':
			c_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
			c_color ='veryunhealthy'

		elif api[0]['Category']['Name'] == 'Hazardous':
			c_description = '(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected'
			c_color = 'hazardous'

		return render(request, 'home.html', {
			'api': api, 
			'c_description': c_description, 
			'c_color': c_color
			})


	else:
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=64933201-FDC2-4B02-A5D8-53F6332543C1')
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'Error..... '


		if api[0]['Category']['Name'] == 'Good':
			c_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk.'
			c_color = 'good'

		elif api[0]['Category']['Name'] == 'Moderate':
			c_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
			c_color = 'moderate'

		elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
			c_description = '(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air'
			c_color = 'usg'

		elif api[0]['Category']['Name'] == 'Unhealthy':
			c_description = '(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
			c_color = 'unhealthy'

		elif api[0]['Category']['Name'] == 'Very Unhealthy':
			c_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
			c_color ='veryunhealthy'

		elif api[0]['Category']['Name'] == 'Hazardous':
			c_description = '(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected'
			c_color = 'hazardous'

		return render(request, 'home.html', {
			'api': api, 
			'c_description': c_description, 
			'c_color': c_color
			}) 

def about(request):
	return render(request, 'about.html', {})


