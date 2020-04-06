import os
import re
import subprocess
import time
import logging

# create a logger for this app
logger = logging.getLogger('speedtest')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('log_speedtest.log')
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

logger.info('about to call speedtest-cli')
response = subprocess.Popen('%PYTHON_HOME%\Scripts\speedtest-cli.exe --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
logger.info('completed call to speedtest-cli')
# logger.debug('response=>', response)

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')

try:
    f = open('output_speedtest.csv', 'a+')
    if os.stat('output_speedtest.csv').st_size == 0:
            f.write('Date,Time,Download,Upload,Ping\r')

    f.write('{},{},{},{},{}\r'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), download, upload, ping))

except Exception as e:
    logger.info('exception during file write')
    logger.error(e)