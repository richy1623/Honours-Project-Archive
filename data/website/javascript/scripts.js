function showrefresh() {
	elem=document.getElementById("refresh-invis")
	if(elem !== undefined && elem !== null){
		elem.style.display = "block";
	}
}

function deleteuser(user, year, project){
		console.log("RUNNING");
	if (window.confirm("Do you really want to delete"+user+"?")) {
		//console.log(window.location.pathname);
		//window.open("../page.html", "delete", "width=500,height=500");
		//var xhttp = new XMLHttpRequest(); 
		//xhttp.open("GET", "modifyprojectsdelete.py", true);
		//xhttp.send();
		window.open("modifyprojectsdelete.py?student="+user+"&year="+year+"&project="+project, "delete", "width=500,height=500");
		//var myWindow = window.open("", "MsgWindow", "width=200,height=100");
		//myWindow.document.write("<p>This is 'MsgWindow'. I am 200px wide and 100px tall!</p>");
		showrefresh();
	}
}
