from modules import logParse
from collections import defaultdict

def aantalStatus():
    """
    Deze functie print het aantal statusmeldingen per statusmelding.
    Er wordt een dictionary bijgehouden met de statussen en bij elke status
    die voorbij komt in de for loop wordt er een bij opgeteld.
    Dit aantal wordt aan het einde geprint.
    Geimporteerde modules:
    - logParse
    - defaultdict
    """
    statussenList = []

    logList = logParse.logParse()
    for dict in logList:
        statussenList.append(dict['status'])

    statussenDict = defaultdict(int)
    for status in statussenList:
        statussenDict[status] += 1

    print()

    for status,aantal in statussenDict.items():
        if aantal == 1:
            print('Er is 1, ' + str(status) + ' status melding' )

        else:
            print('Er zijn ' + str(aantal) + ', ' + str(status) + ' status meldingen')
