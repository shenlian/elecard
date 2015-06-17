$(document).ready(
function()
{
  $("#nav ul li").hover(
    function() {
    $('.list',this).show("fast");
    },
    function() {
    $('.list',this).hide("fast"); 
    }
  );
}
);

