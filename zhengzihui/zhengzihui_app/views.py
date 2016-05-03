# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import json #用来将字典类型的数据序列化，然后传给模板以及js,不能序列化model实例
import jieba,p_alipay.alipay
from django.core import serializers #用来序列化model 传给js
from models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News,Tb_Notice,Tb_Notice_Class,Tb_Apage,Tb_Apage_Class,tb_album,tb_pic,tb_accessory,tb_Artificial_Representations,tb_Message,tb_MessageText,tb_SysMessage,tb_item,tb_item_pa,tb_item_class,tb_goods,tb_album,tb_pic,tb_article,tb_goods_evaluation,tb_goods_click,tb_goods_class,tb_order,tb_item_click,tb_area
# Create your views here.
def index(request):
	#print (123)
	return render_to_response('index.html',{})

def Searchgoods(request):
	if (request.method=="GET"):
		selected = {}
    		flag = False
		ads=[]
		items=[]
		goodsname=request.GET.get("inputitem")
		#print (goodsname)
		#goodsname="精准医学研究"
		if goodsname is not None:
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
			return render(request,'ind.html',{'selected':selected,'flag':flag,'items':items})


def item_details(request):

    tb_item_list = tb_item.objects.all()


    tb_item_class_list = tb_item_class.objects.all()


    tb_item_pa_list = tb_item_pa.objects.all()



    tb_album_list = tb_album.objects.all()

    

    item_id = request.GET['id']
    
    tb_article_list = tb_article.objects.get(affiliation_id=item_id)

    #print tb_article_list.article_name

    return render(request,'project_detail.html',{'tb_item_list':tb_item_list,'tb_item_class_list':tb_item_class_list,'tb_item_pa_list':tb_item_pa_list,'tb_article_list':tb_article_list,'tb_album_list':tb_album_list})


#zss 点击搜索的下一级
def search_result(request):
#首次只返回10条数据
    items = tb_item.objects.all()[:10]
    selected = {}
    flag = False
    if 'bumen' in request.session:
        value = request.session['bumen']
        selected['bumen'] = value
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

    return render(request,'search_result.html',{'selected':selected,'flag':flag,'items':items})

#zss项目信息滚动加载瀑布流
def search_result_load(request):
    last_times = request.GET['times']
    print last_times
    last = int(last_times)
    now = last + 5 #每次只取5条
    print now
    items = tb_item.objects.all()[last:now]
    #序列化之后注意前端取数据的格式,数据部分在fields里面
    return HttpResponse(serializers.serialize("json",items),content_type='application/json')  
 
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



def service_details(request):
    
    if request.GET['goodsid']:
 
        service_detail_goods_id = request.GET['goodsid']
        
       
    goods = tb_goods.objects.get(goods_id = service_detail_goods_id)#获得需要购买的项目的id对应的对象
    service_detail_item_id = goods.item_id
    item = tb_item.objects.get(item_id = service_detail_item_id)#获得需要购买的项目的id对应的对象

    
    return render(request,'service_detail.html',{'item':item,'goods':goods})
    
    
    
    
def pay(request):
	"""
	the function of payment
	"""
	_goods_id = request.GET['goodsidtopay']
	#print _goods_id
	#_goods_id = '0001'
	goods = tb_goods.objects.get(goods_id = _goods_id)
	_price = goods.goods_price
	_discount = goods.goods_price_discouint
	_total_price = _price * _discount
    #total_price=0.01 这里是测试字段，根据实际属性变动
    #o_id = random.randint(1000001,9999999)
    #m_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #state = 0  # 0:未付款,1：已付款
    #order=Orders(clientuser=user,orderid=o_id,ordertime=m_time,ordermoney=total_price,orderstate=state)
    #order.save()
	pay_url = p_alipay.alipay.create_direct_pay_by_user(_goods_id, "充值测试", "hello zhong",
                                                            _total_price) 
	return render(request, 'pay.html', {'pay_url': pay_url})
	
def service_list(request):
    noservice = 1
    noserviceinfo = "没有指定的服务商"
    id1 = request.GET.get('itemid')
    #print id1
    tb_goods_list = tb_goods.objects.filter(item_id=id1)
	#for a in tb_goods_list: 
			#print (a.goods_id)
    if tb_goods_list is None:
        return render(request,'goods_list.html',{'noservice':noservice,'noserviceinfo':noserviceinfo})
    else:
        return render_to_response('goods_list.html',{'tb_goods_list':tb_goods_list})
    
    
   
   
   
   
   
   
