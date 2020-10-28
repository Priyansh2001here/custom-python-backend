# from backend.response import Response
#
# from pprint import pprint as pp
#
#
# #
#
#
# # def app(env, start_response):
# #     headers = [('Content-Type', 'application/json')]
# #     start_response('200 OK', headers)
# #     test = ujson.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# #     test1 = test.encode('utf-8')
# #     return [test1]
#
#
# def app(req, res):
#     template_name = 'index.html'
#     pp(req.get('PATH_INFO'))
#     pp(req.get('QUERY_STRING'))
#     pp(req.get('REQUEST_METHOD'))
#
#     # return response.Response(res, template_name=template_name).from_template()
#
#     return Response(data=template_name).to_json()
