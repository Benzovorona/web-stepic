from cgi import parse_qs
def app(environ, start_response):
    """Simplest possible application object"""
    s = environ['QUERY_STRING']
    s =s.replace('&', '\n')
    print(s)
    # for param in environ.keys():
    # 	print((param, environ[param]),'\n')
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain')
    ]
    start_response(status, response_headers)
    return iter([s.encode('utf-8')])