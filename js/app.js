$(document).ready(function(){
    $('ul.tabs').tabs();
    $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();

  });

$(".linker").on('click', function() {
   
    var c = $(this).attr("class");
    c= c.split(' ')[0];
    c =  '#' + c;
    $(c).find("a").toggleClass("active");
    
});
