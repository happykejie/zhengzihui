/**
 * Created by zss-manong on 2016/3/23.
 */
$(document).ready(function(){
    //使每个筛选标签的前10个之后的标签隐藏
    //标签数量不大于8个的，隐藏更多按钮。
    $(".f-labels").each(function(){
       if($(this).children("li").length <= 8){
           $(this).parent().next(".more").hide();
       }else{
           $(this).children("li:gt(7)").hide();//表示大于第7个的，开始索引从0开始
       }
    });

    //使多选的确定和取消按钮消失
    var $m_a = $(".multiple-btn");
    $m_a.hide();

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

    //一行末尾更多和多选按钮的样式
    $(".multiple,.more").hover(function(){
        $(this).css("box-shadow","1px 1px 3px #c0c0c0");
    },function(){
        $(this).css("box-shadow","0px 0px 0px");
    });

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
    $(".more").each(function(){
        $(this).click(function(){
            var $f_head = $(this).parent().children(".f-head");
            var $f_row = $(this).parent();
            var $hidden_li = $(this).parent().children(".f-select").children("ul").children("li:gt(7)");//表示大于第7个的，开始索引从0开始
            var $first_li = $(this).parent().children(".f-select").children("ul").children("li:eq(0)"); //第一个的索引为0
            var $icon_change = $(this).children("a").children(".glyphicon");
            var $text_change = $(this).children("a").children(".text");

            // if($(".glyphicon").hasClass("glyphicon-chevron-up"))
            //类选择器不知道为什么不能用？
            if ($hidden_li.is(":visible"))   //必须保证li标签的数量大于8
            {
                $icon_change.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
                $text_change.text(" 更多");
                $hidden_li.hide();
                $first_li.show();//显示'全部'
                $f_head.height(33);
                $f_row.height(34);
            }
            else {
                $icon_change.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
                $text_change.text(" 收起");
                $hidden_li.show();
                $first_li.hide(); //隐藏'全部'
                var row_height = $f_row.css("height", "auto").height();
                $f_head.height(row_height-1);

            }
        })
    });

    //多选
    $(".multiple").each(function(){
        $(this).click(function(){  //以下所有后代元素选择器均可用find代替
            var $f_row = $(this).parent();
            var $f_head = $(this).parent().children(".f-head");
            var $multiple_btn = $(this).parent().children(".f-select").children(".multiple-btn");
            var $multiple_enter = $(this).parent().children(".f-select").children(".multiple-btn").children(".multiple-enter").children("a");
            var $hidden_li = $(this).parent().children(".f-select").children("ul").children("li:gt(7)");//表示大于第7个的，开始索引从0开始
            var $all_li = $(this).parent().children(".f-select").children("ul").children("li");
            var $first_li = $(this).parent().children(".f-select").children("ul").children("li:eq(0)"); //第一个的索引为0
            var $last_li = $(this).parent().children(".f-select").children("ul").children("li:last-child");//指的是li元素的父元素（ul）的最后一个子元素。
            var $more = $(this).prev(".more");


            $(this).hide();
            $more.hide();
            $last_li.css("margin-bottom","40px");
            if($hidden_li.length > 0){
                $hidden_li.show();
            }
            $multiple_btn.show();
            $f_row.css("background-color","#EFECEB");
            $first_li.hide(); //隐藏'全部'
            var row_height = $f_row.css("height", "auto").height();
            $f_head.height(row_height-1);
            $all_li.each(function(){
                $(this).find("a").unbind(".filter");
            });
            $all_li.each(function(){
                $(this).unbind("click.simple");
                $(this).bind("click.multiple",function(){
                    if($(this).hasClass("selected")){
                        var selected_length = $(this).parent().children("li.selected").length;
                        if(selected_length < 2){ //增加多选时的样式
                            $multiple_enter.removeClass("active").addClass("disabled");
                        }
                        $(this).removeClass("selected");
                        if($(this).is($last_li)){     //判断是不是最后一个li标签，因为最后一个li标签为了让下面的按钮存在一些间隔，额外设置了margin值40px
                            $(this).css("margin","0px 15px 40px 15px");
                        }else{
                            $(this).css("margin","0px 15px");   //恢复原来的margin值
                        }

                    }else{
                        var selected_length = $(this).parent().children("li.selected").length;
                        if(selected_length === 0){
                            $multiple_enter.removeClass("disabled").addClass("active");
                        }
                        $(this).addClass("selected");
                        //因为selected样式会增加外边框的宽度1px，相当于margin都增加了1，所以会相对应的减少margin的值与边框相呼应
                        //设置margin
                        if($(this).is($last_li)){     //判断是不是最后一个li标签，因为最后一个li标签为了让下面的按钮存在一些间隔，额外设置了margin值40px
                            $(this).css("margin","0px 15px 40px 15px");
                        }else{
                            $(this).css("margin","0px 15px");   //恢复原来的margin值
                        }
                    }
                    //li边框的hover样式
                    $(this).hover(function(){
                        $(this).css("border-color","#D11C00");
                    },function(){
                        $(this).css("border-color","#a8a8a8");
                    });

                });
            });
        });
    });


    //多选-取消所有选择
    $(".multiple-delete").each(function() {
        $(this).click(function () {
            var $f_row = $(this).parent().parent().parent();
            var $f_head = $(this).parent().parent().parent().children(".f-head");
            var $multiple_btn = $(this).parent();
            var $multiple_enter = $(this).prev(".multiple-enter").children("a");
            var $hidden_li = $(this).parent().parent().children("ul").children("li:gt(7)");//表示大于第7个的，开始索引从0开始
            var $all_li = $(this).parent().parent().children("ul").children("li");
            var $first_li = $(this).parent().parent().children("ul").children("li:eq(0)"); //第一个的索引为0
            var $last_li = $(this).parent().parent().children("ul").children("li:last-child");
            var $more = $(this).parent().parent().parent().children(".more");
            var $multiple = $(this).parent().parent().parent().children(".multiple");
            var $icon_change = $(this).parent().parent().parent().children(".more").children("a").children(".glyphicon");
            var $text_change = $(this).parent().parent().parent().children(".more").children("a").children(".text");
            //使多选时，多选标签的效果消失
            $all_li.each(function () {
                $(this).unbind("click.multiple");
                $(this).bind("click.simple",function(){
                    var key_name = $(this).parent().parent().prev(".f-head").children("span").attr("id");
                    var value = $(this).children("a").text();
                    window.location.href = "/filter_labels/?"+key_name+"="+key_name+"&filterkeys="+value;       
                });
                if($(this).hasClass("selected")){  //增加多选时的样式
                    $(this).removeClass("selected");
                    $(this).css("margin","0px 15px");//恢复原来的margin ,此时不用判断是否是最后一个
                }
                if($multiple_enter.hasClass("active")){
                    $multiple_enter.removeClass("active").addClass("disabled");
                }

                $(this).find("a").bind("mouseenter.filter",function(){
                    $(this).css({"color":"#D11C00","font-weight":600});
                });
                $(this).find("a").bind("mouseleave.filter",function(){
                    $(this).css({"color":"#7b7b7b","font-weight":500});
                });
            });
            //其他样式
            $icon_change.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
            $text_change.text(" 更多");
            if ($hidden_li.length > 0) {
                $hidden_li.hide();
                $more.show();
            }
            $multiple_btn.hide();
            $last_li.css("margin-bottom", "20px");
            $f_row.css("background-color", "transparent");//div默认背景色为透明的，如果设置成白色的将遮盖住阴影的颜色。
            $multiple.show();
            $first_li.show();//显示'全部'
            $f_head.height(33);
            $f_row.height(34);
        });
    });


    //多选-确定
	$("#filter .multiple-enter > a").click(function(){
        if($(this).hasClass("active")){
            var multiple = [];
            var $labels = $(this).parent().parent().prev(".f-labels");
			var key_name = $labels.parent().prev().children("span").attr("id");
			console.log(key_name);
            $labels.find(".selected > a").each(function(){
                multiple.push($(this).text());
            });
			window.location.href = "/filter_labels/?"+key_name+"="+key_name+"&filterkeys="+String(multiple);
            
    }
	});

    //单选
    $("#filter .f-labels  li").bind("click.simple",function(){
            var key_name = $(this).parent().parent().prev(".f-head").children("span").attr("id");
            var value = $(this).children("a").text();
            window.location.href = "/filter_labels/?"+key_name+"="+key_name+"&filterkeys="+value;       
    });
	
 



})


