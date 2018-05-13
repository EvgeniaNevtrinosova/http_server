from src.threadpool import ThreadPool

import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read_file(open(r'./httpd.conf'))

document_root = config.get('config', 'document_root')
port = int(config.get('config', 'listen'))

thread_number = 10

server = ThreadPool(thread_number, port, document_root)
server.run()
