import requests

def searchFunction(query, APIKey, num, startIndex):
    if num > 10: num = 10
    if num < 1: num = 1
    try:
        content = requests.get("https://www.googleapis.com/customsearch/v1?key="+APIKey+"&cx=004968834634498115028:9rcxpfpfjsc&q="+query+"&num="+str(num)+"&start="+str(startIndex))
        unpacked = content.json()
        # nextpageindex = unpacked['queries']['nextPage'][0]['startIndex']
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
query = "alexander the great"
result = searchFunction(query, APIKey, 10, 10)
print(len(result))

# inputString = "Nonetheless, many conquered lands retained the Greek influence Alexander introduced—some cities he founded remain important cultural centers even today—and Alexander the Great is revered as one of the most powerful and influential leaders the ancient world ever produced. Alexander the Great. Alexander the Great. Alexander the Great of Macedon Biography. Alexander of Macedonia. RELATED   CONTENT Alexander the Great, the young Macedonian military genius who forged an empire stretching from the eastern Mediterranean to India, dies in Babylon, in present-day Iraq, at the age of 33."

# def removeDuplicates(inpStr):
#     inpStr.split('.')
#     print(inpStr)
#
#
# removeDuplicates(inputString)

