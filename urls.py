from typing import Dict
from cgi import escape, FieldStorage
import cgi
from urllib.parse import parse_qs
from pprint import pprint

from response import Response

URLS: Dict[str, 'Path'] = {}


class Path(object):

    def __init__(self, url: str, view):
        self.url = url
        self.view = view

        URLS[self.url] = self

    def as_view(self, request, response):
        method = request.get('REQUEST_METHOD')
        x = self.view(request, response, method=method)
        return x


def my_json_test(environ, res, *args, **kwargs):
    data = {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55
    }

    if kwargs.get('method') == 'POST':

        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        print(post['name'].value)
        # word = post['word']
        # print('word is {}'.format(word.value))

        return Response(data=data).to_json()
    else:
        return Response(data='404').html_response()


Path('/', my_json_test)

'''
FileNotFoundError'''

'''
priyansh singh hello world
'''
