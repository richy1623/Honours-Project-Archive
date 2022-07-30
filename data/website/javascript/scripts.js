function showrefresh() {
	elem=document.getElementById("refresh-invis")
	if(elem !== undefined && elem !== null){
		elem.style.display = "block";
	}
}

function deleteuser(user, year, project){
	if (window.confirm("Do you really want to delete"+user+"?")) {
		window.open("modifyprojectsdelete.py?student="+user+"&year="+year+"&project="+project, "delete", "width=500,height=500");
		showrefresh();
	}
}
function adduser(year, project){
	window.open("addusertoproject.py?year="+year+"&project="+project, "delete", "width=500,height=500");
	showrefresh();
}
var selectedbutton
var path
function setfile(identity, newpath){
	resetcolor()
	selectedbutton=document.getElementById(identity);
	if(selectedbutton !== undefined && selectedbutton !== null){
		selectedbutton.style.backgroundColor='#FF0000';
		path=newpath
	}
	console.log(path)
}
function resetcolor(){
	if(selectedbutton !== undefined && selectedbutton !== null){
		selectedbutton.style.backgroundColor='#FFFFFF';
	}
}
