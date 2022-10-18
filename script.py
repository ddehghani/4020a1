import xml.etree.ElementTree as ET
import requests # must use pip install requests for this to work

# root = ET.parse('4020a1-datasets.xml').getroot()
# print(root)
# for PubmedArticle in root.iter("ArticleTitle"):
#     print(PubmedArticle.text)

root = ET.parse('4020a1-datasets.xml').getroot()
print(root)

articleTitleList = []
yearCreatedList = []
monthCreatedList = []
dayCreatedList = []
for (ArticleTitle, DateCreated) in zip(root.iter('ArticleTitle'),root.iter('DateCreated')):
    print(ArticleTitle.text, DateCreated[0].text, DateCreated[1].text, DateCreated[2].text)
    articleTitleList.append(ArticleTitle.text)
    yearCreatedList.append(DateCreated[0].text)
    monthCreatedList.append(DateCreated[1].text)
    dayCreatedList.append(DateCreated[2].text)

# for PubmedArticle in root.iter("Article"):
    # for child in PubmedArticle:
    #     print(child.text)
    #     #if child.tag == ("ArticleTitle" or "DateCreated"): 
            

for PubmedArticle in root.iter("ArticleTitle"):
    x = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+PubmedArticle.text+'&field=ArticleTitle')

    print(x.text)



# press python script.py in terminal to run this
#press python -V  to check if python 3 is installed