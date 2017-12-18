#bind = "0.0.0.0:8080"

def app(environ, start_response):
    #data = [i + '\n' for i in environ['QUERY_STRING'].split('&')]
    data = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    #data = ''
    #arr = environ["QUERY_STRING"].split("&");
    #for param in arr:
    #    data += param + "\n"
    #for key in environ:
        #data += key + "\n" #+ "\t:\t" + environ[key];
        #for val in environ[key]:
        #    date += val + ", "
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        #('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return data
