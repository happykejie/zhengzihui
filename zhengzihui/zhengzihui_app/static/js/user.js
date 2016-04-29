/**
 * Created by zss-manong on 2016/4/28.
 */
$(document).ready(function(){

    //初始化效果
    $(".panel-body").first().parent().prev(".panel-heading").css("background-color","#FF404B");
    $("#load").hide();
    //标题点击效果
    $("#boxleft .panel-heading a").on("click.menu",function(){
            var $span = $(this).find("span");
            var $heading = $(this).parent().parent();
            var $hide = $(this).parent().parent().next().find(".panel-body");
            if($hide.is(":hidden")){
                $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-right");
                $heading.css("background-color","#FF404B");

            }else{
                $span.removeClass("glyphicon-chevron-right").addClass("glyphicon-chevron-down");
                $heading.css("background-color","#2B2F3E");
            }
    });

    $("#boxleft .panel-body >li >a").each(function(){
        $(this).click(function(){
            $("#load").show();
            var url = $(this).attr("id");
            console.log(url);
            $.ajax({method:"GET",url:url,dataType:"html",success:function(html){
                if(html.length > 0){  //返回的数据不能为空
                    $("#load").hide();
                    $("#boxright").html(html);
                }else{
                    $("#load").html("<p>请求的数据好像迷路啦！请重试！</p>");
                }
                console.log(html);
            },error: function(XMLHttpRequest, textStatus, errorThrown) {
                console.log(XMLHttpRequest.status);
                console.log(XMLHttpRequest.readyState);
                console.log(textStatus);
            }})
        })

    });


})
