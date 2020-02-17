import pickle
import sklearn
from flask import Flask, jsonify, render_template, flash, request

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():        
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
# 5745.0  35.191669 -114.06745900000001  0.0 201.0 75.0 75.0 9.0 26.59 13.0 16.0 1 775.0 -- 3
    print(input_list) 
    print(request.form.get("City"))
    out_list = []  
    if(request.form.get("City") != None):
        random_forest_classifier = pickle.load(open("models/random_forest_classifier_important", 'rb'))
        severity_val = (random_forest_classifier.predict([input_list])[0])              
        out_list.append(severity_val)    
        out_list.append(lat)
        out_list.append(lng)
        print(out_list)
    
    return render_template("classification.html", outlist = out_list)  

if __name__ == "__main__":
    app.run(debug=True)