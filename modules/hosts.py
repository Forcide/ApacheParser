from modules import logParse

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

    hosts = list(set(hosts))
    aantal = len(hosts)

    print('\nEr zijn ' + str(aantal) + ' unieke hosts welke connectie hebben gehad met de webserver.\n')

    nummer = 1
    for host in hosts:
        print(str(nummer) + ". " + str(hosts[nummer - 1]))
        nummer += 1
