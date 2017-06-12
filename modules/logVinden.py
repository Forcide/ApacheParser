import platform, os, configparser

def distro():
    """
    Deze functie zoekt uit welke distro gebruikt word.
    Geimporteerde modules:
    - platform
    """
    platformStr = platform.platform()

    if 'debian' in platformStr or 'ubuntu' in platformStr:
        return 'debian'

    elif 'centos' in platformStr:
        return 'centos'

    else:
        return 'anders'

def logVinden():
    """
    Deze functie localiseert het Apache log.
    Geimporteerde modules:
    - os
    - configparser
    """
    while True:
        if os.path.exists('settings.ini'):
            config = configparser.ConfigParser()
            config.read('settings.ini')
            fileNaam = config['File']['file']

            if fileNaam == 'NONE' or fileNaam == '':
                break

            if os.path.exists(fileNaam):
                return fileNaam

            else:
                print('\nHet log aangegeven in settings.ini kon niet gevonden worden.')
                print('Laat de \'file\' setting leeg of geef een correcte naam aan.')
                exit()

        else:
            break

    distroNaam = distro()

    if distroNaam == 'debian':
        return '/var/log/apache2/access.log'

    elif distroNaam == 'centos':
        return '/var/log/httpd/access_log'

    else:
        print('\nEr kon geen apache log (automatisch) gevonden worden op uw systeem.')
        print('Het kan zijn dat uw systeem niet ondersteund wordt, lees de README goed door!')
        print('Geef hierom de \'file\' setting in settings.ini aan.')
        exit()
