from modules import logParse
from collections import defaultdict

def uniekeHosts():
    """
    Deze functie print alle unieke hosts welke voorkomen in het log.
    De hosts worden in een list gezet en later geprint.
    Geimporteerde modules:
    - logParse
    """
    hosts = []

    logList = logParse.logParse()
    for dict in logList:
            hosts.append(dict['host'])

    hostsDict = defaultdict(int)
    for host in hosts:
        hostsDict[host] += 1

    aantal = len(hostsDict)

    print()
    print('\nEr zijn ' + str(aantal) + ' unieke hosts welke connectie hebben gehad met de webserver.\n')

    nummer = 1
    for host in hostsDict.items():
        print(str(nummer) + '. ' + str(host[0]) + ' heeft ' + str(host[1]) + ' keer een request gestuurd.')
        nummer += 1
    #nummer = 1
    #for host in hostsDict.items():
    #    print(str(nummer) + ". " + str(host[nummer - 1]))
    #    nummer += 1
