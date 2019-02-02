from flask import Flask, request
from flask_cors import CORS, cross_origin
from json import dumps
from flask_jsonpify import jsonify
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
from multiprocessing import Pool
import indicoio
from summa import summarizer
import requests


indicoio.config.api_key = '10b9bc05e39205de419a80cc3263ea3c'

f = open("apikey.txt", "r")
APIKeystring = f.read()
APIKey = APIKeystring[10:len(APIKeystring)-1]

app = Flask(__name__)
CORS(app)

# API for doing search
@app.route('/search', methods=['GET'])
def searchAPI():
    search_term = request.args.get('search')
    num_results = request.args.get('results')
    print(search_term, num_results)
    urls = searchFunction(search_term)
    with Pool(10) as p:
        result = p.map(async_search, urls)
    return jsonify(result)

# API for expanding summary
@app.route('/expand', methods=['GET'])
def expand():
    url = request.args.get('url')
    print(url)
    result = {
        'summary': async_search(url, 8)
    }

    return jsonify(result)

def searchFunction(query, APIKey, num):
    if num > 10: num = 10
    if num < 1: num = 1
    try:
        content = requests.get("https://www.googleapis.com/customsearch/v1?key="+APIKey+"&cx=004968834634498115028:9rcxpfpfjsc&q="+query+"&num="+str(num))
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


def getWords(url):
    page_html = requests.get(url)
    page_soup = Soup(page_html.text, "html.parser")
    paragraphs = page_soup.findAll('p')
    data = ""
    text = []
    text.append(" ")
    for par in paragraphs:
        for p in par:
            line = str(p.string)
            line.strip("\\n")
            text.append(line)
            if text[len(text)-1] == "\n" or text[len(text)-1] == "None":
                text.pop()

            data = data + " " + text[len(text)-1]
    return data


def SummerizeText(text):
    t = summarizer.summarize(text)
    t = re.sub(r'\[.*?\]','', t)
    t = t.strip('\n')
    t = t.strip('\t')
    return t


def generateEssay(filename, query):
    f = open("apikey.txt", "r")
    APIKeystring = f.read()
    APIKey = APIKeystring[10:len(APIKeystring)-1]
    result = searchFunction(query, APIKey, 10)
    text = ""
    for website in result:
        try:
            text += getWords(website)
        except TypeError:
            continue
    if text is not None:
        finalessay = SummerizeText(text)
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
    result = searchFunction(query, APIKey, 10)
    textList = []
    for website in result:
        try:
            text = getWords(website)
            if text is not None:
                textList.append(SummerizeText(text))
        except TypeError:
            continue
    return textList


if __name__ == '__main__':
   app.run(debug = True)