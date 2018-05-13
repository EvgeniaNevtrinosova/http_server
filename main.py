from src.threadpool import ThreadPool

import configparser
from pathlib import Path
from parser_config import parser_config


# config = configparser.ConfigParser()
# config.read_file(open(r'./httpd.conf'))

# document_root = config.get('config', 'document_root')
# port = int(config.get('config', 'listen'))

try:
    config = parser_config()
    document_root = config['document_root']
except FileNotFoundError:
    document_root = './http-test-suite'

port = 80

thread_number = 10

server = ThreadPool(thread_number, port, document_root)
server.run()
