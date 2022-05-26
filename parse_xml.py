from bs4 import BeautifulSoup
import requests
import lxml


def parse_xml():
    """Your script must return the content of <data> section from the file test.xml"""
    url = "http://upload.itcollege.ee/~aleksei/test.xml"
    xml_content = requests.get(url).content
    soup = BeautifulSoup(xml_content, 'xml')
    titles = soup.find_all("data")
    
    for title in titles:
        word = title.get_text()
        return str(word.strip())
