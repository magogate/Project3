import requests
import bs4

usStates = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin','wyoming', 'american samoa', 'district of columbia']
usStatesCodes = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy', 'as', 'dc']
url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

def getStateCode(state):    
    return (usStatesCodes[usStates.index(state)])    
    

def extractData():

    city=""
    state=""
    population=""

    hdr = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=hdr)
    soup = bs4.BeautifulSoup(response.text, "html.parser")    
    cityPop = soup.find_all('table', class_="wikitable sortable")
    # print(cityPop.encode("utf-8"))
    for pop in cityPop:        
        # https://github.com/llSourcell/twitter_sentiment_challenge/issues/1
        tabelContent = str(pop.encode("utf-8"))
        # https://www.afternerd.com/blog/python-string-contains/
        if ("2018<br/>rank" in tabelContent):
            cityPopulation = []
            # https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup
            for tr in (pop.find("tbody").find_all("tr")):
                # print(td.find("a").get("title"))
                td = tr.find_all("td", limit=4)
                cnt=0
                myPopList = []
                for data in td:                    
                    if(cnt==1):
                        # print(data.find("a").text)
                        city = data.find("a").text
                        if(city != ''):
                            myPopList.append(city.lower())
                    if(cnt==2):
                        # print(data.find("a"))
                        # https://www.geeksforgeeks.org/ternary-operator-in-python/
                        state = data.text if (data.find("a") == None) else data.find("a").text
                        if(state != ''):
                            myPopList.append(state.replace("\xa0","").replace("\n","").lower())
                        # print(state.strip())
                    if(cnt==3):
                        # print(data.text.strip())
                        population = data.text.strip()
                        if(population != ''):
                            myPopList.append(int(population.replace(",","")))

                    # cityPopulation = f"{city},{state},{population}"
                    cnt += 1
                cityPopulation.append(myPopList)


            for state in cityPopulation:
                if(len(state) > 0):
                    state[1] = getStateCode(state[1])

            return (cityPopulation)

            
    # cityPopulation = open("cityPopulation.txt","w+")
    # cityPopulation.write(response)
    # print(response.text.replace("\u2660","").replace("\u2032",""))

# extractData()
# getStateCode("test")