from django.shortcuts import render
import requests

def index(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city') 
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=53f9387f9cfe7c4e750729557058f3e0'
        r = requests.get(url).json()
        weather_data = {
            'city': city,
            'temperature': r['main']['temp'],
            'pressure': r['main']['pressure'],
            'humidity': r['main']['humidity'],
            'description': r['weather'][0]['description'],
            'weather': r['weather'][0]['main'],
        }
    return render(request, 'weather.html', weather_data)
