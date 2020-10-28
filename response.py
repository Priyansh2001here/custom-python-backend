from jinja2 import Template
import os
import ujson
from typing import Dict

import exceptions
import config

BASE_DIR = os.path.relpath(os.getcwd())

# TEMPLATES_DIR = (os.path.join(os.path.relpath(os.getcwd(), config.TEMPLATES_DIR), config.TEMPLATES_DIR))

try:
    TEMPLATES_DIR = os.path.join(BASE_DIR, config.TEMPLATES_DIR)
except AttributeError as _:
    TEMPLATES_DIR = (os.path.join(BASE_DIR, 'templates'))


class Response(object):

    def __init__(self, data: str or Dict[str, str] = None, template_name: str = None, context=None):
        self.data = data
        self.context = context
        self.template_name = template_name

    @staticmethod
    def __response(data, content_type):
        valid_content_types = frozenset(('application/json', 'text/plain', 'text/html'))

        if content_type not in valid_content_types:
            raise exceptions.ContentTypeNotSupported(content_type)
        headers = [
            ('Content-Type', content_type)
        ]

        data = data.encode('utf-8')
        return data, headers

    def to_json(self):
        data = ujson.dumps(self.data)
        content_type = 'application/json'

        return self.__response(data, content_type)

    def from_template(self):

        template_as_str = ""

        template_path = f'{TEMPLATES_DIR}/{self.template_name}'

        try:
            with open(template_path) as f:
                template_as_str = f.read()
        except FileNotFoundError as _:
            raise exceptions.TemplateNotFound(self.template_name, TEMPLATES_DIR)

        t = Template(template_as_str)
        if self.context:
            data = t.render(self.context)
        else:
            data = t.render()

        content_type = 'text/html'

        return self.__response(data, content_type)

    def html_response(self):
        t = Template(self.data)

        if self.context:
            data = t.render(self.context)
        else:
            data = t.render()

        content_type = 'text/html'

        return self.__response(data, content_type)

    def plain_response(self):
        data = self.data
        content_type = 'text/plain'

        return self.__response(data, content_type)
