# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from itertools import chain
import datetime 
import time
import json #用来将字典类型的数据序列化，然后传给模板以及js,不能序列化model实例
import jieba,p_alipay.alipay
from django.core import serializers #用来序列化model 传给js
from models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News,Tb_Notice,Tb_Notice_Class,Tb_Apage,Tb_Apage_Class,tb_album,tb_pic,tb_accessory,tb_Artificial_Representations,tb_Message,tb_MessageText,tb_SysMessage,tb_item,tb_item_pa,tb_item_class,tb_goods,tb_album,tb_pic,tb_article,tb_goods_evaluation,tb_goods_click,tb_goods_class,tb_order,tb_item_click,tb_area
# Create your views here.
def index(request):
	request.session['bumen']='全部'
	request.session['jibie']='全部'
	request.session['zhuangtai']='全部'
	#print (123)
	return render_to_response('index.html',{})


def Searchgoods(request):
    allthebumen=['经济与信息化','发展与改革','财政','科技','教育','文化','卫计','体育','知识产权','农业','林业','畜牧','渔业','粮食','中医药','国土','住建','交通','水利','能源','环保','商务','投资促进','工商','税务','民政','人社','扶贫','旅游','人民银行','银监','证监','保监','质监','药监','安监']
    a_items = []
    selected = {}
    flag = False
    ads=[]
    items=[]
    if (request.method=="GET"):	
        goodsname=request.GET.get("inputitem")
        #print (goodsname)
        #goodsname="精准医学研究"
        if goodsname is not None:
	#fenleisousuo	
            if  goodsname.encode("utf-8") in allthebumen:
                selected['bumen'] = goodsname.encode("utf-8")
		#print selected['bumen']
                request.session['bumen'] = goodsname.encode("utf-8")
                return HttpResponseRedirect('/search_result/')
	#xiangmusousuo        
	#分词
            seg_list = jieba.cut(goodsname,cut_all=False)
        #搜索
            for gname in seg_list:
                ads+=tb_item.objects.filter(item_name__contains = gname) #filter(someziduan__contains = something) 代表模糊过滤出包含something的所有object
        #去重复
            for i in ads: 
                if i not in items:
                    items.append(i)
                    #print i.item_name
            
	    
            for item in items:
                a_item = {}    
                a_item['item_id'] = item.item_id#获取项目id
                a_item['item_name'] = item.item_name#获取项目名字 
                a_item['item_ga'] = item.item_ga
                a_item['item_key'] = item.item_key
                a_item['item_about'] = item.item_about
                now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
                a_item['item_publish'] = item.item_publish.strftime('%Y.%m.%d')
                a_item['item_deadtime'] = item.item_deadtime.strftime('%Y.%m.%d')
                start_seconds = time.mktime(item.item_publish.timetuple())  #utc 0时区
                end_seconds = time.mktime(item.item_deadtime.timetuple())
                consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
                if consume_time > 100:
                    a_item['item_consume_time'] = 100
                    a_item['item_key'] = "已结束"
                else:
                    a_item['item_consume_time'] = int(consume_time)
                a_item['pa'] = tb_item_pa.objects.get(ipa_id=item.item_pa_id).ipa_name
                album = tb_album.objects.filter(album_type=0,affiliation_id=item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
                album_id = album.album_id
                a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
                a_item['order_num'] = len(tb_order.objects.filter(item_id=item.item_id))#获取项目对应订单的数量
                a_items.append(a_item)

    return render(request,'search_result.html',{'selected':selected,'flag':flag,'items':a_items})


#zss 点击搜索的下一级
def search_result(request):
#首次只返回10条数据
    a_items = []
    middle_items=[]
    tmiddle_items=[]
    items=[]
    selected = {}
    flag = False
    if 'bumen' in request.session:
        value = request.session['bumen']
        selected['bumen'] = value
        #print(selected['bumen'])
        flag = True
    else:
        selected['bumen'] = ''
    if 'jibie' in request.session:
        value = request.session['jibie']
        selected['jibie'] = value
        flag = True
    else:
        selected['jibie'] = ''
    if 'zhuangtai' in request.session:
        value = request.session['zhuangtai']
        selected['zhuangtai'] = value
        flag = True
    else:
        selected['zhuangtai'] = ''
	
	#bumenstr = selected['bumen'].encode("utf-8")
    #print(selected['bumen'])
    #jibiestr = selected['jibie'].encode("utf-8")
    #zhuangtaistr = selected['zhuangtai'].encode("utf-8")   
    allthebumen = ['经济与信息化','发展与改革','财政','科技','教育','文化','卫计','体育','知识产权','农业','林业','畜牧','渔业','粮食','中医药','国土','住建','交通','水利','能源','环保','商务','投资促进','工商','税务','民政','人社','扶贫','旅游','人民银行','银监','证监','保监','质监','药监','安监']
    allthejibie = ['县级财政资金','市级财政资金','省级财政资金','中央财政资金']
    allthezhuangtai = ['正在申报','截止申报']
    #items = tb_item.objects.all()
    #if  (selected['bumen'].encode("utf-8") is not '全部'):
    	#middle_items = items.objects.filter(item_about__contains = bumenstr)
    if  (selected['jibie'].encode("utf-8") != '全部'):
    	#print selected['jibie'].encode("utf-8")
    	#print list(selected['jibie'])
    	jibielist = (selected['jibie'].encode("utf-8")).split(',')
    	#print jibielist
    	for i in jibielist:
    		middle_items = chain(middle_items,(tb_item.objects.filter(item_level = (allthejibie.index(i)+1))))
    else:
    	middle_items=tb_item.objects.all()
    	'''for i in middle_items:
    		print(i.item_status)'''
    
    if  (selected['zhuangtai'].encode("utf-8") != '全部'):
    	#print(type(items))
    	#items = items(item_status = (allthezhuangtai.index(selected['zhuangtai'].encode("utf-8"))))
    	for i in middle_items:
    		if allthezhuangtai.index(selected['zhuangtai'].encode("utf-8")) == i.item_status:
    			tmiddle_items.append(i)
    #if  (selected['zhuangtai'].encode("utf-8") != '全部'):
    else:
    	tmiddle_items=middle_items
    	#for i in tmiddle_items:
    		#print (i.item_status)
    		
    if  (selected['bumen'].encode("utf-8") != '全部'):
    	bumenlist = (selected['bumen'].encode("utf-8")).split(',')
    	for i in tmiddle_items:
    		for j in bumenlist:
    			if j in (i.item_about).encode("utf-8"):
    				items.append(i) 		
    else:
    	#print (222)
    	items=tmiddle_items
	   
    
    #items = items[:10]//不够10条报错
    for item in items:
        a_item = {}    
        a_item['item_id'] = item.item_id#获取项目id
        a_item['item_name'] = item.item_name#获取项目名字 
        a_item['item_ga'] = item.item_ga
        a_item['item_key'] = item.item_key
        a_item['item_about'] = item.item_about
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_item['item_publish'] = item.item_publish.strftime('%Y.%m.%d')
        a_item['item_deadtime'] = item.item_deadtime.strftime('%Y.%m.%d')
        start_seconds = time.mktime(item.item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(item.item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_item['item_consume_time'] = 100
            a_item['item_key'] = "已结束"
        else:
            a_item['item_consume_time'] = int(consume_time)
        a_item['pa'] = tb_item_pa.objects.get(ipa_id=item.item_pa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_item['order_num'] = len(tb_order.objects.filter(item_id=item.item_id))#获取项目对应订单的数量
        a_items.append(a_item)

    return render(request,'search_result.html',{'selected':selected,'flag':flag,'items':a_items})

##############################排序by LJW
#按发布时间
sortflag=True
def search_result_sort_starttime(request):
    a_items = []
    
    
    
   
    if(sortflag==True):
    	items = tb_item.objects.order_by('item_publish')
  	global sortflag
	sortflag=False
    else:
    	items = tb_item.objects.order_by('-item_publish')
  	global sortflag
	sortflag=True
    
    for item in items:
    	a_item = {}    
        a_item['item_id'] = item.item_id#获取项目id
        a_item['item_name'] = item.item_name#获取项目名字 
        a_item['item_ga'] = item.item_ga
        a_item['item_key'] = item.item_key
        a_item['item_about'] = item.item_about
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_item['item_publish'] = item.item_publish.strftime('%Y.%m.%d')
        a_item['item_deadtime'] = item.item_deadtime.strftime('%Y.%m.%d')
        start_seconds = time.mktime(item.item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(item.item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_item['item_consume_time'] = 100
            a_item['item_key'] = "已结束"
        else:
            a_item['item_consume_time'] = int(consume_time)
        a_item['pa'] = tb_item_pa.objects.get(ipa_id=item.item_pa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_item['order_num'] = len(tb_order.objects.filter(item_id=item.item_id))#获取项目对应订单的数量
        a_items.append(a_item)
    return render(request,'search_result.html',{'items':a_items})
    

#按截至时间
sortflag1=True
def search_result_sort_deadtime(request):
    a_items = []
    
    
    
   
    if(sortflag1==True):
    	items = tb_item.objects.order_by('item_deadtime')
  	global sortflag1
	sortflag1=False
    else:
    	items = tb_item.objects.order_by('-item_deadtime')
  	global sortflag1
	sortflag1=True
    
    for item in items:
    	a_item = {}    
        a_item['item_id'] = item.item_id#获取项目id
        a_item['item_name'] = item.item_name#获取项目名字 
        a_item['item_ga'] = item.item_ga
        a_item['item_key'] = item.item_key
        a_item['item_about'] = item.item_about
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_item['item_publish'] = item.item_publish.strftime('%Y.%m.%d')
        a_item['item_deadtime'] = item.item_deadtime.strftime('%Y.%m.%d')
        start_seconds = time.mktime(item.item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(item.item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_item['item_consume_time'] = 100
            a_item['item_key'] = "已结束"
        else:
            a_item['item_consume_time'] = int(consume_time)
        a_item['pa'] = tb_item_pa.objects.get(ipa_id=item.item_pa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_item['order_num'] = len(tb_order.objects.filter(item_id=item.item_id))#获取项目对应订单的数量
        a_items.append(a_item)
    return render(request,'search_result.html',{'items':a_items})
##############################
#zss项目信息滚动加载瀑布流
def search_result_load(request):
    a_items = []
    last_times = request.GET['times']
    last = int(last_times)
    now = last + 5 #每次只取5条
    items = tb_item.objects.all()[last:now]
    for item in items:
        a_item = {}    
        a_item['item_id'] = item.item_id#获取项目id
        a_item['item_name'] = item.item_name#获取项目名字 
        a_item['item_ga'] = item.item_ga
        a_item['item_key'] = item.item_key
        a_item['item_about'] = item.item_about
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_item['item_publish'] = item.item_publish.strftime('%Y.%m.%d')
        a_item['item_deadtime'] = item.item_deadtime.strftime('%Y.%m.%d')
        start_seconds = time.mktime(item.item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(item.item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_item['item_consume_time'] = 100
            a_item['item_key'] = "已结束"
        else:
            a_item['item_consume_time'] = int(consume_time)
        a_item['pa'] = tb_item_pa.objects.get(ipa_id=item.item_pa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_item['order_num'] = len(tb_order.objects.filter(item_id=item.item_id))#获取项目对应订单的数量
        a_items.append(a_item)
        print item
        #json.dumps('a_item',a_items)
        #序列化之后注意前端取数据的格式,数据部分在fields里面
        #return HttpResponse(serializers.serialize("json",a_items),content_type='application/json')  
    return HttpResponse(json.dumps(a_items))  
 
#zss条件筛选
def filter_labels(request):
    keys = request.GET['filterkeys']
    if 'bumen' in request.GET:
        request.session['bumen'] = keys    
    if 'jibie' in request.GET:
        request.session['jibie'] = keys 
    if 'zhuangtai' in request.GET:
        request.session['zhuangtai'] = keys
    return HttpResponseRedirect('/search_result/')

#lzh项目项目详情加载
def project_detail(request):
    
    if request.GET['id']:
 
        project_detail_item_id = request.GET['id']
        
       
    item = tb_item.objects.get(item_id = project_detail_item_id)
    
    article = tb_article.objects.filter(affiliation_id = project_detail_item_id)
    article0 = article[0]
    article1 = article[1]
    article2 = article[2]

    a_pics = []

    album = tb_album.objects.filter(album_type=0,affiliation_id=project_detail_item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
    album_id = album.album_id
    pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片
    for pic in pics:
        a_pic = pic.pic_object.url[14:]
        a_pics.append(a_pic)
    
    return render(request,'project_detail.html',{'item':item,'article0':article0,'article1':article1,'article2':article2,'a_pics':a_pics})

#YZ 服务商详情页面
def service_details(request):
    if request.GET['goodsid']:
 
        service_detail_goods_id = request.GET['goodsid']
        
     
    goods = tb_goods.objects.get(goods_id = service_detail_goods_id)#获得需要购买的项目的id对应的服务商
    service_detail_item_id = goods.item_id
    item = tb_item.objects.get(item_id = service_detail_item_id)#获得需要购买的项目的id对应的对象
    
    #计算日期百分比用于赋值进度条
    starttime = item.item_publish
    endtime = item.item_deadtime
    days_total = (endtime - starttime).days
    
    days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days
    if days_remain <= 0:
        finish_percentage = 100
    else:
        finish_percentage = int((days_remain/days_total)*100)
        
    #取项目对应的图片，赋值相册空间
    pics_url = []
    album = tb_album.objects.filter(affiliation_id=item.item_id)[0]#获取项目对应的相册id
    album_id = album.album_id
    pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片                                                               #切片14是去除前缀zhengzihui_app 否则图片不能显示    
    for pic in pics:
        a_pic = pic.pic_object.url[14:] # 切片14是去除前缀zhengzihui_app 否则图片 ！！！部署时肯定还得修改
        pics_url.append(a_pic)
    
    
    #用于推荐其他服务商
    allgoods_for_itemhere = tb_goods.objects.filter(item_id = item.item_id).order_by("goods_sort")#获取提供该项目支持的服务商，并按照他们的升序降序排列 排除自身！！
    #从推荐服务商排除自己
    goods_myself = tb_goods.objects.get(goods_id = goods.goods_id)
    allgoods_for_itemhere = list(allgoods_for_itemhere)
    for good in allgoods_for_itemhere:
        if good.goods_id == goods_myself.goods_id:
            allgoods_for_itemhere.remove(good)
      
    
    #获得排序最高的4个服务商
    if len(allgoods_for_itemhere)> 4:
        goods_recommend_display = allgoods_for_itemhere[0:4]
    else:
        goods_recommend_display = allgoods_for_itemhere
    
    
    
    #格式化日期
    publish_time_format = item.item_publish.strftime("%Y-%m-%d %H:%I:%S")
    datetime_format = item.item_deadtime.strftime("%Y-%m-%d %H:%I:%S")
    return render(request,'service_detail.html',{'item':item,'goods':goods,'finish_percentage':finish_percentage,'pics_url':pics_url,'publish_time_format':publish_time_format,'datetime_format':datetime_format,'goods_recommend_display':goods_recommend_display})
    
    
    
    

	
def service_list(request):
    noservice = 1
    noserviceinfo = "没有指定的服务商"
    id1 = request.GET.get('itemid')
    #print id1

    id1 = int(id1)
    tb_goods_list = tb_goods.objects.filter(item_id=1)
    #for a in tb_goods_list: 
    #print (a.goods_id)

    items = tb_item.objects.all()[:3]
    a_items = []
    for item in items:
	a_item = {} 
	a_item['item_key'] = item.item_key
	album = tb_album.objects.filter(album_type=0,affiliation_id=item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
	album_id = album.album_id
	a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
	a_items.append(a_item)
    
    if tb_goods_list is None:
        return render(request,'goods_list.html',{'noservice':noservice,'noserviceinfo':noserviceinfo,'items1':a_items[0],'items2':a_items[1],'items3':a_items[2]})
    else:
        return render_to_response('goods_list.html',{'tb_goods_list':tb_goods_list,'items1':a_items[0],'items2':a_items[1],'items3':a_items[2]})
    


def pay(request):
	"""
	the function of payment
	"""
	_goods_id = request.GET['goodsidtopay']
	order_id=len(tb_order.objects.all())+1
	order_no=order_id
	pay_no=order_id
	#request.session['unpayedid']=order_id
	#print length
	#_goods_id = '0001'
	goods = tb_goods.objects.get(goods_id = _goods_id)
	_price = goods.goods_price
	_discount = goods.goods_price_discouint
	_total_price = _price * _discount
	item_id=goods.item_id
	items = tb_item.objects.get(item_id=item_id)
	item_name=items.item_name
	sp_id=good.sp_id
	#下面都是写死的
	buyer_id=3
	buyer_name=3
	buyer_email='1@qq.com'
	add_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
	order_state=1
	payment_code=1
	payment_time=add_time
	final_time=add_time
	good_amount=1
	order_amount=1
	eval_state=0
	refund_state=0
	lock_state=0
	refund_amount=0
	delay_time=0
	order_from=1
	express_id=0
	express_no=0
	express_state=1
    #total_price=0.01 这里是测试字段，根据实际属性变动
    #o_id = random.randint(1000001,9999999)
    #m_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #state = 0  # 0:未付款,1：已付款
    #order=Orders(clientuser=user,orderid=o_id,ordertime=m_time,ordermoney=total_price,orderstate=state)
    #order.save()
	pay_url = p_alipay.alipay.create_direct_pay_by_user(_goods_id, "充值测试", "hello zhong",
                                                            _total_price) 
	return render(request, 'pay.html', {'pay_url': pay_url})
	
def declare(request):
	id1 = request.GET.get('itemid')
	#print id1
	tb_goods_list = tb_goods.objects.filter(item_id=id1)
	#for a in tb_goods_list: 
			#print (a.goods_id)
	return render_to_response('goods_list.html',{'tb_goods_list':tb_goods_list})


#zss
#用户中心
def user_center(request):
    request.session['user_id'] = 3#此处设置了个session值用来测试，等登录模块完成之后再修改
    user = []
    a_click_items = []
    a_recommend_items = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        user = tb_user.objects.get(user_id=user_id)

    click_items = tb_item_click.objects.order_by('-click_counter')[:15]#获取点击率前15的项目
    for click_item in click_items:
        a_click_item = {}    
        a_click_item['id'] = click_item.item_id#获取项目id
        a_click_item['name'] = click_item.item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_click_items.append(a_click_item)
    recommend_items = tb_item.objects.filter(is_recommend=1).order_by('-item_id')[:15]#获取推荐的前15的项目
    for recommend_item in recommend_items:
        a_recommend_item= {}
        a_recommend_item['id'] = recommend_item.item_id#获取项目id
        a_recommend_item['name'] = recommend_item.item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=recommend_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_recommend_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_recommend_items.append(a_recommend_item)
    return render(request,'user.html',{'user':user,'a_click_items':a_click_items,'a_recommend_items':a_recommend_items})


#用户信息 zss

    #我的信息
def my_info(request):
    user = []
    company = []
    usertype = False
    if request.session['user_id']:
        user_id = request.session['user_id']
        user = tb_user.objects.get(user_id=user_id)
        if user.user_type == 1:
            company = tb_user_expand.objects.get(user_id=user_id)
            usertype = True
    return render(request,'my_info.html',{'user':user,'company':company,'usertype':usertype})

    #保存修改信息
def modify_user(request):
    user = []
    user_expand = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        user = tb_user.objects.get(user_id=user_id)
    user.user_name = request.POST['name']
    user.user_email = request.POST['email']
    user.user_password = request.POST['password']
    user.user_telephone = request.POST['phonenumber']
    usertype = int(request.POST['usertype'])
    user.user_type = usertype
    user.save()
    if usertype == 1:
        user_expand = tb_user_expand.objects.get(user_id=user.user_id)
        user_expand.company_tel = request.POST['company_tel']
        user_expand.company_email = request.POST['company_email']
        user_expand.company_name = request.POST['company_name']
        user_expand.company_district = request.POST['company_district']
        user_expand.company_address = request.POST['company_address']
        user_expand.company_registered_capital = request.POST['company_registered_capital']
        user_expand.company_industry = request.POST['company_industry']
        user_expand.company_stuff_no = request.POST['company_stuff_no']
        user_expand.company_nature = request.POST['company_nature']
        user_expand.save()
    return HttpResponseRedirect('/zzh/user_center')
    #安全中心
def safe_center(request):
    if request.session['user_id']:
        user_id = request.session['user_id']

    #支付绑定
def pay_combine(request):
    if request.session['user_id']:
        user_id = request.session['user_id']

    #等级与成长
def grade_grow(request):
    if request.session['user_id']:
        user_id = request.session['user_id']


#订单管理 zss
    #全部订单
def all_orders(request):
    order_list = []
    a_order_list = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        order_list = tb_order.objects.filter(buyer_id=user_id).order_by('-add_time')

    for order in order_list:
        a_order = {}    
        a_order['item_id'] = order.item_id#获取项目id
        a_order['item_name'] = order.item_name#获取项目名字
        if order.order_state == 0:
            a_order['order_state'] = '已取消'
        if order.order_state == 1:
            a_order['order_state'] = '未付款'
        if order.order_state == 2:
            a_order['order_state'] = '已付款'
        if order.order_state == 3:
            a_order['order_state'] = '已发货' 
        if order.order_state == 4:
            a_order['order_state'] = '已收货'
        a_order['order_amount'] = order.order_amount
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})

    #未支付
def not_pay(request):
    order_list = []
    a_order_list = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=1).order_by('-add_time')

    for order in order_list:
        a_order = {}    
        a_order['item_id'] = order.item_id#获取项目id
        a_order['item_name'] = order.item_name#获取项目名字
        a_order['order_state'] = '未付款'
        a_order['order_amount'] = order.order_amount
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})

    #已支付
def payed(request):
    order_list = []
    a_order_list = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=2).order_by('-add_time')

    for order in order_list:
        a_order = {}    
        a_order['item_id'] = order.item_id#获取项目id
        a_order['item_name'] = order.item_name#获取项目名字
        a_order['order_state'] = '已支付'
        a_order['order_amount'] = order.order_amount
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})


    #已发货
def delivered(request):
    order_list = []
    a_order_list = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=3).order_by('-add_time')

    for order in order_list:
        a_order = {}    
        a_order['item_id'] = order.item_id#获取项目id
        a_order['item_name'] = order.item_name#获取项目名字
        a_order['order_state'] = '已发货'
        a_order['order_amount'] = order.order_amount
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})


    #已验收
def checked(request):
    order_list = []
    a_order_list = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=4).order_by('-add_time')

    for order in order_list:
        a_order = {}    
        a_order['item_id'] = order.item_id#获取项目id
        a_order['item_name'] = order.item_name#获取项目名字
        a_order['order_state'] = '已验收'
        a_order['order_amount'] = order.order_amount
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})

    #已取消
def delete(request):
    order_list = []
    a_order_list = []
    if request.session['user_id']:
        user_id = request.session['user_id']
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=0).order_by('-add_time')

    for order in order_list:
        a_order = {}    
        a_order['item_id'] = order.item_id#获取项目id
        a_order['item_name'] = order.item_name#获取项目名字
        a_order['order_state'] = '已取消'
        a_order['order_amount'] = order.order_amount
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})

