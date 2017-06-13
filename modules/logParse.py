from modules import logVinden
import re

def logParse():
    """
    Deze functie opent de log en maakt hier eerst meerdere dictonaries van welke
    in een list komen te staan.
    Het eerste gedeelte geeft de delen van het log aan welke in meerdere
    dictonaries worden verwerkt om zoeken makkelijk te maken.
    Deze functie werkt voor de access log files op debian genaamd access.log
    Wanneer het een andere log is wordt deze doorverwezen naar de volgende functie.
    Geimporteerde modules:
    - logVinden
    - re
    """
    delen = [
        r'(?P<host>\S+)',
        r'\S+',
        r'(?P<user>\S+)',
        r'\[(?P<time>.+)\]',
        r'"(?P<request>.+)"',
        r'(?P<status>[0-9]+)',
        r'(?P<size>\S+)',
        r'"(?P<referer>.*)"',
        r'"(?P<agent>.*)"',
    ]
    patroon = re.compile(r'\s+'.join(delen)+r'\s*\Z')

    logLocatie = logVinden.logVinden()

    logLines = [line.rstrip('\n') for line in open(logLocatie)]

    try:
        logList = []
        for logLine in logLines:
            m = patroon.match(logLine)
            logDict = m.groupdict()
            logList.append(logDict)

        return logList

    except:
        return logParseZonderAgent()

def logParseZonderAgent():
    """
    Deze functie opent de log en maakt hier eerst meerdere dictonaries van welke
    in een list komen te staan.
    Het eerste gedeelte geeft de delen van het log aan welke in meerdere
    dictonaries worden verwerkt om zoeken makkelijk te maken.
    Deze functie werkt voor meerdere logs waar er geen referer en agent worden
    aangegeven zoals access_log.
    Wanneer het een andere log is wordt deze doorverwezen naar de volgende functie.
    Geimporteerde modules:
    - logVinden
    - re
    """
    delen = [
        r'(?P<host>\S+)',
        r'\S+',
        r'(?P<user>\S+)',
        r'\[(?P<time>.+)\]',
        r'"(?P<request>.+)"',
        r'(?P<status>[0-9]+)',
        r'(?P<size>\S+)',
    ]
    patroon = re.compile(r'\s+'.join(delen)+r'\s*\Z')

    logLocatie = logVinden.logVinden()

    logLines = [line.rstrip('\n') for line in open(logLocatie)]

    try:
        logList = []
        for logLine in logLines:
            m = patroon.match(logLine)
            logDict = m.groupdict()
            logList.append(logDict)

        return logList

    except:
        return logParseZonderUser()

def logParseZonderUser():
    """
    Deze functie opent de log en maakt hier eerst meerdere dictonaries van welke
    in een list komen te staan.
    Het eerste gedeelte geeft de delen van het log aan welke in meerdere
    dictonaries worden verwerkt om zoeken makkelijk te maken.
    Deze functie werkt voor epa-http.txt.
    Wanneer deze functie niet met succes uitgevoerd kan worden wordt er een
    foutmelding weergegeven.
    Geimporteerde modules:
    - logVinden
    - re
    """
    delen = [
        r'(?P<host>\S+)',
        r'\[(?P<time>.+)\]',
        r'"(?P<request>.+)"',
        r'(?P<status>[0-9]+)',
        r'(?P<size>\S+)',
    ]
    patroon = re.compile(r'\s+'.join(delen)+r'\s*\Z')

    logLocatie = logVinden.logVinden()

    logLines = [line.rstrip('\n') for line in open(logLocatie)]

    try:
        logList = []
        for logLine in logLines:
            m = patroon.match(logLine)
            logDict = m.groupdict()
            logList.append(logDict)

        return logList

    except:
        print('\nLog kon niet met succes uitgelezen worden!')
        exit()
