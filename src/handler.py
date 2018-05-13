import os
import re
import urllib.parse

import datetime

from src.constants import DATE_TEMPLATE, CONTENT_TYPE, RESPONSE_CODES, RESPONSE_OK, RESPONSE_FAIL, ALLOW_METHODS, MAIN_PAGE


class Request:
    def __init__(self):
        self.method = None
        self.path = None
        self.content_type = None


class Handler:
    def __init__(self, request_string, root_dir):
        self.code = None
        self.content = b''
        self.content_length = None
        self.content_type = None

        request = self.__parse_request(request_string)

        self.__make_response(request, root_dir)

    def __parse_request(self, request_string):
        request = Request()
        try:
            request.method = re.findall(r'^(\w+)', request_string)[0]
        except IndexError:
            pass

        try:
            request.path = re.findall(r'([^\s?]+)', request_string)[1]
            request.path = urllib.parse.unquote(request.path)
        except IndexError:
            request.path = None

        content_type = request.path.split('.')[-1]
        try:
            self.content_type = CONTENT_TYPE[content_type]
        except KeyError:
            self.content_type = "text/txt"

        return request

    def __make_response(self, request, root_dir):
        if request.method not in ALLOW_METHODS:
            self.code = RESPONSE_CODES["NOT_ALLOWED"]
            return

        filename = os.path.normpath(root_dir + request.path)

        if not(filename.startswith(os.path.normpath(root_dir))) or not(os.path.exists(os.path.join(filename))):
            self.code = RESPONSE_CODES["NOT_FOUND"]
            return

        if not(os.path.isfile(filename)):
            filename = os.path.join(filename, MAIN_PAGE)

            if not(os.path.isfile(filename)):
                self.code = RESPONSE_CODES["FORBIDDEN"]
                return


        try:
            with open(filename, 'rb') as f:
                self.code = RESPONSE_CODES["OK"]

                content = f.read()
                self.content_length = len(content)

                if request.method == 'GET':
                    self.content = content

        except IOError:
            print('File open error')
            pass

    def get_response(self):
        if RESPONSE_CODES["OK"]:
            return RESPONSE_OK.format(
                self.code,
                self.content_type,
                self.content_length,
                datetime.datetime.utcnow().strftime(DATE_TEMPLATE)
            ).encode() + self.content
        else:
            return RESPONSE_FAIL.format(self.code).encode()
