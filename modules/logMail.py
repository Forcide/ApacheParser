from modules import logVinden
from email.mime.text import MIMEText
import smtplib, os, configparser, datetime

def mailVerzenden(naarMail):
    """
    Deze functie verstuurd het log wanneer hier in het mail menu om gekozen wordt.
    Eerst wordt het log ingelezen voor de mail.
    Het account wordt opgevraagd bij de mailAccount functie.
    De mail wordt opgemaakt en verzonden.
    Geimporteerde modules:
    - logVinden
    - MIMEText
    - datetime
    - smtplib
    """
    logLocatie = logVinden.logVinden()

    with open(logLocatie) as log:
        bericht = MIMEText(log.read())

    accountList = mailAccount()
    login = accountList[0]
    wachtwoord = accountList[1]

    bericht['Subject'] = 'Apache log ' + datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    bericht['From'] = login
    bericht['To'] = naarMail

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(login, wachtwoord)
        server.send_message(bericht)
        server.quit()

        print('\nMail verzonden naar ' + naarMail + '!')

    except:
        print('\nKon mail niet verzenden!')

def mailAccount():
    """
    In deze functie wordt het mail account opgehaald uit de settings.ini en
    teruggeven aan de mailVerzenden functie.
    Geimporteerde modules:
    - configparser
    """
    try:
        account = []
        config = configparser.ConfigParser()
        config.read('settings.ini')
        account.append(config['Mail']['mail'])
        account.append(config['Mail']['password'])

    except:
        print('\nEr is een fout opgetreden, lees de README goed door!')
        exit()

    return account

def logMail():
    """
    Deze funcie fungeerd als een menu.
    Er wordt gevraagd of het log geprint of gemaild moet worden.
    Wanneer het printen is wordt het log geprint.
    Wanneer het mailen is wordt er naar het mail adres gevraagd waar het log
    heen gestuurd zal moeten worden.
    Dit mail adres wordt meegegeven aan de functie mailVerzenden.
    Geimporteerde modules:
    - logVinden
    - os
    """
    loop = 1
    while loop == 1:
        print('\nWat wilt u doen met het log?')
        print('1) Printen op het scherm')
        print('2) Mailen')

        try:
            keuze = int(input('Wat is uw keuze? '))

            if keuze <= 0 or keuze >= 3:
                raise ValueError

        except ValueError:
            print('\nGebruik cijfers 1 t/m 2 voor het invoeren van uw keuze!\n')
            continue

        loop = 0

    if keuze == 1:
        logLocatie = logVinden.logVinden()
        print('')
        with open (logLocatie) as log:
            print(log.read())

    elif keuze == 2:
        if os.path.exists('settings.ini'):
            loop = 1
            while loop == 1:
                try:
                    naarMail = input('\nNaar welk e-mail adres moet het log verstuurd worden? ')

                except ValueError:
                    print('\nGeen geldig e-mail adres!')
                    continue

                loop = 0

                mailVerzenden(naarMail)

        else:
            print('\nEr is geen settings.ini gevonden, lees de README goed door!')
            exit()