#评价管理
    #全部评价
def all_evaluations(request):
    if request.session['user_id']:
        user_id = request.session['user_id']

    #未评论
def not_evaluate(request):
    if request.session['user_id']:
        user_id = request.session['user_id']
        
    #已评论
def evaluated(request):
    if request.session['user_id']:
        user_id = request.session['user_id']
        
        
        
        
def friend_link(request):
    return render(request,'link.html',{})
    
def quanlification(request):
    return render(request,'quanlification.html',{})
  
def newhire(request):
	return render_to_response('hire.html',{})
	
def artificial_apeal(request):
	return render_to_response('artificial_apeal.html',{})

def contact_us(request):
	return render_to_response('contact_us.html',{})
	
	
def business_cooperation(request):
    return render(request,'business_cooperation.html',{})

def union_website(request):
    return render(request,'union_website.html',{})

	

#个人注册
def g_register(request):  
    errors= []  
    telephone=None  
    password=None  
    password2=None  
    CompareFlag=False  
  
    if request.method == 'POST':  
        if not request.POST.get('telephone'):  
            errors.append('请输入手机号码')  
        else:  
            telephone = request.POST.get('telephone')  
        if not request.POST.get('password'):  
            errors.append('请输入密码')  
        else:  
            password= request.POST.get('password')  
        if not request.POST.get('password2'):  
            errors.append('请确认密码')  
        else:  
            password2= request.POST.get('password2')  
  
        if password is not None and password2 is not None:  
            if password == password2:  
                CompareFlag = True  
            else:  
                errors.append('两次输入密码不一致，请重新输入 ')   
        if telephone is not None and password is not None and password2 is not None and CompareFlag :  
            user=User.objects.create_user(telephone,password)  
            user.is_active=True  
            user.save  
            return HttpResponseRedirect('register2.html')  
    return render_to_response('g_register.html', {'errors': errors})  
    
