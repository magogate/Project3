import pandas as pd
import fetchUSCityPopulation as us_city_population
import fetchGACityPopulation as ga_city_population
import dao as dao

def readCityTransportData():
    city_state_transport = []
    df_usa_transport = pd.read_csv(".\\US_Accidents_Dec19\\USA_Cities_PublicTransport.csv")
    # city_state_transport
    for index, row in df_usa_transport.iterrows():
        city_state = []
        city_state.append(row["City-State"].split(",")[0].strip().lower())
        city_state.append(row["City-State"].split(",")[1].strip().lower())
        city_state.append(row["PublicTransportNumbers"])
        city_state_transport.append(city_state)
    return (city_state_transport)

def readUSAccidentsData():
    df_usa_accidents = pd.read_csv(".\\US_Accidents_Dec19\\US_Accidents_2018.csv")
    df_acc_by_city = df_usa_accidents.loc[:,["ID","City","State"]].groupby(["City","State"]).count()
    # df_acc_by_city.to_csv(".\\US_Accidents_Dec19\\US_Accidents_2018_By_CityState.csv")
    df_acc_by_city = df_acc_by_city.reset_index()
    city_state_accidents = []
    for index, row in df_acc_by_city.iterrows():
        accidents = []
        accidents.append(row.ID)        
        accidents.append(row.City.lower())
        accidents.append(row.State.lower())
        city_state_accidents.append(accidents)

    return (city_state_accidents)

def readGAAccidentsData():
    df_usa_accidents = pd.read_csv(".\\US_Accidents_Dec19\\US_Accidents_2018.csv")
    df_ga_accidents = df_usa_accidents.loc[df_usa_accidents.loc[:,"State"] == "GA", :]
    df_acc_by_city = df_ga_accidents.loc[:,["ID","City","State"]].groupby(["City","State"]).count()
    df_acc_by_city = df_acc_by_city.reset_index()
    city_state_accidents = []
    for index, row in df_acc_by_city.iterrows():
        accidents = []
        accidents.append(row.ID)        
        accidents.append(row.City.lower())
        accidents.append(row.State.lower())
        city_state_accidents.append(accidents)

    return (city_state_accidents)


def getUSACityPopulationAccidents():
    print("Inside getUSACityPopulationAccidents")
    cityAccidents = readUSAccidentsData()
    print("After calling dataframe")
    # cityPopulation = us_city_population.extractData()
    cityPopulation = ga_city_population.populationByUSACities()
    print("After webscrap")
    # print(cityAccidents)
    city_population_accidents = []
    for city in cityPopulation:
        if(len(city) > 1):
            for c in cityAccidents:
                if(city[0] == c[1] and city[1] == c[2]):
                    city.append(c[0])
                    # dao.insertCityPopulation(city)
                    # print(city)
                    city_population_accidents.append({
                        "city":city[0],
                        "state":city[1],
                        "population":city[2],
                        "accidents":city[3]
                    })
    print("Assiging transport data")
    for city in city_population_accidents:        
        print(city)
        city["transportation"] = 0.1
        for c in readCityTransportData():
            if(city["city"] == c[0] and city["state"] == c[1]):
                city["transportation"] = c[2]   

    # print(city_population_accidents)
    dao.insertUSCityPopulation(city_population_accidents)
    city_pop_accidents = dao.getUSCityPopulation()
    # print(city_pop_accidents)
    print("USA City Process Completed")
    # (cities_list)


def getGACityPopulationAccidents():
    cityAccidents = readGAAccidentsData()
    cityPopulation = ga_city_population.populationByGACities()
    # print(cityAccidents)
    city_population_accidents = []
    for city in cityPopulation:
        if(len(city) > 1):
            for c in cityAccidents:
                if(city[0] == c[1]):
                    city.append(c[0])
                    # dao.insertCityPopulation(city)
                    # print(city)
                    city_population_accidents.append({
                        "city":city[0],
                        "state":"ga",
                        "population":city[2],
                        "accidents":city[3]
                    })

    for city in city_population_accidents:        
        city["transportation"] = 0.1
        for c in readCityTransportData():
            if(city["city"] == c[0] and city["state"] == c[1]):
                city["transportation"] = c[2]                

    # print(city_population_accidents)
    dao.insertGACityPopulation(city_population_accidents)
    city_pop_accidents = dao.getGACityPopulation()
    # print(city_pop_accidents)
    print("GA City Process Completed")


getUSACityPopulationAccidents()

getGACityPopulationAccidents()

