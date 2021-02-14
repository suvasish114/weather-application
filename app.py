import requests
from flask import Flask, render_template
from form import SearchForm

url = 'http://api.openweathermap.org/data/2.5/weather?q={},uk&APPID=e16a84cd226983d486986572b34a3896'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'suvasishdas114'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/')
def index():
    city_name = ""
    search_form = SearchForm()
    city_name = search_form.city_name.data
    print(city_name)
    r = requests.get(url.format(city_name)).json()
    weather = {
        'icon': r['weather'][0]['icon'],
        'city_name': r['name'],
        'tempareture': round((r['main']['temp'])-273.15),
        'description': r['weather'][0]['description']
    }
    print(weather)
    return render_template('index.html', search_form=search_form, weather=weather)

# errors


@app.errorhandler(404)
@app.errorhandler(500)
def error(e):
    error_code = 200
    error_name = 'oops, error happen'
    if e == 404:
        error_code = 404
        error_name = 'page not found'
    else:
        error_code = 500
        error_name = 'internal server error'

    return render_template('error.html', error_code=error_code, error_name=error_name)


if __name__ == '__main__':
    app.run(debug=True)
