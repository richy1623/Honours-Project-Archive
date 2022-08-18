from datetime import date

def banner():
	print('<nav class="navbar navbar-expand-md navbar-dark bg-dark">')
	print('<a class="navbar-brand" href="../index.html"><img id="logo-small" src="../images/logo-small.png" />University of Cape Town - Computer Science Honours Archive</a>')
	print('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">')
	print('<span class="navbar-toggler-icon"></span>')
	print('</button>')
	print('')
	print('<div class="collapse navbar-collapse mr-auto" id="navbarsExampleDefault">')
	print('<ul class="navbar-nav mr-auto">')
	print('<li class="nav-item"><div id="login"><a class="login-link" href="../login.html" onClick="login1(this.href); return false">Login / Register</a></div></li>')
	print('<li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>')
	print('<li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>')
	print('<li class="nav-item"><a class="nav-link" href="../users.html">Authors</a></li>')
	print('<li class="nav-item"><a class="nav-link" href="../search.html">Search</a></li>')
	print('<li class="nav-item"><a class="nav-link" href="../contact.html">Contact Us</a></li>')
	print('<li class="nav-item"><a class="nav-link" href="/cgi-bin/manageproject.py"><strong>Manage Project</strong></a></li>')
	print('</ul>')
	print('</div>')
	print('</nav>')

def bannersmall():
	print('<nav class="navbar navbar-dark bg-dark">')
	print('<img id="logo-small" style="height: 75px" src="../images/logo-small.png" />')
	print('<span class="navbar-brand float-right mr-5">Computer Science Honours Archive</span>')
	print('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">')
	print('</nav>')

def setuser(user):
	script('showUsername("'+user+'")')

