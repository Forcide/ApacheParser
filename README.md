# ApacheParser
ApacheParser is a project made for school by Ramses 'Forcide' Houps.

This project parses the access log from the Apache Webserver.

It can give information about hosts that visited the Webserver or 404 status reports.

# Installation
No additional installation of modules needed.

To run the program, run:
```
python3 main.py
```

To use the mail function, rename the settings.ini-example to settings.ini and insert your gmail username and password.

Please note that it only works with gmail.

# Log location
This script is build to automatically find the Apache log.

Please note that it only works with Debian and CentOS.

You can override this by changing the 'file' setting in the settings.ini and placing the log file in the same directory.
