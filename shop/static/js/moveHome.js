function scrollFunction(){
  // var fatherElement = document.getElementsByTagName("body");
  var elmnt = document.getElementById("header");
  var fatherElement = document.documentElement.clientHeight;

  // var windowHeight = window.innerHeight;
  // var x = elmnt.scrollLeft;
  var vertMovement = fatherElement.scrollTop;

  elmnt.style.paddingTop = vertMovement + "px" ;
  // elmnt.style.color = "#" + 101010;
document.getElementById ("subheader").innerHTML = "Horizontally: " + fatherElement + "px";
}
