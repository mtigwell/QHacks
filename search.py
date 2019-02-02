import requests

def searchFunction(query, APIKey):
    try:
        content = requests.get("https://www.googleapis.com/customsearch/v1?key="+APIKey+"&cx=004968834634498115028:9rcxpfpfjsc&q="+query+"\"")
        unpacked = content.json()
        results = unpacked["items"]
        resultList = []
        urlList = []
        for i in range(len(results)):
            try:
                resultList.append(results[i]["pagemap"]["metatags"][0])
            except KeyError:
                continue
        for result in resultList:
            try:
                result['og:url'][0]
                if result['og:url'][0] == 'h':
                    urlList.append(result['og:url'])
            except KeyError:
                continue
        return urlList

    except ValueError:
        print("error generating search")


f = open("apikey.txt", "r")
APIKeystring = f.read()
APIKey = APIKeystring[10:len(APIKeystring)-1]
query = "usain bolt"
result = searchFunction(query, APIKey)
