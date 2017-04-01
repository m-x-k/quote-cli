import fire
import requests
from bs4 import BeautifulSoup


class Quotes(object):

    url = "http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=%s"

    def getQuote(self, number):
        response = requests.get(self.url % number)
        if response.status_code == 200:
            data = response.json()
            return ["%s: %s" % (q.get("title"), BeautifulSoup(q.get("content"), "html.parser").text) for q in data]
        else:
            return "ERROR: %s" % response.text

if __name__ == '__main__':
    fire.Fire(Quotes)
