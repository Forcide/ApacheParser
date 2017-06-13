from modules import menu, hosts, logMail, status, webpagina, zoekInLog

""""
Dit is de start file van het programma, hierin worden alle modules geladen en zo nodig uitgevoerd.
Het menu wordt gestart en de keuze wordt verwezen naar een van de modules.
Geimporteerde modules:
- menu
- hosts
- logMail
- status
- webpagina
- zoekInLog
"""

def main():
    keuze = menu.menu()

    if keuze == 1:
        logMail.logMail()

    elif keuze == 2:
        webpagina.bezochteWebpagina()

    elif keuze == 3:
        hosts.uniekeHosts()

    elif keuze == 4:
        status.aantalStatus()

    elif keuze == 5:
        zoekInLog.zoekInLog()

    elif keuze == 6:
        exit()

    hoofdmenu = menu.menuAfsluiten()

    if hoofdmenu == 'J':
        main()

    elif hoofdmenu == 'N':
        exit()

main()
