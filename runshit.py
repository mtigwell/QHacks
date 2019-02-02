import search
import ResearchAssitant

def generateEssay(filename, query):
    f = open("apikey.txt", "r")
    APIKeystring = f.read()
    APIKey = APIKeystring[10:len(APIKeystring)-1]
    result = search.searchFunction(query, APIKey, 10)
    text = ""
    for website in result:
        try:
            text += ResearchAssitant.getWords(website)
        except TypeError:
            continue
    if text is not None:
        finalessay = ResearchAssitant.SummerizeText(text)
        print(finalessay)
    else:
        print("YA FUCKED IT")
    f = open(str(filename)+".txt", "w")
    f.write(finalessay)
    f.close()

def generateArticles(query):
    f = open("apikey.txt", "r")
    APIKeystring = f.read()
    APIKey = APIKeystring[10:len(APIKeystring) - 1]
    query = "alexander the great"
    result = search.searchFunction(query, APIKey, 10)
    textList = []
    for website in result:
        try:
            text = ResearchAssitant.getWords(website)
            if text is not None:
                textList.append(ResearchAssitant.SummerizeText(text))
        except TypeError:
            continue
    return textList



