import platform

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
        print('\nUw systeem wordt niet ondersteund.')
        exit()

def logVinden():
    """
    Deze functie localiseert het Apache log.
    """
    distroNaam = distro()
    if distroNaam == 'debian':
        return '/var/log/apache2/access.log'

    elif distroNaam == 'centos':
        return '/var/log/httpd/access_log'
