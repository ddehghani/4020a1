import xml.etree.ElementTree as ET
import requests # must use pip install requests for this to work

root = ET.parse('4020a1-datasets.xml').getroot()
#print(root)

articleTitleList = []
pubYearList = []
pubMonthList = []
pubDayList = []
#iterCount = 0
for (ArticleTitle, PubDate) in zip(root.iter('ArticleTitle'),root.iter('PubDate')):
    # print(ArticleTitle.text.split()[:3], PubDate[0].text, PubDate[1].text, PubDate[2].text)
    articleTitleList.append(ArticleTitle.text.split()[:3])
    #print(ArticleTitle.text.split()[:3],end="")
    try:
        pubYearList.append(PubDate[0].text)
        #print(PubDate[0].text,end="")
    except:
        pubYearList.append('')
    try:    
        pubMonthList.append(PubDate[1].text)
        #print(PubDate[1].text,end="")
    except:
        pubMonthList.append('') 
    try:
        pubDayList.append(PubDate[2].text)
        #print(PubDate[2].text)
    except:
        pubDayList.append('')
    #print(pubDayList)
    # iterCount = iterCount + 1
    # print(iterCount + articleTitleList[iterCount] + pubYearList[iterCount] + pubMonthList[iterCount] + pubDayList[iterCount])
    # print(articleTitleList[articleTitleList.index(ArticleTitle)] + pubYearList[pubYearList.index(PubDate)] + pubMonthList[pubMonthList.index(PubDate)] + pubDayList[pubDayList.index(PubDate)])
#
articleInfo = [list(a) for a in zip(articleTitleList, pubYearList,pubMonthList,pubDayList)]
print(articleInfo[1])


for article in articleInfo:
    # https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=
    x = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+article[0][0]+'&retmax=3&datetype=pdate')

    print(x.text)


# press python script.py in terminal to run this
#press python -V  to check if python 3 is installed