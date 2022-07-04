$(document).ready(function() {
    $('.main-menu-click').click(function() {
    	$('body').toggleClass('menu-open');
	});
	
	 
	
$(document).ready(function() {
		if($(window).width() > 767) { 
			$('#latest-news-section').pinterest_grid({
				no_columns: 3,
				padding_x: 0,
				padding_y: 0,
				margin_bottom: 0,
				single_column_breakpoint: 480 
			}); 
		
		} else {
		   
		   $('#latest-news-section').pinterest_grid({
				no_columns: 2,
				padding_x: 0,
				padding_y: 0,
				margin_bottom: 0,
				single_column_breakpoint: 480
			}); 
		}
                
                if($(window).width() > 767) {
			$('#upcoming-event-section').pinterest_grid({
				no_columns: 3,
				padding_x: 0,
				padding_y: 0,
				margin_bottom: 0,
				single_column_breakpoint: 480 
			}); 
		
		} else {
		   
		   $('#upcoming-event-section').pinterest_grid({
				no_columns: 2,
				padding_x: 0,
				padding_y: 0,
				margin_bottom: 0,
				single_column_breakpoint: 480
			}); 
		}
  
      if($(window).width() > 991) { 
			$('#recent-news-section').pinterest_grid({
				no_columns: 3,
				padding_x: 0,
				padding_y: 0,
				margin_bottom: 0,
				single_column_breakpoint: 767
			}); 
		
		} else {
		   
		   $('#recent-news-section').pinterest_grid({
				no_columns: 2,
				padding_x: 0,
				padding_y: 0,
				margin_bottom: 0, 
				single_column_breakpoint: 767
			}); 
		}
  
	});
	
	
	$(window).load(function() {
		
	});
			
			
});