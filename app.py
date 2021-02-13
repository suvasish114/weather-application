import requests
from flask import Flask, render_template

url = 'http://api.openweathermap.org/data/2.5/weather?q={},uk&APPID=e16a84cd226983d486986572b34a3896'

app = Flask(__name__)

@app.route('/')
def index():
    r=requests.get(url.format('London')).json()
    weather = {
        'icon': r['weather'][0]['icon'],
        'city_name': r['name'],
        'tempareture': round((r['main']['temp'])-273.15),
        'description': r['weather'][0]['description']
    }
    print(weather)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)