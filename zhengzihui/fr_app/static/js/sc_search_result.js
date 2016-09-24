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
	 


})


