def header(scripts=[]):
	print("Content-type:text/html\r\n\r\n")
	print("<html>")
	print("<head>")
	print("<title>Honours Archive</title>")
	print('<script src="/javascript/scripts.js"></script>')
	for i in scripts:
		print('<script>'+i+'</script>')
	print("</head>")
	print("<body>")

def close():
	print("</body>")
	print("</html>")

def p(string):
	print('<p>'+str(string)+'</p>')

def h(string, level=1):
	print('<h'+str(level)+'>'+str(string)+'</h'+str(level)+'>')

def br():
	print('<br />')
	
def a(string):
	print(makelink(string, string))
	
def makelink(link, text):
	return '<a href="'+link+'">'+str(text)+'</a>'	
	
def makelinkonclick(link, onclick, text):
	return '<a onclick="'+onclick+'"href="'+link+'" target="_blank">'+text+'</a>'

def strong(string):
	return '<strong>'+string+'</strong>'

def makebutton(function, params, text):
	return '<button onclick="'+function+'('+','.join(['\''+str(i).strip()+'\'' for i in params])+')">'+text+'</button>'

def makebuttonidentity(function, params, text, identity):
	return '<button id="'+identity+'" onclick="'+function+'('+','.join(['\''+str(i).strip()+'\'' for i in params])+')">'+text+'</button>'

def script(function):
	print('<script type="text/javascript">')
	print(function)
	print('</script>')

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
		
def highlightprojectdir(dirid):
	script('highlightdir("'+dirid+'")')
	
def highlightpath(selected)	:
	for index, s in enumerate(selected):
		highlightprojectdir('button'+str(index)+str(s))

def modbuttons(arr, selected):
	path=[]
	for i in range(len(arr)):
		if i<len(selected):
			path.append(arr[i][selected[i]])
		for index, item in enumerate(arr[i]):
			identity='button'+str(i)+str(index) #to set the id html property
			arr[i][index] = makebuttonidentity('selectfile', [identity, '/'.join(path[:i])], arr[i][index], identity)

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
	if arr == []:
		p('No files in directory')
		return
	modbuttons(arr, selected)
	table = modtable(arr)
	tablegen(table)
	highlightpath(selected)
	
def projectmenu():
	print('<div class="menu">')
	h('Menu', 2)
	print(makebutton('openfile', [], 'Open'))
	print(makebutton('deletefile', [], 'Delete'))
	print(makebutton('addfile', [], 'Add File to Project'))
	print(makebutton('addmetadata', [], 'Add Metadata to Project'))
	print(makebutton('renamefile', [], 'Rename'))
	br()
	print(makebutton('viewproject', [], 'View Project'))
	print(makebutton('submitfile', [], 'Submit'))
	print('</div>')
	invisrefresh()
	#script('alert("ok");')

def createuploadformcsv(year):
	print('<form enctype = "multipart/form-data" action = "addprojectscsv.py" method = "post">')
	print('<p>Year: <input type = "text" name = "year" /></p>')
	print('<p>Upload File: <input type = "file" name = "uploadfile" /></p>')
	print('<p><input type = "submit" value = "Upload" /></p>')
	print('</form>')
	
def createuploadform(filecontextnames, filecontextvalues):
	print('<form enctype = "multipart/form-data" action = "addfile.py" method = "post">')
	print('<p>Upload File: <input type = "file" name = "uploadfile" /></p>')
	print('<input type="checkbox" name="unzip" value="True" /><label>Unzip this file</label>')
	print('<p><input type = "submit" value = "Upload" /></p>')
	for i in range(len(filecontextnames)):
		print(' <input type="hidden" name="'+filecontextnames[i]+'" value="'+filecontextvalues[i]+'">')
	print('</form>')
	
def createrenamefileform(year, path, oldfilename):
	p('Renaming file '+oldfilename)
	print('<form action="renamefile.py">')
	print('<label>New name for the file:</label><input type="text" name="newfilename" />')
	print('<input type="hidden" name="year" value="'+year+'" />')
	print('<input type="hidden" name="path" value="'+path+'" />')
	print('<input type="hidden" name="oldfilename" value="'+oldfilename+'" />')
	br()
	print('<input type="submit" value="Rename">')
	print('</form>')

def createmetadataform(projectcode, year, path, filename):
	p('Please input metadata below')
	print('<form action="addmetadata.py" method="get">')
	print('<label>Title of Project:</label><input type="text" name="title" /><br />')
	for i in range(1,5):
		print('<label>Student '+str(i)+':</label><input type="text" name="student'+str(i)+'" /><br />')
	print('<label>Supervisor of Project:</label><input type="text" name="supervisor" /><br />')
	print('<input type="hidden" name="year" value="'+year+'" />')
	print('<input type="hidden" name="path" value="'+path+'" />')
	print('<input type="hidden" name="filename" value="'+filename+'" />')
	print('<input type = "submit" value = "Upload" />')
	print('</form>')