#企业注册
def q_register(request):  
    errors= []  
    account=None     
    password=None  
    password2=None  
    CompareFlag=False
    company=None
    address=None
    capital=None
    name=None
    telephone=None
    email=None

    if request.method == 'POST':  
        if not request.POST.get('account'):  
            errors.append('请输用户名')  
        else:  
            account = request.POST.get('account')  
        if not request.POST.get('password'):  
            errors.append('请输入密码')  
        else:  
            password= request.POST.get('password')  
        if not request.POST.get('password2'):  
            errors.append('请确认密码')  
        else:  
            password2= request.POST.get('password2')  
  
        if password is not None and password2 is not None:  
            if password == password2:  
                CompareFlag = True  
            else :  
                errors.append('两次输入密码不一致，请重新输入 ')  
  
        if not request.POST.get('company'):  
            errors.append('请输入公司名称')  
        else:  
            company= request.POST.get('company')

        if not request.POST.get('address'):  
            errors.append('请输入公司注册地址')  
        else:  
            address= request.POST.get('address')

        if not request.POST.get('capital'):  
            errors.append('请输入公司注册资本')  
        else:  
            capital= request.POST.get('capital')

        if not request.POST.get('name'):  
            errors.append('请输入联系人姓名')  
        else:  
            name= request.POST.get('name')

        if not request.POST.get('telephone'):  
            errors.append('请输入联系人座机号码')  
        else:  
            telephone= request.POST.get('telephone')

        if not request.POST.get('email'):  
            errors.append('请输入联系人邮箱')  
        else:  
            email= request.POST.get('email') 
        if account is not None and password is not None and password2 is not None and CompareFlag and company is not None and address is not None and capital is not None and name is not None and telephone is not None and email is not None :  
            user=User.objects.create_user(account,telephone,company,address,capital,name,password,email)  
            user.is_active=True  
            user.save  
            return HttpResponseRedirect('register2.html')    
    return render_to_response('q_register.html', {'errors': errors}) 

