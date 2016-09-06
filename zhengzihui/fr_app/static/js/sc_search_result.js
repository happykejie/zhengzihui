/**
 * Created by zss-manong on 2016/3/23.
 */
$(document).ready(function(){
    //使每个筛选标签的前10个之后的标签隐藏
    //筛选标签的hover样式
    $(".filter li>a").bind("mouseenter.filter",function(){
        $(this).css({"color":"#D11C00","font-weight":600});
    });
    $(".filter li>a").bind("mouseleave.filter",function(){
        $(this).css({"color":"#7b7b7b","font-weight":500});
    });

    //一行筛选样式的阴影效果

    $(".f-row").hover(function(){
        $(this).css("box-shadow","1px 2px 3px #c0c0c0");
    },function(){
        $(this).css("box-shadow","0px 0px 0px");
    });

    //修复进度条提示百分比溢出边框
    $(".info").each(function(){
        var $left1 = $(this).offset().left;
        var $left2 = $(this).prev(".progress-bar").offset().left;
        var $offleft = $left1 - $left2;
        if($offleft > 50){
            $(this).addClass("info-bug");
        }
    })

    //项目列表阴影以及进度条动画效果
    $(".list-content").hover(function(){
        $(this).css("box-shadow","0px 0px 10px #656565");
        var $bar = $(this).find(".progress-bar");
        if(! $bar.is(":animated")){
            var $width = $bar.next(".info").text();
            //$bar.animate({width:$width,opacity:"1"},200);   //有问题
            $bar.css("width",$width)//.css("opacity","1");             css方法有动画，神奇！
        }
    },function(){
        $(this).css("box-shadow","0px 0px 0px");
    });

    //更多
    //****提示：不能通过定义变量的形式对上一个变量进行引用，每一条选择器必须有$(this)，也就是变量初始化后不能在用于初始化另一个变量****
    //****绝对重要提示：当使用children后代选择器的时候，为了避免不必要的麻烦，应该尽量使用带参数的，比如元素名称或者类名，因为使用bootstrap存在before以及after的伪类，也算dom树结构的一个节点****
    //单选
    $("#filter .f-labels  li").bind("click.simple",function(){
            var key_name = $(this).parent().parent().prev(".f-head").children("span").attr("id");
            var value = $(this).children("a").text();
            window.location.href = "/free_require/supporting_center/filter_labels/?"+key_name+"="+key_name+"&filterkeys="+value;
    });
	 
    //滚动条到达底部触发ajax请求
    var times = 10  //定义全局请求数据的初始条数
    $(window).scroll(function(){
        if($("#load").is(":hidden")){ //用load的隐藏或者显示来标示一次请求是否在进行或者结束
            var $last = $(".list-content").last();//取得 class = list-content的最后一个元素，也就是最后一个项目详情方块。div YZ
			var bottom=$last.offset().top+$last.outerHeight();//最后一个元素底部距离浏览器窗口顶部的距离
			var scrollTop=document.documentElement.scrollTop||document.body.scrollTop||0;//滚动条距离
		    var windowHeight=document.documentElement.clientHeight||document.body.clientHeight||0;//窗口高度
            //上面算距离和，下面的判断是为什么，猜想是为了判断load这个div时候出现了吧？？
            if(scrollTop>=bottom-windowHeight){
                //console.log(bottom);
                //console.log(scrollTop);
                //console.log(windowHeight);
                $("#load").show();
                    $.ajax({method:"GET",url:"/search_result_load/",data:{"times":times},dataType:"json",success:function(data){
						if(data.length > 0){  //返回的数据不能为空
							$.each(data,function(index,obj){
                            $last.clone(true).appendTo("#list")// 传递参数true，使复制事件，默认为false
                            var $last_now = $(".list-content").last();
                            $last_now.find(".title > a").text(obj.item_name);
                            $last_now.find("a").attr("href","/item_details/?id="+obj.item_id);
                            $last_now.find("a > img").attr("src",obj.pic_url);
                            $last_now.find(".title > label").text(obj.item_about);
                            $last_now.find(".title > a").attr("href","/item_details/?id="+obj.item_id);
                            $last_now.children("span").text(obj.item_key);
                            $last_now.find(".benefit-num").text(obj.item_ga);
                            $last_now.find(".agency span").last().text(obj.pa);
                            $last_now.find(".info").css("left",obj.item_consume_time+"%").text(obj.item_consume_time+"%"); //注意控制style里的样式使用css，而不能使用attr
                            $last_now.find(".start").text(obj.item_publish);
                            $last_now.find(".stop").text(obj.item_deadtime);
                            $last_now.find(".sum").text(obj.order_num);
                            $last_now.find(".witch > a").attr("href","/item_details/?id="+obj.item_id);
                            //$last_now.animate({opacity:"1"},200);
                            });
                            $("#load").hide();
                            times += 5; //每次取5条数据
                            //console.log(times);
                            //console.log(data[0].fields.item_name);  //后台序列化的结果就是将整个对象和方法都序列化啦，而数据内容区域在fields里面
                            //console.log(data)
						}else{
							$("#load").html("<p>数据已经全部加载完毕啦，如果没有感兴趣的内容请移步其他网页！</p>");
						}
                         },error: function(XMLHttpRequest, textStatus, errorThrown) {
                         console.log(XMLHttpRequest.status);
                         console.log(XMLHttpRequest.readyState);
                         console.log(textStatus);
                         }})

            }
        }


    })




})


