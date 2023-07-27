import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '1b2108b34b87c41199c48170d8b6e1c6'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)
        data = response.json()

        if data['cod'] == '404':
            error_message = 'City not found. Please enter a valid city name.'
            return render(request, 'index.html', {'error_message': error_message})
        else:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            return render(request, 'index.html', {'weather_data': weather_data})
    
    return render(request, 'index.html')

