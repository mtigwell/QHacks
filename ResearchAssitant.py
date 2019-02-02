from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
import indicoio
from summa import summarizer
import re
import requests

indicoio.config.api_key = '10b9bc05e39205de419a80cc3263ea3c'

def getWords(url):
    # try:
    # uClient= uReq(url)
    # page_html = uClient.read()
    page_html = requests.get(url)
    # uClient.close()
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

    # except Exception:
    #     print("oops")


def SummerizeWebsite(url):
    string= indicoio.summarization(url)
    data = ""
    for i in range(len(string)):
        print(i)
        s = string[i]
        s = s.strip('\n')
        s = re.sub(r'\[.*?\]', '', s)
        print(string)
        data = data + " " + s
    return data


def SummerizeText(text):
    t = summarizer.summarize(text)
    t= re.sub(r'\[.*?\]','', t)
    t= t.strip('\n')
    t= t.strip('\t')
    print(t)
    return t

# url = "http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/"
# # url = "https://en.wikipedia.org/wiki/Alexander_the_Great"
# word = getWords(url)
# SummerizeText(word)
# print()
# print()
# word = SummerizeWebsite(url)
# print(word)