#验证
def register2(request):  
    errors= []  
    code=None
    if request.method == 'POST' :  
        if not request.POST.get('code'):  
            errors.append('请输入验证码')  
        else:  
            code = request.POST.get('code')
        if code is not None:
            user=User.objects.create_user(code)  
            user.is_active=True  
            user.save  
        return HttpResponseRedirect('register3.html')
    return render_to_response('register2.html', {'errors': errors})    

#注册成功
def register3(request):    
    return render_to_response('denglu.html')  

#登陆
def login(request):
    errors= []  
    account=None  
    password=None  
    if request.method == 'POST' :  
        if not request.POST.get('account'):  
            errors.append('请输入用户名')  
        else:  
            account = request.POST.get('account')  
        if not request.POST.get('password'):  
            errors.append('请输入登陆密码')  
        else:  
            password= request.POST.get('password')  
        if account is not None and password is not None :  
             user = authenticate(username=account,password=password)  
             if user is not None:  
                 if user.is_active:  
                     login(request,user)  
                     return HttpResponseRedirect('index.html')  
                 else:  
                     errors.append('用户名不存在')  
             else :  
                  errors.append('用户名无效，请重新输入')  
    return render_to_response('denglu.html', {'errors': errors})

#找回密码步骤一
def password1(request):
    errors= []  
    account=None
    code=None
    if request.method == 'POST' :  
        if not request.POST.get('account'):  
            errors.append('请输入用户名')  
        else:  
            account = request.POST.get('account')
        if not request.POST.get('code'):  
            errors.append('请输入图形验证码')  
        else:  
            code = request.POST.get('code')
        if account is not None and code is not None:
            user=User.objects.create_user(account,code)  
            user.is_active=True  
            user.save  
        return HttpResponseRedirect('password2.html')
    return render_to_response('password1.html', {'errors': errors})   

