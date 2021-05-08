import requests # Getting text from websites
import html2text # Converting html pages to plain text
from googlesearch import search # Performing Google searches
from bs4 import BeautifulSoup
from markdown import markdown
import re

class Query:
    '''
    Query class handles the input question and fetches context from internet
    '''

    def __init__(self, query, n_links):
        '''
        constructor to handle attributes
        '''
        self.query = query
        self.n_links = n_links
        self.html_conv = html2text.HTML2Text()
        self.html_conv.ignore_links = True
        self.html_conv.escape_all = True

    
    def get_context(self):
        '''
        this is the most important function in class that returns context for given question
        '''
        text = []
        for link in self._query_pages():
            req = requests.get(link)
            if req.ok:
                text.append(self.html_conv.handle(req.text))
                text[-1] = self._format_text(text[-1])
        return text

    def _query_pages(self):
        '''
        private function that return google search links for a given query
        '''
        links = search(self.query)[1:self.n_links]
        print(links)
        return links

    def _markdown_to_text(self, markdown_string):
        """ Converts a markdown string to plaintext
        # md -> html -> text since BeautifulSoup can extract text cleanly
        """
        html = markdown(markdown_string)
        # remove code snippets
        html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
        html = re.sub(r'<code>(.*?)</code >', ' ', html)
        # extract text
        soup = BeautifulSoup(html, "html.parser")
        text = ''.join(soup.findAll(text=True))
        return text

    def _format_text(self,text):
        text = self._markdown_to_text(text)
        text = text.replace('\n', ' ')
        return text

if __name__ == "__main__":
    cls_obj = Query("what is the color of sky",3)
    print(cls_obj.get_context())