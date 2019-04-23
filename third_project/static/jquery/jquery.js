$(window).scroll(function(){
	if($(this).scrollTop() > 1)
		{
			$("#main").addClass('shrink');
		}
	else
		{
			$("#main").removeClass('shrink');
		}
});
