from typing import Dict

from response import Response
URLS: Dict[str, 'Path'] = {}


class Path(object):

    def __init__(self, url: str, view):
        self.url = url
        self.view = view

        URLS[self.url] = self

    def as_view(self, request, response):
        x = self.view(request, response)
        return x


def my_view(req, res):
    # return Response(data="<h1>Heading {{name}}</h1>", context={'name': 'hehe'}).html_response()

    return Response(template_name='index.html', context={'name': 'hehe'}).from_template()


def shivank(req, res):
    return Response(template_name='hello.html').plain_response()

    # return Response(data="<h1>Heading {{name}}</h1>").plain_response()


def shivank_json(req, res):
    data = {
        'shivank_is': 'jod',
        'priyansh_is': 'jod'
    }

    return Response(data=data).to_json()


Path('/', my_view)
Path('/shivank', shivank)
Path('/shivank-json', shivank_json)

'''
FileNotFoundError'''

'''
priyansh singh hello world
'''
