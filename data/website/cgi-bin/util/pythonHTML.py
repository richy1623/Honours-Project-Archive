def header():
	print("Content-type:text/html\r\n\r\n")
	print("<html>")
	print("<head>")
	print("<title>Hello - Second CGI Program</title>")
	print("</head>")
	print("<body>")
	
def close():
	print("</body>")
	print("</html>")

def p(string):
	print('<p>'+string+'</p>')

def h(string):
	print('<h1>'+string+'</h1>')
	
def a(string):
	print('<a href="'+string+'">'+string+'</a>')
