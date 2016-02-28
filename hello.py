from cgi import parse_qs
def app(environ, start_response):
    """Simplest possible application object"""
    data = parse_qs(environ['QUERY_STRING'])
    d =''
    for key in data.keys():
        for i in range(len(data[key])):
            d+=key+':'+str(i)+'\n'
    print(d)
    d = d.encode('utf-8')
    # for param in environ.keys():
    # 	print((param, environ[param]),'\n')
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain')
    ]
    start_response(status, response_headers)
    return iter([d])