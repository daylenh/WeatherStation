from flask import Flask, render_template, jsonify
from weather import WeatherStation

app = Flask(__name__)
station = WeatherStation()

@app.route('/collect')
def collect():
    reading = station.collect_data()
    return jsonify(reading)

@app.route('/')
def index():
    if not station.data:
        station.simulate_past_days(7)  
    summary = station.summary()
    return render_template("index.html", summary=summary, temperatures=summary["temperatures_by_day"])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
