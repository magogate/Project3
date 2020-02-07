# Created By: 
#     Grettel Canepari
#     Katherine Lee
#     Mandar Gogate
#     Petra Alex
#     Preet Puri
#     Sweta Shekhar
# Created On: 01/01/2020
# Updated On: 01/10/2020


from pymongo import MongoClient
import pandas as pd

def getConnection():
    # conn = MongoClient('localhost', 27017)
    connString = "mongodb+srv://mandargogate:Password123@cluster0-x4wnf.mongodb.net/test?retryWrites=true&w=majority"    
    conn = MongoClient(connString, 27017)    
    conn.population
    return conn.population

def insertCityPopulation(cities_list):
    # print(cities_list)
    db = getConnection()

    cityPopulation = list(db.all_us_city_population.find())
    if len(cityPopulation) < 1:
        db.all_us_city_population.insert(cities_list)
    else:
        # https://www.w3schools.com/python/python_mongodb_delete.asp
        db.all_us_city_population.delete_many({})
        db.all_us_city_population.insert(cities_list)

def getCityPopulation():
    db = getConnection()    
    cityPopulation = list(db.all_us_city_population.find({},{"population": 1, "_id":0, "city": 1, "accidents":1, "state":1}))
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
    df = pd.DataFrame(cityPopulation)
    cityPopJson = df.to_json(orient='records')
    # print(cityPopJson)
    return cityPopJson