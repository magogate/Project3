import pandas as pd

def readUSCountyPopulationAndAccidents():
    mydf = pd.read_csv("County_accidents_2018.csv")

    us_county = []

    for index, row in mydf.iterrows():        
        if(row[0] != "Grand Total"):
            us_county.append({
                "county":row[0].lower(),
                "population":row[2],
                "accidents":row[1]
            })

    # print(us_county)
    return us_county

# readUSCountyPopulationAndAccidents()