$(document).ready(function(){
	$("#loadMore").on('click',function(){
		var _currentProducts=$(".box").length;
		var _limit=$(this).attr('data-limit');
		var _total=$(this).attr('data-total');
		// Start Ajax
		$.ajax({
			url:'/load-more-data',
			data:{
				limit:_limit,
				offset:_currentProducts
			},
			dataType:'json',
			beforeSend:function(){
				$("#loadMore").attr('disabled',true);
			},
			success:function(res){
				$("#demo").append(res.data);
				$("#loadMore").attr('disabled',false);

				var _totalShowing=$(".box").length;
				if(_totalShowing==_total){
					$("#loadMore").remove();
				}
			}
		});
		// End
	});
})