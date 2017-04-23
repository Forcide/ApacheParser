import platform, os

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
    """
    distroNaam = distro()

    if os.path.exists('access.log'):
        return 'access.log'

    elif distroNaam == 'debian':
        return '/var/log/apache2/access.log'

    elif distroNaam == 'centos':
        return '/var/log/httpd/access_log'

    else:
        print('\nUw systeem wordt niet ondersteund.')
        exit()
