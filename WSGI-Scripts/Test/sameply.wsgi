

def application(environ, start_response):
    status = '200 OK'
    output = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<title>Wellington Radio Yacht Club - New Zealand</title>
</head>

<body>

<!--Title block of the web page -->
<div id="Title_Div">
	<br />
	<h1 id="Title">Wellington Radio Yacht Club - New Zealand</h1>
</div>

</body>

</html>'''

    response_headers = [('Content-type', 'html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    
    return [str.encode(output)]