import urllib.request
import pyperclip
import logging
logging.basicConfig(filename='store_ip.log', level=logging.INFO, format='%(levelname)s : %(asctime)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
def pip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8') # gets the Public IP
    pyperclip.copy(external_ip)  # copies public IP to clipboard
    logging.info(external_ip)    # logs to a file to later use 
pip()
