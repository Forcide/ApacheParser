from modules import menu, uniekeHosts, logMail, status

""""
Dit is de start file van het programma, hierin worden alle modules geladen en zo nodig uitgevoerd.
Het menu wordt gestart en de keuze wordt verwezen naar een van de modules..
Geimporteerde modules:
- menu
- uniekeHosts
- logMail
- status
"""

def main():
    keuze = menu.menu()

    if keuze == 1:
        logMail.logMail()

    elif keuze == 2:
        uniekeHosts.uniekeHosts()

    elif keuze == 3:
        status.aantalStatus()

    elif keuze == 4:
        exit()

main()
