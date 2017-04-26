from modules import logParse
from collections import defaultdict

def aantalStatus():
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
