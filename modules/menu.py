def menu():
    while True:
        print('\n1) Print of mail het volledige log')
        print('2) Print de top drie meest bezochte webpagina\'s')
        print('3) Print (aantal) unieke hosts')
        print('4) Print de status meldingen (aantal)')
        print('5) Stop')

        try:
            keuze = int(input('Wat is uw keuze? '))

            if keuze < 1 or keuze > 5:
                raise ValueError

        except ValueError:
            print('\nGebruik cijfers 1 t/m 5 voor het invoeren van uw keuze!\n')
            continue

        return keuze

def menuAfsluiten():
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
