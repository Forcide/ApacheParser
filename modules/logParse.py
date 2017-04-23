from modules import logVinden
import re

def logParse():
    delen = [
        r'(?P<host>\S+)',                   # host %h
        r'\S+',                             # indent %l (unused)
        r'(?P<user>\S+)',                   # user %u
        r'\[(?P<time>.+)\]',                # time %t
        r'"(?P<request>.+)"',               # request "%r"
        r'(?P<status>[0-9]+)',              # status %>s
        r'(?P<size>\S+)',                   # size %b (careful, can be '-')
        r'"(?P<referer>.*)"',               # referer "%{Referer}i"
        r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
    ]
    patroon = re.compile(r'\s+'.join(delen)+r'\s*\Z')

    logLocatie = logVinden.logVinden()

    with open(logLocatie) as log:
        logLines = log.readlines()
    logLines = [line.rstrip('\n') for line in open(logLocatie)]

    logList = []
    for logLine in logLines:
        m = patroon.match(logLine)
        logDict = m.groupdict()
        logList.append(logDict)

    return logList
