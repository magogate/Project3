import pandas as pd
import fetchUSCityPopulation as us_city_population
import fetchGACityPopulation as ga_city_population
import dao as dao

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
    cityAccidents = readUSAccidentsData()
    cityPopulation = us_city_population.extractData()
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

    dao.insertUSCityPopulation(city_population_accidents)
    city_pop_accidents = dao.getUSCityPopulation()
    print(city_pop_accidents)
    # (cities_list)


def getGACityPopulationAccidents():
    cityAccidents = readGAAccidentsData()
    cityPopulation = ga_city_population.populationByCities()
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
                        "state":"GA",
                        "population":city[1],
                        "accidents":city[2]
                    })

    # print(city_population_accidents)
    dao.insertGACityPopulation(city_population_accidents)
    city_pop_accidents = dao.getGACityPopulation()
    print(city_pop_accidents)


getUSACityPopulationAccidents()

getGACityPopulationAccidents()