def create_test_data(request):
    p0 = tb_item( 
    	    item_id = 45,
            item_code = "58",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 23,
            item_level = 1,
            item_ga = "科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "科技创新",
            item_url = "../static/images/6.jpg",
            item_key = "成功率高",
            item_status = 0,
            is_hot = 45,
            item_from = 0,
            is_recommend = 0,
            )
    p0.save()
    p001 = tb_item( 
    	    item_id = 205,
            item_code = "53248",
            item_name = "四川省火星计划2016年度项目的通知",
            itcl_id = 23,
            item_level = 1,
            item_ga = "科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "科技创新",
            item_url = "../static/images/7.jpg",
            item_key = "成功率高",
            item_status = 0,
            is_hot = 45,
            item_from = 0,
            is_recommend = 0,
            )
    p001.save()
    p002 = tb_item( 
    	    item_id = 20168,
            item_code = "58324234",
            item_name = "四川省高端医疗计划项目的通知",
            itcl_id = 23,
            item_level = 1,
            item_ga = "科技厅",
            item_pa_id = 3,
            item_publish = 2015,
            item_deadtime = 2016,
            item_about = "科技创新",
            item_url = "../static/images/9.jpg",
            item_key = "成功率高",
            item_status = 0,
            is_hot = 45,
            item_from = 0,
            is_recommend = 0,
            )
    p002.save()
    p003 = tb_item( 
    	    item_id = 2325,
            item_code = "524332521",
            item_name = "贵州省旅游重点点专项2016年度项目的通知",
            itcl_id = 23,
            item_level = 1,
            item_ga = "科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "科技创新",
            item_url = "../static/images/2.jpg",
            item_key = "成功率高",
            item_status = 0,
            is_hot = 45,
            item_from = 0,
            is_recommend = 0,
            )
    p003.save()
    

    p2 = tb_item_class(
            itcl_id = 112,
            itcl_code = 112,
            itcl_name = "models",
            itcl_des = "models.CharField",
            necl_parent_id = 76,
            necl_sort = 12,
            )

    p2.save()
    tb_item_class_list = tb_item_class.objects.all()

    p3 = tb_item_pa(
            ipa_id = 11,
            ipa_name = "max_length=100,null=False",
            ipa_parent_id = 33,
            ipa_sort = 55,
            area_id = 66,
            )
    p3.save()
    tb_item_pa_list = tb_item_pa.objects.all()

    p41 = tb_article(
            article_id = 451,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 45,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p41.save()
    
    p42 = tb_article(
            article_id = 451,
            article_code = 2325,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 2325,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p42.save()
    p43 = tb_article(
            article_id = 451,
            article_code = 2325,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 2325,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p43.save()
    p42 = tb_article(
            article_id = 452,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20151,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p42.save()
    p43 = tb_article(
            article_id = 453,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20152,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p43.save()
    p44 = tb_article(
            article_id = 454,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20153,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p44.save()
    p45 = tb_article(
            article_id = 455,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20154,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p45.save()
    p46 = tb_article(
            article_id = 456,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20155,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p46.save()
    p47 = tb_article(
            article_id = 457,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20156,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p47.save()
    p48 = tb_article(
            article_id = 458,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20157,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p48.save()
    p49 = tb_article(
            article_id = 459,
            article_code = 45,
            article_name = "2016科技计划项目",
            author = "models.CharField",
            author_email = "models.CharField",
            article_type = 98,
            affiliation_id = 20158,
            article_content = "models.TextField",
            article_keywords = "models.TextField",
            article_des = "models.CharField",
            article_sort = 99,
            
            is_default = 00,
            article_click = 06,
            )
    p49.save()
  

    p5 = tb_album(
            album_id = 56,
            album_name = "models.CharField",
            album_type = 88,
            affiliation_id = 99,
            nacl_des = "models.CharField",
            nacl_sort = 43,
            nacl_cover = "models.CharFieldmax",
            
            is_default = 21,
            )
    p5.save()
    tb_album_list = tb_album.objects.all()


    return HttpResponse("插入数据成功！")
    





def service_detail(request):
    
    if request.GET['goodsid']:
 
        service_detail_goods_id = request.GET['goodsid']
        
       
    goods = tb_goods.objects.get(goods_id = service_detail_goods_id)#获得需要购买的项目的id对应的对象
    service_detail_item_id = goods.item_id
    item = tb_item.objects.get(item_id = service_detail_item_id)#获得需要购买的项目的id对应的对象

    
    return render(request,'service_detail.html',{'item':item,'goods':goods})
    
    
    
    
def pay(request):
	"""
	the function of payment
	"""
	_goods_id = request.GET['goodsidtopay']
	print _goods_id
	#_goods_id = '0001'
	goods = tb_goods.objects.get(goods_id = _goods_id)
	_price = goods.goods_price
	_discount = goods.goods_price_discouint
	_total_price = _price * _discount
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






def project_detail(request):
    
    if request.GET['id']:
 
        project_detail_item_id = request.GET['id']
        
       
    item = tb_item.objects.get(item_id = project_detail_item_id)
    
    article = tb_article.objects.get(affiliation_id = project_detail_item_id)

    
    return render(request,'project_detail.html',{'item':item,'article':article})



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

#搜索一条项目
def search_one_item(request):
    if request.GET['item_id']:
        item_id = request.GET['item_id']

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