# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import json #用来将字典类型的数据序列化，然后传给模板以及js,不能序列化model实例
import jieba,p_alipay.alipay
from django.core import serializers #用来序列化model 传给js
from models import tb_item,tb_item_class,tb_item_pa,tb_article,tb_album,tb_pic,tb_goods
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
				ads+=tb_item.objects.filter(item_name__contains = gname)
		#去重复
			for i in ads: 
				if i not in items:
					items.append(i)
					#print i.item_name
			return render(request,'ind.html',{'selected':selected,'flag':flag,'items':items})


def hello(request):

    tb_item_list = tb_item.objects.all()


    tb_item_class_list = tb_item_class.objects.all()


    tb_item_pa_list = tb_item_pa.objects.all()



    tb_album_list = tb_album.objects.all()

    

    item_id = request.GET['id']
    
    tb_article_list = tb_article.objects.get(affiliation_id=item_id)

    #print tb_article_list.article_name

    return render(request,'project_detail.html',{'tb_item_list':tb_item_list,'tb_item_class_list':tb_item_class_list,'tb_item_pa_list':tb_item_pa_list,'tb_article_list':tb_article_list,'tb_album_list':tb_album_list})


#点击搜索的下一级
def ind(request):


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

    return render(request,'ind.html',{'selected':selected,'flag':flag,'items':items})

#项目信息滚动加载瀑布流
def ajax(request):
    p0 = {
            "item_id":45,
            "item_code" :"58%",
            "item_name" :"四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            "itcl_id" : 23,
            "item_level" : 1,
            "item_ga" :"科技厅",
            "item_about" : "科技创新",
            "item_url" : "../static/images/6.jpg",
            "item_key" : "成功率高",
            
            "is_hot" :45
         
            }
    p1 = {
            "item_id":45,
            "item_code" :"58%",
            "item_name" :"四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            "itcl_id" : 23,
            "item_level" : 1,
            "item_ga" :"科技厅",
            "item_about" : "科技创新",
            "item_url" : "../static/images/5.jpg",
            "item_key" : "成功率高",
            
            "is_hot" :45
         
            }
    p2 = {
            "item_id":45,
            "item_code" :"58%",
            "item_name" :"四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            "itcl_id" : 23,
            "item_level" : 1,
            "item_ga" :"科技厅",
            "item_about" : "科技创新",
            "item_url" : "../static/images/4.jpg",
            "item_key" : "成功率高",
            
            "is_hot" :45
         
            }
    p3 = {
            "item_id":45,
            "item_code" :"58%",
            "item_name" :"四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            "itcl_id" : 23,
            "item_level" : 1,
            "item_ga" :"科技厅",
            "item_about" : "科技创新",
            "item_url" : "../static/images/3.jpg",
            "item_key" : "成功率高",
            
            "is_hot" :45
         
            }
    last_times = request.GET['times']
    print last_times
    last = int(last_times)
    now = last + 5 #每次只取5条
    print now
    items = tb_item.objects.all()[last:now]
    #序列化之后注意前端取数据的格式,数据部分在fields里面
    return HttpResponse(serializers.serialize("json",items),content_type='application/json')  
 

#条件筛选
def filter(request):
	
    keys = request.GET['filterkeys']
    if 'bumen' in request.GET:
        request.session['bumen'] = keys    
    if 'jibie' in request.GET:
        request.session['jibie'] = keys 
    if 'zhuangtai' in request.GET:
        request.session['zhuangtai'] = keys
    return HttpResponseRedirect('/zzh_index/')
    
'''
def hello(request):
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
    tb_item_list = tb_item.objects.all()

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

    

    item_id = request.GET['id']
    
    tb_article_list = tb_article.objects.get(affiliation_id=item_id)

    #print tb_article_list.article_name

    return render(request,'project_detail.html',{'tb_item_list':tb_item_list,'tb_item_class_list':tb_item_class_list,'tb_item_pa_list':tb_item_pa_list,'tb_article_list':tb_article_list,'tb_album_list':tb_album_list})
 '''   
    



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