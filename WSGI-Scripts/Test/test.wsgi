#copied from here
#http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/

#minor moification since i am using the defult system through apache2 so 
#it looks for application not hello_world
def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    
    return [str.encode(output)]