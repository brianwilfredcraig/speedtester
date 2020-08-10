import os
import re
import subprocess
import time
import logging

# create a logger for this app
logger = logging.getLogger('wifi_ssid_detector')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('wifi_ssid_detector.log')
fh.setLevel(logging.DEBUG)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(ch)
logger.addHandler(fh)

logger.info('about to call subprocess.check_output')

netsh_output = subprocess.Popen("netsh wlan show interfaces", shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
logger.info('wifi_ssif=>%s<', netsh_output)

outputArray = netsh_output.splitlines(False)
logger.info('outputArray=>%s<', outputArray)

outputArrayNoSpaces = [x.replace(' ','') for x in outputArray]
logger.info('outputArrayNoSpaces=>%s<', outputArrayNoSpaces)

ssidArray = [s for s in outputArrayNoSpaces if s.startswith("SSID")]
logger.info('ssidArray=>%s<', ssidArray)

if (len(ssidArray) > 0) :
    wifi_ssid = ssidArray[0]
else :
    wifi_ssid = 'ETHERNET'

logger.info('wifi_ssid=>%s<', wifi_ssid)


# wifi_ssid = subprocess.Popen("netsh wlan show interfaces", shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')



# if "SchoolWifiName" in subprocess.check_output("netsh wlan show interfaces"):
    # print "I am on school wifi!"