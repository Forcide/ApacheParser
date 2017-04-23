def menu():
    while True:
        print('1) Print of mail het volledige log')
        print('2) Print (aantal) unieke hosts')
        print('3) Print de status meldingen (aantal)')
        print('4) Stop')

        try:
            keuze = int(input('Wat is uw keuze? '))

            if keuze <= 0 or keuze >= 5:
                raise ValueError

        except ValueError:
            print('\nGebruik cijfers 1 t/m .... voor het invoeren van uw keuze!\n')
            continue

        return keuze
