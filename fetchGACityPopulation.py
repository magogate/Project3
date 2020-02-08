import pandas as pd
import dao as dbCon

def extractData(url):    
    df = pd.read_html(url)[7]    
    df.dropna()
    cities_df2 = df.rename(columns={0: "city", 1: "population"})                  
    cities_list = []
    # Iterate through each row and append in above list
    for i in range(0,len(cities_df2)):
        city = []
        city.append(str(cities_df2.loc[i][0]).lower().replace(" city",""))
        city.append(cities_df2.loc[i][1])
        cities_list.append(city)
    
    # print(cities_list)
    return cities_list


def populationByCities():
    baseUrl = "http://www.togetherweteach.com/TWTIC/uscityinfo/10ga/gapopr/10gapr.htm"
    cities_list = extractData(baseUrl)
    return cities_list

populationByCities()