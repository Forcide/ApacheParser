from modules import logVinden

def zoekInLog():
    """
    Deze functie zoekt uit welke distro gebruikt word.
    Geimporteerde modules:
    - platform
    """
    logLocatie = logVinden.logVinden()

    with open(logLocatie) as log:
        logLines = log.readlines()

    listNummer = 0

    while True:
        try:
            zoekInput = str(input('\nTyp het woord waar u op wilt zoeken: '))

            if zoekInput == '' or zoekInput == ' ':
                raise ValueError

            else:
                print()
                niksGevonden = 1
                for string in logLines:
                    if zoekInput in string:
                        print(string)
                        niksGevonden = 0
                    listNummer += 1

                if niksGevonden != 0:
                    print('Er is niks gevonden.')

                return

        except ValueError:
            print('\nVerkeerde input, probeer opnieuw!')
            continue
