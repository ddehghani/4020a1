from dataclasses import dataclass
from datetime import date
import xml.etree.ElementTree as ET
import requests
import time

@dataclass
class Article():
    ArticleTitle: str
    pubDate: date

def main():
    PATH_TO_SOURCE_XML = './4020a1-datasets.xml'
    ESEARCH_BASE_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    PATH_TO_OUTPUT_FILE = 'groupID_result.xml'
    articles = extractArticles(PATH_TO_SOURCE_XML) [0:10]
    ids = getIdsByAPICall(articles,ESEARCH_BASE_URL)
    assert len(ids) == len(articles) , "some articles could not be found"
    createXMLfromIds(PATH_TO_OUTPUT_FILE,ids, articles)

def createXMLfromIds(outfile: str, ids: list[int], articles: list[Article]) -> None:
    article_set = ET.Element('PubmedArticleset')
    for art, id in zip(articles, ids):
        article = ET.SubElement(article_set,'PubmedArticle')
        pmid = ET.SubElement(article,'PMID')
        pmid.text = str(id)
        articleTitle = ET.SubElement(article,'ArticleTitle')
        articleTitle.text = art.ArticleTitle
    with open(outfile, 'wt') as file:
        file.write(ET.tostring(article_set, encoding='utf8', method='xml').decode('utf8'))

def getIdsByAPICall(articles: list[Article], baseurl) -> list[int]:
    result = []
    failCount = 0
    for article in articles:
        params = {'db': 'pubmed', 'term': article.ArticleTitle, 'field': 'title'}
        try:
            root = ET.fromstring(requests.get(baseurl, params=params).text)
            result.append(int(root.find('IdList')[0].text))
            resultCount = root.find('Count').text
            if resultCount != '1':
                # print(f'{article.ArticleTitle = }')
                # print(f'{resultCount = }')
                failCount += 1
        except Exception as e:
            print(e)
            failCount += 1
        time.sleep(0.2) #api call limit rate
    # print(f'{len(result) * 100 / (len(result) + failCount)}:.2f%')
    return result

def extractArticles(sourceFile: str) -> list[Article]:
    root = ET.parse(sourceFile).getroot()
    return [ Article(ArticleTitle.text,  
                        date( int(PubDate[0].text), 
                        convertMonthToNum(PubDate[1].text), 
                        1 if len(PubDate) < 3 else int(PubDate[2].text))) 
                for (ArticleTitle, PubDate) in zip(root.iter('ArticleTitle'),root.iter('PubDate'))]

def convertMonthToNum(month: str) -> int:
    source = { 'Jan': 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug': 8, 'Sep': 9, 'Oct' : 10, 'Nov': 11, 'Dec' : 12}
    return source.get(month)

if __name__ == '__main__':
    main()