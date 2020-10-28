from urls import URLS
from exceptions import InvalidMethod

VALID_METHODS = frozenset(('GET', 'POST'))


def app(environ, start_response):
    path = environ.get('PATH_INFO')
    method = environ.get('REQUEST_METHOD')

    try:
        obj = URLS[path]
    except KeyError:
        headers = [('Content-Type', 'text/plain')]
        start_response('404', headers)
        data = '404 page not found'.encode('utf-8')
        return [data]

    if method not in VALID_METHODS:
        raise InvalidMethod(method)

    (view_obj, headers) = obj.as_view(environ, start_response)

    start_response('200 OK', headers)

    return iter([view_obj])
