from cgi import parse_qs, escape

def application(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'subject' in parameters:
        subject = escape(parameters['subject'][0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'''Hello %(subject)s Hello %(subject)s!''' % {b'subject': subject}]