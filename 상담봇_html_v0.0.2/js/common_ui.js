$(document).ready(function(){
	
	var atc = $('#aside > ul > li');
		atc.addClass('hid');
	$('#aside > ul > li > a').click (function() {
		var atcm = $(this).parents('#aside > ul > li:first');
		if(atcm.hasClass('hid')) {
			atcm.removeClass('hid').addClass('active').find('ul').slideUp(150);
		} else {
			atcm.removeClass('active').addClass('hid').find('ul').slideDown(150);
		}
		return false;
	});

	$(".tbl_list tr.view").on("click", function(){
	    $(this).toggleClass("open").next(".fold").toggleClass("open");
	});

	//tab
	var $tabsNav    = $('.tabs'),
		$tabsNavLis = $tabsNav.children('li'),
		$tabContent = $('.tab_cont');
	$tabsNav.each(function() {
		var $this = $(this);
		$this.next().children('.tab_cont').stop(true,true).hide().first().show();
		$this.children('li').first().addClass('on').stop(true,true).show();
	});
	$tabsNavLis.on('click', function(e) {
		var $this = $(this);
		$this.siblings().removeClass('on').end().addClass('on');
		$this.parent().next().children('.tab_cont').stop(true,true).hide().siblings( $this.find('a').attr('href') ).fadeIn(0);
		e.preventDefault();
	});

	//layer_popup
	$('.layerpop').click(function(e) {
		e.preventDefault();
		
		var id = $(this).attr('href');
		var maskHeight = $(document).height();
		var maskWidth = $(window).width();
		
		$('#layermask').css({'width':maskWidth,'height':maskHeight});
		$('#layermask').fadeTo("",0.7);
	
		var winH = $(window).height();
		var winW = $(window).width();
              
		$(id).css('top',  winH/2-$(id).height()/2);
		$(id).css('left', winW/2-$(id).width()/2);
		$(id).fadeIn(500);
		$('body').addClass('body_scl');
	});
	$('.layer_close').click(function (e) {
		e.preventDefault();
		$('#layermask').fadeOut(500);
		$('.layerwrap2').fadeOut(500);
	});
	$(window).resize(function () { 
 		var box = $('.layerwrap2'); 
        var maskHeight = $(document).height();
        var maskWidth = $(window).width();      
        $('#layermask').css({'width':maskWidth,'height':maskHeight});               
        var winH = $(window).height();
        var winW = $(window).width();
        box.css('top',  winH/2 - box.height()/2);
        box.css('left', winW/2 - box.width()/2);
	});

});
 