class ContentTypeNotSupported(Exception):
    __slots__ = ()

    def __init__(self, requested_content_type):
        self.requested_content_type = requested_content_type

        super().__init__(self.requested_content_type)


class InvalidMethod(Exception):
    __slots__ = ()

    def __init__(self, requested_method: str):
        self.message = f'{requested_method} not supported'

        super().__init__(self.message)


class TemplateNotFound(FileNotFoundError):
    __slots__ = ()

    def __init__(self, file_name, directory):
        self.message = f'file name {file_name} could not be located in {directory}'

        super().__init__(self.message)
