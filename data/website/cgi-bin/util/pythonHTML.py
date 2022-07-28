def header(scripts=[]):
	print("Content-type:text/html\r\n\r\n")
	print("<html>")
	print("<head>")
	print("<title>Hello - Second CGI Program</title>")
	print('<script src="/javascript/scripts.js"></script>')
	for i in scripts:
		print('<script>'+i+'</script>')
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
	print(makelink(string, string))
	
def makelink(link, text):
	return '<a href="'+link+'">'+text+'</a>'	
	
def makelinkonclick(link, onclick, text):
	return '<a onclick="'+onclick+'"href="'+link+'" target="_blank">'+text+'</a>'

def strong(string):
	return '<strong>'+string+'</strong>'

def makebutton(function, params, text):
	return '<button onclick="'+function+'('+','.join(['\''+str(i).strip()+'\'' for i in params])+')">'+text+'</button>'

def invisrefresh():
	print('<button id="refresh-invis" onClick="window.location.reload();" style="display:none">Refresh Page</button>')
	
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
	elif len(arr[0])>=len(arr[2]):
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

def modlinks(arr, yearindex, projectindex):
	for i in range(len(arr[2])):
		arr[2][i] = makebutton('deleteuser',[arr[2][i], arr[0][yearindex], arr[1][projectindex]], arr[2][i])
		#arr[2][i] = makebutton('showrefresh',[], arr[2][i])
	for i in range(len(arr[1])):
		arr[1][i]= makelink('modifyprojectsselect.py?year='+arr[0][yearindex]+'&projectcode='+arr[1][i], arr[1][i])
	for i in range(len(arr[0])):
		arr[0][i]= makelink('modifyprojectsselect.py?year='+arr[0][i], arr[0][i])

def tablegen2(arr, yearindex, projectindex):
	modlinks(arr, yearindex, projectindex)
	if yearindex!=-1:
		arr[0][yearindex] = strong(arr[0][yearindex])
	if projectindex!=-1:
		arr[1][projectindex] = strong(arr[1][projectindex])
	table = modtable(arr)
	tablegen(table)
