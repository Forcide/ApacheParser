from modules import logParse
from collections import defaultdict
from operator import itemgetter
import heapq

def bezochteWebpagina():
    """
    Deze functie print de top drie meest bezochte webpagina's.
    Er wordt een list gemaakt en hier worden requests aan toegevoegd
    wanneer dit geen 404 statusmeldingen bevat.
    Hierna wordt er een dict gemaakt welke deze request bijhoudt en telkens als
    een zelfde request voorbij komt in de for loop een bij opgeteld.
    Dit wordt gesorteerd op requests die het meeste voor kwamen en de top drie
    wordt geprint.
    Geimporteerde modules:
    - logParse
    - defaultdict
    - itemgetter
    - heapq
    """
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
