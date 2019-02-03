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
import re


indicoio.config.api_key = '10b9bc05e39205de419a80cc3263ea3c'

f = open("apikey.txt", "r")
APIKeystring = f.read()
APIKey = APIKeystring[10:len(APIKeystring) - 1]


app = Flask(__name__)
CORS(app)

# API for doing search
@app.route('/search', methods=['GET'])
def searchAPI():
    search_term = request.args.get('search')
    num_results = int(request.args.get('results'))
    print(search_term, num_results)
    result = generateArticles(search_term, num_results)
    return jsonify(result)

@app.route('/essay', methods=['GET'])
def gen_essay():
    search_term = request.args.get('search')
    num_results = int(request.args.get('results'))
    count = int(request.args.get('count'))
    print(search_term, num_results, count)
    result = generateEssay(search_term, num_results, count)
    return jsonify([{'summary': result, 'url': "Essay"}])

# API for expanding summary
@app.route('/expand', methods=['GET'])
def expand():
    url = request.args.get('url')
    print(url)

    text = getWords(url)

    result = {
        'summary': SummerizeText(text, 800)
    }

    return jsonify(result)

def searchFunction(query, num, startIndex = 1):
    if num > 10: num = 10
    if num < 1: num = 1
    try:
        content = requests.get("https://www.googleapis.com/customsearch/v1?key="+APIKey+"&cx=004968834634498115028:9rcxpfpfjsc&q="+query+"&num="+str(num)+"&start="+str(startIndex))
        unpacked = content.json()
        results = unpacked["items"]
        resultList = []
        urlList = []
        for i in range(len(results)):
            try:
                resultList.append(results[i]["pagemap"]["metatags"][0])
            except KeyError:
                print("Skipped: No Metatags")
                continue
        for result in resultList:
            try:
                result['og:url'][0]
                if result['og:url'][0] == 'h':
                    urlList.append(result['og:url'])
            except KeyError:
                print("Skipped: No og:url")
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


def SummerizeText(text, word=200):
    t = summarizer.summarize(text, words=word)
    t = re.sub(r'\[.*?\]','', t)
    t = re.sub(r'\<.*?\>','', t)
    t = re.sub(r'\s ','',t)
    return t


def generateEssay(query, number=10, word_count=None):
    result = searchFunction(query, number)
    text = ""
    for website in result:
        try:
            text += getWords(website)
        except TypeError:
            continue
    if text is not None:
        essay = SummerizeText(text, word_count)
        finalessay = removeRedundancy(essay)
        print(finalessay)
    else:
        print("Error Occurred")
    return finalessay


def generateArticles(query, number):
    textList = []
    startIndex = 1
    while len(textList) < number:
        result = searchFunction(query, number, startIndex)
        for website in result:
            try:
                text = getWords(website)
                if text is not None:
                    summary = SummerizeText(text)
                    if summary is not None:
                        summarydone = removeRedundancy(summary)
                        textList.append({'summary': summarydone, 'url': website})
            except TypeError:
                print("Skipped:" + website)
                continue
        startIndex += 10
    return textList[:number]


def findall(inpstr, sub):
    ptr = 0
    indexlist = []
    while ptr < len(inpstr)-1:
        index = inpstr.find(sub, ptr, len(inpstr)-1)
        if index == -1:
            return indexlist
        indexlist.append(index)
        ptr = index+1
    return indexlist


def removeString(inpstr, index, remove):
    newstr = inpstr[0:index]
    newstr2 = inpstr[index+remove-1:]
    return newstr+" "+newstr2


def removeRedundancy(givenstr):
    indexlist = findall(givenstr, "\n")
    for ind in indexlist[::-1]:
        givenstr = removeString(givenstr, ind, 2)
    periodIndex = findall(givenstr, ".")

    for i in range(len(periodIndex)-2):
        if periodIndex[i+1]-periodIndex[i] == periodIndex[i+2]-periodIndex[i+1]:
            if givenstr[periodIndex[i]] == givenstr[periodIndex[i+1]]:
                givenstr = removeString(givenstr, periodIndex[i], periodIndex[i + 1] - periodIndex[i])
    return givenstr


if __name__ == '__main__':
    app.run(debug=True)