#找回密码步骤二
def password2(request):
    errors= []  
    code=None
    if request.method == 'POST' :  
        if not request.POST.get('code'):  
            errors.append('请输入手机动态密码')  
        else:  
            code = request.POST.get('code')
        if code is not None:
            user=User.objects.create_user(account,code)  
            user.is_active=True  
            user.save  
        return HttpResponseRedirect('password3.html',{})
    return render_to_response('password2.html', {'errors': errors})  

#找回密码步骤三
def password3(request):
    errors= []  
    password=None  
    password2=None
    CompareFlag=False
    if request.method == 'POST':
        if not request.POST.get('password'):  
            errors.append('请输入密码')  
        else:  
            password= request.POST.get('password')  
        if not request.POST.get('password2'):  
            errors.append('请确认密码')  
        else:  
            password2= request.POST.get('password2')  
  
        if password is not None and password2 is not None:  
            if password == password2:  
                CompareFlag = True  
            else:  
                errors.append('两次输入密码不一致，请重新输入 ')   
        if password is not None and password2 is not None and CompareFlag :   
            user=User.objects.create_user(password)  
            user.is_active=True  
            user.save  
            return HttpResponseRedirect('password4.html',{})  
    return render_to_response('password3.html', {'errors': errors})

#找回密码步骤四
def password4(request):   
    return render_to_response('denglu.html',{})             
         
def download(request):
	return render(request,'download.html',{})

