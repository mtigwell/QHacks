from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
import indicoio
from summa import summarizer
import re
import requests

indicoio.config.api_key = '10b9bc05e39205de419a80cc3263ea3c'

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