def header(scripts=[]):
	print("Content-type:text/html\r\n\r\n")
	print('<!DOCTYPE html>')
	print("<html>")
	print("<head>")
	print("<title>Honours Archive</title>")
	print('<script src="/javascript/scripts.js"></script>')
	print('<script src="/scripts/login.js"></script>')
	for i in scripts:
		print('<script>'+i+'</script>')
		
	print('<meta name="viewport" content="width=device-width, initial-scale=1" />')
	print('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
	print('<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>')
	print('<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>')
	print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>')
	print('<link rel="stylesheet" type="text/css" href="../styles/bootstrapstyle.css"/>')
	print('')
	print('<!-- Font Awsome -->')
	print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />')

	print("</head>")
	print("<body>")

def close():
	print("</body>")
	print("</html>")

def smallp(string):
	print('<p class="smalltext">'+str(string)+'</p>')

def p(string):
	print('<p>'+str(string)+'</p>')

def smallh(string, level=1):
	print('<h'+str(level)+' class="smalltext">'+str(string)+'</h'+str(level)+'>')

def h(string, level=1):
	print('<h'+str(level)+'>'+str(string)+'</h'+str(level)+'>')

def br():
	print('<br />')
	
def hr():
	print('<hr />')

def a(string):
	print(makelink(string, string))
	
def makelink(link, text, classes=[]):
	return '<a href="'+link+'" class="'+' '.join(classes)+'">'+str(text)+'</a>'	
	
def makelinkonclick(link, onclick, text):
	return '<a onclick="'+onclick+'"href="'+link+'" target="_blank">'+text+'</a>'

def strong(string):
	return '<strong>'+string+'</strong>'

def makebuttonclass(function, params, cssclass, text):
	return '<button onclick="'+function+'('+','.join(['\''+str(i).strip()+'\'' for i in params])+')" class="'+cssclass+'">'+text+'</button>'

def makebutton(function, params, text):
	return makebuttonclass(function, params, 'btn btn-outline-primary', text)

def makebuttonidentity(function, params, text, identity):
	return '<button id="'+identity+'" onclick="'+function+'('+','.join(['\''+str(i).strip()+'\'' for i in params])+')" class="btn btn-outline-primary">'+text+'</button>'

def script(function):
	print('<script type="text/javascript">')
	print(function)
	print('</script>')

def invisrefresh():
	print('<button id="refresh-invis" class="btn btn-warning ml-3" onClick="window.location.reload();" style="display:none">Refresh Page</button>')
	
def tablegen(table):
	print('<table>')
	for row in table:
		print('<tr>')
		for item in row:
			print('<td>'+item+'</td>')
		print('</tr>')
	print('</table>')

def tablegenstyled(table, error='', hover=False):
	print('<table class="table'+(' table-hover' if hover else '')+'">')
	#table Header
	print('<thead class="thead-light">\n<tr>')
	for item in table[0]:
		print('<th scope="col">'+item+'</th>')
	print('</tr>\n</thead>')
	#rest of table
	for row in table[1:]:
		print('<tr>')
		for item in row:
			if len(item)==2:
				print('<td align="center" colspan="'+str(item[1])+'">'+item[0]+'</td>')
			else:
				print('<td>'+item+'</td>')
		print('</tr>')
	print(error)
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

def modbuttons(arr, dirs, selected):
	path=[]
	for i in range(len(arr)):
		if i<len(selected):
			path.append(arr[i][selected[i]])
		for index, item in enumerate(arr[i]):
			foldericon = ' <i class="fa fa-folder"></i>' if len(dirs)>0 and dirs[i][index] else ''
			identity='button'+str(i)+str(index) #to set the id html property
			arr[i][index] = makebuttonidentity('selectfile', [identity, '/'.join(path[:i])], arr[i][index]+foldericon, identity)

def modbuttons2(arr, yearindex, projectindex):
	for i in range(len(arr[2])):
		arr[2][i] = makebuttonclass('deleteuser', [arr[2][i], arr[0][yearindex], arr[1][projectindex]], 'btn btn-outline-danger', 'Remove '+arr[2][i])
		#arr[2][i] = makebutton('showrefresh',[], arr[2][i])
	if len(arr[2])!=0:
		arr[2].append(makebuttonclass('adduser', [arr[0][yearindex], arr[1][projectindex]], 'btn btn-outline-success', 'Add user'))
	for i in range(len(arr[1])):
		if i == projectindex:
			arr[1][i]= makebuttonclass('openprojectselectyp', [arr[0][yearindex], arr[1][i]], 'btn btn-outline-primary', arr[1][i])
		else:
			arr[1][i]= makebutton('openprojectselectyp', [arr[0][yearindex], arr[1][i]], arr[1][i])
	for i in range(len(arr[0])):
		if i == yearindex:
			arr[0][i]= makebuttonclass('openprojectselecty', [arr[0][i]], 'btn btn-outline-primary', arr[0][i])
		else:
			arr[0][i]= makebutton('openprojectselecty', [arr[0][i]], arr[0][i])

def tablegen2(arr, yearindex, projectindex):
	modbuttons2(arr, yearindex, projectindex)
	if yearindex!=-1:
		arr[0][yearindex] = strong(arr[0][yearindex])
	if projectindex!=-1:
		arr[1][projectindex] = strong(arr[1][projectindex])
	table = modtable(arr)
	table.insert(0, ['Year', 'Project Code', 'Students'])
	tablegenstyled(table)

def tablegen3(arr, dirs, selected):
	if arr == []:
		p('No files in directory')
		return
	modbuttons(arr, dirs, selected)
	table = modtable(arr)
	tablegen(table)
	highlightpath(selected)

def tablegen4(projects):
	tableform=[[strong('Projects'), strong('View Webpage'), strong('View Metadata'), strong('Approve'), strong('Deny')]]
	for year in projects:
		tableform.append([[strong(year[0]), 5]])
		for project in year[1]:
			projectlist=[]
			projectlist.append(project)
			projectlist.append(makebutton('viewgivenproject', [year[0], project], 'Webpage'))
			projectlist.append(makebutton('viewspecificmetadata', [year[0], project], 'Metadata'))
			projectlist.append(makebutton('approveproject', [year[0], project], 'Approve'))
			projectlist.append(makebutton('denyproject',  [year[0], project], 'Deny'))
			tableform.append(projectlist)
	if len(projects)==0:
		tablegenstyled(tableform, error='<tr class="table-danger"> <td class="table-danger" align="center" colspan="5">No projects pending moderation</td></tr>', hover=True)
	else:
		tablegenstyled(tableform)
	invisrefresh()
	
def projectmenu():
	print('<div class="menu">')
	h('Menu', 2)
	print(makebutton('openfile', [], 'Open'))
	print(makebutton('deletefile', [], 'Delete'))
	print(makebutton('addfile', [], 'Add File to Project'))
	print(makebutton('addmetadata', [], 'Add Metadata to Project'))
	print(makebutton('renamefile', [], 'Rename'))
	br()
	print(makebuttonclass('viewproject', [], 'btn btn-primary', 'View Project'))
	print(makebuttonclass('viewmetadata', [], 'btn btn-primary', 'View Metadata'))
	print(makebuttonclass('submitfile', [], 'btn btn-primary', 'Submit'))
	print('</div>')
	invisrefresh()
	#script('alert("ok");')

def createuploadformcsv(year):
	print('<form enctype = "multipart/form-data" action = "addprojectscsv.py" method = "post">')
	print('<p>Year: <input class="form-control" type = "text" name = "year" placeholder="'+str(date.today().year)+'" required /></p>')
	print('<p>Upload File: <input type="file" class="form-control-file"  name="uploadfile" required /></p>')
	print('<p><input type="submit" class="btn btn-primary" value = "Upload" /></p>')
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

def createmetadataform(projectcode, year):
	p('Please input metadata below')
	print('<form action="addmetadata.py" method="post" enctype = "multipart/form-data">')
	print('<label>Title of Project:</label><input type="text" name="title" /><br />')
	print('<label>Description of Project:</label><input type="textarea" name="description" /><br />')
	for i in range(1,5):
		print('<label>Student '+str(i)+':</label><input type="text" name="student'+str(i)+'" /><br />')
	print('<label>Supervisor of Project:</label><input type="text" name="supervisor" /><br />')
	print('<p>*Optional* Thumbnail Image for Project: <input type = "file" name = "image" accept="image/jpg" /></p>')
	print('<input type="hidden" name="year" value="'+year+'" />')
	print('<input type="hidden" name="projectcode" value="'+projectcode+'" />')
	print('<input type = "submit" value = "Submit" />')
	print('</form>')

def createprojectform():
	print('<form name="projectform" class="projectformclass" method="post" action="createproject.py">')
	print('<h2>Project Details</h2>')
	print('<span class="">Project Name:</span>')
	print('<input class="textbox" name="projectname" type="text"/>')
	print('<br/>')
	print('<span class="">Project Code:</span>')
	print('<input class="textbox" name="projectcode" type="text"/>')
	print('<br/>')
	print('<span class="">Project Year:</span>')
	print('<input class="textbox" name="projectyear" type="text"/>')
	print('<br/>')
	print('<hr/>')
	print('<h2>Student Details</h2>')
	for i in range(1,5):
		print('<span class="">Student Number '+str(i)+':</span>')
		print('<input class="textbox" name="student'+str(i)+'" type="text"/>')
		print('<br/>')
	print('<button class="" type="submit">Submit</button>')
	print('</form>')

def displayprojectapprovalpage(projects):
	tablegen4(projects)
	
def getnamefield(line):
	name = line[line.index('<')+1:line.index('>')]
	field = line[line.index('>')+1:line.rindex('<')]
	return [name, field]
	
def printmetadata(metadata, fields):
	for index in range(len(metadata)):
		metadata[index] = getnamefield(metadata[index])
	for line in metadata:
		if line[0] in fields:
			p(line[0].capitalize()+': '+strong(line[1]))
