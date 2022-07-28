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
	
def tablegen(table):
	print('<table>')
	for row in table:
		print('<tr>')
		for item in row:
			print('<td>'+item+'</td>')
		print('</tr>')
	print('</table>')

def modtable(arr):
	if len(arr[0])<len(arr[1]):
		if len(arr[2])>len(arr[1]):
			maxlen=2
		else:
			maxlen=1
	elif len(arr[0])>=len(arr[1]):
		maxlen=0
	else:
		maxlen=2
	table=[]
	for i in range(len(arr[maxlen])):
		row = []
		for j in range(3):
			if len(arr[j])>i:
				row.append(arr[j][i])
			else:
				row.append('')
		table.append(row)
	return table
	
def tablegen2(arr):
	table = modtable(arr)
	tablegen(table)
