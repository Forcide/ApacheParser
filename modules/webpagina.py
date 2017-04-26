from modules import logParse
from collections import defaultdict
from operator import itemgetter
import heapq

def bezochteWebpagina():
    webpaginaList = []

    logList = logParse.logParse()
    for dict in logList:
        if dict['status'] != '404':
            webpaginaList.append(dict['request'])

    webpaginaDict = defaultdict(int)
    for request in webpaginaList:
        webpaginaDict[request] += 1

    print('\nDe meest bezochte webpagina\'s: ')

    webpaginaSorted = heapq.nlargest(3, webpaginaDict.items(), key=itemgetter(1))
    i = 1

    for webpagina,aantal in webpaginaSorted:
        webpaginaStr = webpagina
        webpaginaStr = webpaginaStr.replace('GET ', '')
        print(str(i) + '. ' + webpaginaStr[:-9])
        i += 1
