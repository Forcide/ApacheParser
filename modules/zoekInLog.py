from modules import logVinden

def zoekInLog():
    logLocatie = logVinden.logVinden()

    with open(logLocatie) as log:
        logLines = log.readlines()

    listNummer = 0

    while True:
        try:
            zoekInput = str(input('\nTyp het woord waar u op wilt zoeken: \n'))

            if zoekInput == '' or zoekInput == ' ':
                raise ValueError

            else:
                for string in logLines:
                    if zoekInput in string:
                        print(string)
                    listNummer += 1
                return

        except ValueError:
            print('\nVerkeerde input, probeer opnieuw!')
            continue
