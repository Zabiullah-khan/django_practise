
x=0
function underline() {
	
	var line = document.getElementById('linez');
	line.style.width=x+'vmin';
	x++;
	console.log(x);
	if  (x==55) {
		
		clearInterval(stp)
	
	}	

}stp=setInterval(underline,20);
