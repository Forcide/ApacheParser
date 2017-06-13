def menu():
    """
    Deze functie voert het menu uit.
    Allereest worden de keuzes geprint waarna een keuze gegeven kan worden.
    De keuze word terug gegeven aan het hoofdprogramma.
    """
    while True:
        print('\n1) Print of mail het volledige log')
        print('2) Print de top drie meest bezochte webpagina\'s')
        print('3) Print (aantal) unieke hosts')
        print('4) Print de status meldingen (aantal)')
        print('5) Zoek letters of woorden uit het log')
        print('6) Stop')

        try:
            keuze = int(input('Wat is uw keuze? '))

            if keuze < 1 or keuze > 6:
                raise ValueError

        except ValueError:
            print('\nGebruik cijfers 1 t/m 6 voor het invoeren van uw keuze!\n')
            continue

        return keuze

def menuAfsluiten():
    """
    Waarneer het programma klaar is vraagt deze functie of het menu opnieuw
    opgegeven moet worden.
    Deze keuze word terug gegeven aan het hoofdprogramma.
    """
    while True:
        try:
            terug = str(input('\nWilt u terug naar het hoofdmenu?(J/N) '))

            if terug == 'j' or terug == 'J':
                return 'J'

            elif terug == 'n' or terug == 'N':
                return 'N'

            else:
                raise ValueError

        except ValueError:
            print('\nGebruik \'J\' of \'N\' voor het invoeren van uw keuze!')
            continue
