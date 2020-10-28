class ViewClass(object):

    def __init__(self, request, response):
        self.req = request
        self.res = response

    def post(self):
        headers = [('Content-Type', 'text/plain')]
        self.res('200 OK', headers)

        data = 'post request'.encode('utf-8')

        return [data]

    def get(self):

        headers = [('Content-Type', 'application/json')]
        self.res('200 OK', headers)

        data = 'get request'.encode('utf-8')

        return [data]
