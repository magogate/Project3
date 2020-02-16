import pickle
import sklearn
from flask import Flask, jsonify, render_template, flash, request

app = Flask(__name__, static_url_path='/static')

random_forest_classifier = ""

@app.route("/")
def index():    
    random_forest_classifier = pickle.load(open("models/k_neares_neighbour", 'rb'))
    print(sklearn.__version__)
    return render_template("index.html")  

# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
@app.route("/classification", methods=["POST","GET"])
def classification():        
    input_list = []
    city = request.form.get("City")
    input_list.append(city)
    lat = request.form.get("Start_Lat")
    input_list.append(lat)
    lng = request.form.get("Start_Lng")
    input_list.append(lng)
    traffic_signal = request.form.get("Traffic_Signal")
    input_list.append(traffic_signal)
    tmc = request.form.get("TMC")
    input_list.append(tmc)
    temp = request.form.get("Temprature")
    input_list.append(temp)
    wind_chill = request.form.get("Wind_Chill")
    input_list.append(wind_chill)
    humidity = request.form.get("Humidity")
    input_list.append(humidity)
    pressure = request.form.get("Pressure")
    input_list.append(pressure)
    wind_speed = request.form.get("Wind_Speed")
    input_list.append(wind_speed)
    hour = request.form.get("Hour")
    input_list.append(hour)
    weekday = request.form.get("Weekday")
    input_list.append(weekday)
    time_duration = request.form.get("Time_Duration")
    input_list.append(time_duration)

    print(input_list)
    
    return render_template("classification.html")  

if __name__ == "__main__":
    app.run(debug=True)