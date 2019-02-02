from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
import indicoio

indicoio.config.api_key = '10b9bc05e39205de419a80cc3263ea3c'


def getWords(url):
    my_url = url
    uClient= uReq(my_url)
    page_html=uClient.read()
    uClient.close()

    page_soup = Soup(page_html, "html.parser")
    paragraphs= page_soup.findAll('p')

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


    return data, text


def Summerize(url):
    string= indicoio.summarization(url)
    print(type(string))
    return string





