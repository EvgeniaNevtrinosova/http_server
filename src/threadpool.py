import socket
from threading import Thread

from src.handler import Handler
from src.constants import BUFFER, HOST

import sys


class Worker(Thread):
    def __init__(self, socket, document_root):
        Thread.__init__(self)
        self.socket = socket
        self.document_root = document_root

    def run(self):
        while True:
            conn, adr = self.socket.accept()

            conn.settimeout(1.0)

            try:
                data = conn.recv(BUFFER)

                if len(data.strip()) == 0:
                    conn.close()

                else:
                    conn.sendall(Handler(data.decode(),
                                        self.document_root).get_response())
                    conn.close()

            except socket.timeout:
                conn.close()
                continue

            except socket.error:
                continue

            except Exception as e:
                continue


class ThreadPool:
    def __init__(self, thread_count, port, document_root):
        self.port = port
        self.document_root = document_root
        self.workers_pool = []
        self.thread_count = int(thread_count)

    def run(self):
        mysocket = socket.socket()

        mysocket.bind((HOST, self.port))
        mysocket.listen(10)

        for i in range(0, self.thread_count):
            worker = Worker(mysocket, self.document_root)
            self.workers_pool.append(worker)
            worker.start()

        for w in self.workers_pool:
            w.join()
