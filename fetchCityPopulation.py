import requests
import bs4

def extractData(url):

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
                        myPopList.append(city)
                    if(cnt==2):
                        # print(data.find("a"))
                        # https://www.geeksforgeeks.org/ternary-operator-in-python/
                        state = data.text if (data.find("a") == None) else data.find("a").text
                        myPopList.append(state.replace("\xa0","").replace("\n",""))
                        # print(state.strip())
                    if(cnt==3):
                        # print(data.text.strip())
                        population = data.text.strip()
                        myPopList.append(population)

                    # cityPopulation = f"{city},{state},{population}"
                    cnt += 1
                print(myPopList)
                    
            
    # cityPopulation = open("cityPopulation.txt","w+")
    # cityPopulation.write(response)
    # print(response.text.replace("\u2660","").replace("\u2032",""))


url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

extractData(url)