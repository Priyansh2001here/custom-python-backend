from webob import Request, Response


class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):

        print('called')

        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def route(self, path):

        print('route')

        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def handle_request(self, request):
        response = Response()

        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, response)
                return response


app = API()


@app.route("/home")
def home(request, response):
    response.data = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.data = "Hello from the ABOUT page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.data = f"Hello, {name}"
