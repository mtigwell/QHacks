from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq




# for i in len(text[len(text) - 1][:]):
#     if ord((text[len(text) - 1][i]) > 126 or ord(text[len(text) - 1][i]) < 32:
#         text.pop()
#     break


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

    print(text)
    return data



url = 'https://www.history.com/topics/ancient-history/alexander-the-great'
url = "http://www.bbc.co.uk/history/historic_figures/alexander_the_great.shtml"
url = 'https://en.wikipedia.org/wiki/Alexander_the_Great'
url = 'https://www.ancient.eu/Alexander_the_Great/'
url = "https://en.wikipedia.org/wiki/American_Revolutionary_War"
url= "https://www.history.com/topics/american-revolution/american-revolution-history"

string = getWords(url)
print()
print(string)
print()








