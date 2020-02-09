import pandas as pd
import dao as dbCon

city_population_url_list = ["http://www.togetherweteach.com/TWTIC/uscityinfo/01al/alpopr/01alpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/01al/alpopr/01alpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/01al/alpopr/01alpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/02ak/akpopr/02akpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/02ak/akpopr/02akpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/03az/azpopr/03azpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/04ar/arpopr/04arpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/04ar/arpopr/04arpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/04ar/arpopr/04arpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/05ca/capopr/05capr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/05ca/capopr/05capr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/05ca/capopr/05capr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/05ca/capopr/05capr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/05ca/capopr/05capr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/06co/copopr/06copr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/06co/copopr/06copr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/07ct/ctpopr/07ctpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/08de/depopr/08depr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/09fl/flpopr/09flpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/09fl/flpopr/09flpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/09fl/flpopr/09flpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/09fl/flpopr/09flpr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/10ga/gapopr/10gapr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/10ga/gapopr/10gapr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/10ga/gapopr/10gapr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/11hi/hipopr/11hipr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/12id/idpopr/12idpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/13il/ilpopr/13ilpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/13il/ilpopr/13ilpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/13il/ilpopr/13ilpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/13il/ilpopr/13ilpr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/13il/ilpopr/13ilpr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/13il/ilpopr/13ilpr6.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/14in/inpopr/14inpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/14in/inpopr/14inpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/14in/inpopr/14inpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/15ia/iapopr/15iapr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/15ia/iapopr/15iapr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/15ia/iapopr/15iapr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/15ia/iapopr/15iapr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/16ks/kspopr/16kspr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/16ks/kspopr/16kspr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/16ks/kspopr/16kspr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/16ks/kspopr/16kspr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/17ky/kypopr/17kypr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/17ky/kypopr/17kypr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/18la/lapopr/18lapr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/18la/lapopr/18lapr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/19me/mepopr/19mepr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/20md/mdpopr/20mdpr.htm",
# "http://www.togetherweteach.com/TWTIC/uscityinfo/21ma/mapopr/21mapr.htm",
# "http://www.togetherweteach.com/TWTIC/uscityinfo/21ma/mapopr/21mapr2.htm",
# "http://www.togetherweteach.com/TWTIC/uscityinfo/21ma/mapopr/21mapr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr6.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr7.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/22mi/mipopr/22mipr8.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr6.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr7.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr8.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr9.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/23mn/mnpopr/23mnpr10.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/24ms/mspopr/24mspr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/24ms/mspopr/24mspr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/25mo/mopopr/25mopr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/25mo/mopopr/25mopr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/25mo/mopopr/25mopr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/25mo/mopopr/25mopr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/26mt/mtpopr/26mtpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/27ne/nepopr/27nepr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/27ne/nepopr/27nepr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/27ne/nepopr/27nepr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/28nv/nvpopr/28nvpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/29nh/nhpopr/29nhpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/30nj/njpopr/30njpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/31nm/nmpopr/31nmpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr6.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr7.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/32ny/nypopr/32nypr8.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/33nc/ncpopr/33ncpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/33nc/ncpopr/33ncpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/33nc/ncpopr/33ncpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/34nd/ndpopr/34ndpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/35oh/ohpopr/35ohpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/35oh/ohpopr/35ohpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/35oh/ohpopr/35ohpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/35oh/ohpopr/35ohpr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/36ok/okpopr/36okpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/36ok/okpopr/36okpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/36ok/okpopr/36okpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/37or/orpopr/37orpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/37or/orpopr/37orpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr6.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr7.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr8.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/38pa/papopr/38papr9.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/39ri/ripopr/39ripr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/40sc/scpopr/40scpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/40sc/scpopr/40scpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/41sd/sdpopr/41sdpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/41sd/sdpopr/41sdpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/42tn/tnpopr/42tnpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/42tn/tnpopr/42tnpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr6.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr7.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr8.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/43tx/txpopr/43txpr9.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/44ut/utpopr/44utpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/44ut/utpopr/44utpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/45vt/vtpopr/45vtpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/46va/vapopr/46vapr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/46va/vapopr/46vapr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/47wa/wapopr/47wapr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/47wa/wapopr/47wapr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/47wa/wapopr/47wapr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/48wv/wvpopr/48wvpr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/48wv/wvpopr/48wvpr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr2.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr3.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr4.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr5.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr6.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr7.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/49wi/wipopr/49wipr8.htm",
"http://www.togetherweteach.com/TWTIC/uscityinfo/50wy/wypopr/50wypr.htm"]

def extractData(city_list):   
    cities_list = []
    for url in city_list:
        print(url)
        df = pd.read_html(url)[7]    
        df.dropna()
        cities_df2 = df.rename(columns={0: "city", 1: "population"})
        
        # Iterate through each row and append in above list
        for i in range(0,len(cities_df2)):
            city = []
            city.append(str(cities_df2.loc[i][0]).lower().replace(" city",""))
            city.append(url.replace("http://www.togetherweteach.com/TWTIC/uscityinfo/","")[2:4])
            city.append(cities_df2.loc[i][1])        
            cities_list.append(city)
    
    # print(cities_list)
    return cities_list


def populationByUSACities():        
    cities_list = extractData(city_population_url_list)
    # print(cities_list)
    return cities_list

def populationByGACities():    
    cities_list = extractData(["http://www.togetherweteach.com/TWTIC/uscityinfo/10ga/gapopr/10gapr.htm",
                                "http://www.togetherweteach.com/TWTIC/uscityinfo/10ga/gapopr/10gapr2.htm",
                                "http://www.togetherweteach.com/TWTIC/uscityinfo/10ga/gapopr/10gapr3.htm"]
                                )
    # print(cities_list)
    return cities_list

# populationByCities()