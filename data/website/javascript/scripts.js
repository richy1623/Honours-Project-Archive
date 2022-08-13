let width=500;
let height=500;
var selectedbutton;
var oldcolor;
var path;
var year;

function showrefresh() {
	elem=document.getElementById("refresh-invis")
	if(elem !== undefined && elem !== null){
		elem.style.display = "block";
	}
}

function deleteuser(user, year, project){
	if (window.confirm("Do you really want to delete "+user+"?")) {
		window.open("modifyprojectsdelete.py?student="+user+"&year="+year+"&project="+project, "delete", "width="+width+",height="+height);
		showrefresh();
	}
}
function adduser(year, project){
	window.open("addusertoproject.py?year="+year+"&project="+project, "delete", "width="+width+",height="+height);
	showrefresh();
}

function setyear(newyear){
	year=newyear
}

function selectfile(identity, newpath){
	resetcolor()
	selectedbutton=document.getElementById(identity);
	if(selectedbutton !== undefined && selectedbutton !== null){
		oldcolor=selectedbutton.style.backgroundColor;
		selectedbutton.style.backgroundColor='#0AA1DD';
		path=newpath
	}
}
function resetcolor(){
	if(selectedbutton !== undefined && selectedbutton !== null){
		selectedbutton.style.backgroundColor=oldcolor;
	}
}
function deletefile(){
	if(path !== undefined && path !== null){
		if (window.confirm("Do you really want to delete "+selectedbutton.innerText+"?")) {
			window.open("deletefile.py?year="+year+"&path="+path+"&filename="+selectedbutton.innerText, "Delete File", "width="+width+",height="+height);
			showrefresh();
		}
	}
}
function renamefile(){
	if(path !== undefined && path !== null){
		window.open("renamefile.py?year="+year+"&path="+path+"&oldfilename="+selectedbutton.innerText, "Rename File", "width="+width+",height="+height);
		showrefresh();
	}
}
function openfile(){
	let selectfile = selectedbutton.innerText;
	if(path !== undefined && path !== null && selectfile !== undefined && selectfile !== null){
		url="manageproject.py?";
		var pathdir
		if (path==""){
			pathdir=[]
		}else{
			pathdir=path.split("/");
		}
		pathdir.push(selectfile);
		pathdir = pathdir.slice(1);
		for(let i=0;i<pathdir.length;i++){
			pathdir[i]="d"+(i+1)+"="+pathdir[i];
		}
		url = url+pathdir.join("&");
		window.open(url,"_self")
	}
}
function addmetadata(){
	if(path !== undefined && path !== null){
		window.open("addmetadata.py?year="+year+"&path="+path+"&filename="+selectedbutton.innerText, "Add Metadata", "width="+width+",height="+height);
	}
}
function viewgivenproject(year, projectcode){
	window.open("view/"+year+"/"+projectcode+"/"+projectcode+".zip/", "Project View");
}
function viewproject(){
	let projectcode = document.getElementById("button00").innerText;
	window.open("zipproject.py?year="+year+"&projectcode="+projectcode, "Project Zipping").close();
	window.open("view/"+year+"/"+projectcode+"/"+projectcode+".zip/", "Project View");
}
function submitfile(){
	if (window.confirm("Are you ready to submit your project for moderation?")) {
		let projectcode = document.getElementById("button00").innerText;
		window.open("submitproject.py?year="+year+"&projectcode="+projectcode, "Submitting Project", "width="+width+",height="+height)
	}
	
}

function addfile(){
	let selectfile = selectedbutton.innerText;
	if(path !== undefined && path !== null && selectfile !== undefined && selectfile !== null){
		window.open("addfile.py?year="+year+"&path="+path+"&filename="+selectfile, "Add File", "width="+width+",height="+height);
		showrefresh();
	}
}
function highlightdir(identity2){
	let pathbutton=document.getElementById(identity2);
	if(pathbutton !== undefined && pathbutton !== null){
		pathbutton.style.backgroundColor='#79DAE8';
	}else{
		console.log(identity2+' not found')
	}
} 
function approveproject(year, project){
	if (window.confirm("Approve "+project+" to be added to archive?")) {
		window.open("approveprojects.py?year="+year+"&projectapprove="+project, "Approve Project", "width="+width+",height="+height);
		showrefresh();
	}
}
function denyproject(year, project){
	let reason=window.prompt("Reason for rejecting project "+project);
	if (reason !== null) {
		window.open("approveprojects.py?year="+year+"&projectdeny="+project+"&reason="+reason, "Deny Project", "width="+width+",height="+height);
		showrefresh();
	}
}
