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

def br():
	print('<br />')
	
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

def formlist(ls, action, multiple='', hidden=[]):
	print('<form action="'+action+'">')
	print('<label for="items">Choose an item:</label>')
	print('<select name="student" size="4" '+multiple+'>')
	for item in ls:
		print('<option value="'+item+'">'+item+'</option>')
	print('</select><br><br>>')
	for item in hidden:
		print('<input type="hidden" name="'+str(item[0])+'" value="'+str(item[1])+'">')
	print('<input type="submit">')
	print('</form>')

def maxarrlen(arr):
	mx = len(arr[0])
	for i in arr:
		if len(i)>mx:
			mx=len(i)
	return mx

def modtable(arr):
	maxlen = maxarrlen(arr)
	table=[]
	for i in range(maxlen):
		row = []
		for j in range(len(arr)):
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
	if len(arr[2])!=0:
		arr[2].append(makebutton('adduser',[arr[0][yearindex], arr[1][projectindex]], 'Add user'))
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

def tablegen3(arr, selected):
	for index, s in selected:
		arr[index][s] = strong(arr[index][s])
	table = modtable(arr)
	tablegen(table)
