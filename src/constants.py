CONTENT_TYPE = {
    'html': 'text/html',
    'css': 'text/css',
    'js': 'application/javascript',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'swf': 'application/x-shockwave-flash'
}

RESPONSE_CODES = {
    'OK': '200 OK',
    'NOT_FOUND': '404 Not Found',
    'NOT_ALLOWED': '405 Method Not Allowed',
    'FORBIDDEN': '403 Forbidden'
}

RESPONSE_OK = 'HTTP/1.1 {}\r\n' \
    'Content-Type: {}\r\n' \
    'Content-Length: {}\r\n'\
    'Date: {}\r\n' \
    'Server: ThreadPoolPython\r\n\r\n'

RESPONSE_FAIL = 'HTTP/1.1 {}\r\n' \
    'Server: ThreadPoolPython'

DATE_TEMPLATE = '%a, %d %b %Y %H:%M:%S GMT'

MAIN_PAGE = 'index.html'

ALLOW_METHODS = ['HEAD', 'GET']

HOST = '0.0.0.0'

BUFFER = 1024