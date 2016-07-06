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
from token import Token
from django.core.mail import send_mail
from django.core import serializers #用来序列化model 传给js
from models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News,Tb_Notice,Tb_Notice_Class,Tb_Apage,Tb_Apage_Class,tb_album,tb_pic,tb_accessory,tb_Artificial_Representations,tb_Message,tb_MessageText,tb_SysMessage,tb_item,tb_item_pa,tb_item_class,tb_goods,tb_album,tb_pic,tb_article,tb_goods_evaluation,tb_goods_click,tb_goods_class,tb_order,tb_item_click,tb_area
SECRET_KEY = '+a^0qwojpxsam*xa5*y_5o+#9fej#+w72m998sjc!e)oj9im*y'
token_confirm = Token(SECRET_KEY)
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
        #后面取值用
        goodsnametmp = goodsname
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
    #有待完善，当输入'科技'等 关键词时无法显示
    search_content = "全部"
    if goodsnametmp!='':
        search_content = goodsnametmp
        if search_content =='':
            search_content = selected
    return render(request,'search_result.html',{'selected':selected,'flag':flag,'items':a_items,'search_content':search_content})


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
    #print(len(items))
    if (len(items)>10):
    	items = items[:10]#不够10条报错
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

##############################服务商排序by LJW
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
    

#按截至时间 排序存在的问题估计是因为 瀑布流每次只能取得10个所以 当超过10个之后再取的8 个 就出现了 重新排序，但是还是按顺序排列

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

    items = items[last:now]
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
    article0 = None
    article1 = None
    a_pics = []
    if (len(article)>=2):
        article0 = article[0]
        article1 = article[1]
    if (len(article)==1):
        article0 = article[0]
        article1 = None
    if (len(article)==0):
        pass
    #article2 = article[2]
    if ((article0 == None)and(article1==None)):
        
        return render(request,'project_detail.html',{'item':item,'article0':article0,'article1':article1,'a_pics':a_pics})
    else:
       

        album = tb_album.objects.filter(album_type=0,affiliation_id=project_detail_item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            a_pics.append(a_pic)
    
        return render(request,'project_detail.html',{'item':item,'article0':article0,'article1':article1,'a_pics':a_pics})
        
        
#修复从搜索结果界面获得到 item_details/ url的bug,并没有写，但是出现了        
def item_details(request):
    
    if request.GET['id']:
 
        project_detail_item_id = request.GET['id']
        
       
    item = tb_item.objects.get(item_id = project_detail_item_id)
    
    article = tb_article.objects.filter(affiliation_id = project_detail_item_id)
    article0 = None
    article1 = None
    a_pics = []
    if (len(article)>=2):
        article0 = article[0]
        article1 = article[1]
    if (len(article)==1):
        article0 = article[0]
        article1 = None
    if (len(article)==0):
        pass
    #article2 = article[2]
    if ((article0 == None)and(article1==None)):
        
        return render(request,'project_detail.html',{'item':item,'article0':article0,'article1':article1,'a_pics':a_pics})
    else:
       

        album = tb_album.objects.filter(album_type=0,affiliation_id=project_detail_item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            a_pics.append(a_pic)
    
        return render(request,'project_detail.html',{'item':item,'article0':article0,'article1':article1,'a_pics':a_pics})

        

    
def service_list(request):
    service = 1
    noservice = 0
    noserviceinfo = "没有指定的服务商"
    id1 = request.GET['itemid']
    
    
    #未完！！
    #按项目点击率降序获得前最多前三个热门项目
    HotClick = tb_item_click.objects.all()[0:2]
    HotClickDis =HotClick
    #得到相关的项目
    HotItemDis = []
    a_pics = []
    for hotclick in HotClickDis:
        album = tb_album.objects.filter(album_type=0,affiliation_id=hotclick.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0]#获取第一张张图片
        a_pic = pics.pic_object.url[14:]
        a_pics.append(a_pic)

        
        
        
        
        
    if (id1==''):
        service = 0
        noservice =1
        return render_to_response('goods_list.html',{'service':service,'noservice':noservice,})
    else:
        #print id1
        id1 = int(id1)
        tb_goods_list = tb_goods.objects.filter(item_id = id1)
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
    
        
        else:
            return render_to_response('goods_list.html',{'tb_goods_list':tb_goods_list,'service':service,'noservice':noservice,})        
        
        
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
    # print(days_remain)
    #print(days_total)
    #print(starttime)
    #print(endtime)
    if days_remain <= 0:
        finish_percentage = 100
    else:
        finish_percentage = int((float(days_remain)/float(days_total))*100)
    #
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
    #判断是否是来自未登录用户的支付浏览
    showDialogflag = 0
    
    if 'unregist_tobepay_goodsid' in request.COOKIES:
        showDialogflag = 1
        response = render(request,'service_detail.html',{'item':item,'goods':goods,'finish_percentage':finish_percentage,'pics_url':pics_url,'publish_time_format':publish_time_format,'datetime_format':datetime_format,'goods_recommend_display':goods_recommend_display,'showDialogflag':showDialogflag})         
        response.delete_cookie('unregist_tobepay_goodsid')
        return response
        
    
    print showDialogflag 
    return render(request,'service_detail.html',{'item':item,'goods':goods,'finish_percentage':finish_percentage,'pics_url':pics_url,'publish_time_format':publish_time_format,'datetime_format':datetime_format,'goods_recommend_display':goods_recommend_display,'showDialogflag':showDialogflag})         
    
    
    
    

	

    
def Payback(request):
	order_id=request.session['unpayedid']
	u = tb_order.objects.get(order_id=order_id)
	u['order_state']=2
	u.save()
	return HttpResponseRedirect('/zzh/user_center')

def pay(request):
	"""
	the function of payment
	"""
	_goods_id = request.GET['goodsidtopay']
	order_id=len(tb_order.objects.all())+1
	#order_no=order_id     order_no这个字段我替换成了goods_id
	request.session['unpayedid']=order_id
	#print length
	#_goods_id = '0001'
	goods = tb_goods.objects.get(goods_id = _goods_id)
	goods_name = goods.goods_name
	_price = goods.goods_price
	_discount = goods.goods_price_discouint
	_total_price = _price * _discount
	item_id=goods.item_id
	items = tb_item.objects.get(item_id=item_id)
	item_name=items.item_name
	sp_id=goods.sp_id
	#下面都是写死的
	buyer_id=3
	add_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	pay_no = 0
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
	delay_time=add_time
	order_from=1
	express_id=0
	express_no=0
	express_state=1
	u=tb_order(express_id=express_id,order_id=order_id,goods_id=_goods_id,pay_no=pay_no,item_id=item_id,item_name=goods_name,sp_id=sp_id,buyer_id=buyer_id,add_time=add_time,payment_time=payment_time,final_time=final_time,good_amount=good_amount,refund_amount=refund_amount,delay_time=delay_time)
	u.save()

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
    #request.session['user_id'] = 3#此处设置了个session值用来测试，等登录模块完成之后再修改
    user = []
    a_click_items = []
    a_recommend_items = []
    if 'user_id' in request.COOKIES:
        user_id = int(request.COOKIES['user_id'])
        user = tb_user.objects.get(user_id=user_id)
    else:
        return HttpResponse("请先登录账号;请返回到上级页面登录或者注册")

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
        user_id = int(request.session['user_id'])
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
        user_id = int(request.session['user_id'])
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
        user_id = int(request.session['user_id'])

    #支付绑定
def pay_combine(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])

    #等级与成长
def grade_grow(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])


#订单管理 zss
    #全部订单
def all_orders(request):
    order_list = []
    a_order_list = []
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id     
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0:
            if order.order_state == 0:
                a_order['order_state'] = '已取消'
            if order.order_state == 1:
                a_order['order_state'] = '未付款'
            if order.order_state == 2:
                a_order['order_state'] = '已付款'
            if order.order_state == 3:
                a_order['order_state'] = '已发货' 
            if order.order_state == 4:
                a_order['order_state'] = '已验收'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
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
        user_id = int(request.session['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=1).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id 
        a_order['goods_id'] = order.goods_id#获取商品id     
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '未付款'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
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
        user_id = int(request.session['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=2).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id      
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已付款'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
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
        user_id = int(request.session['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=3).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id   
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已发货'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
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
        user_id = int(request.session['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=4).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id      
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已验收'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
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
        user_id = int(request.session['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=0).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id      
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已取消'
        else:
            a_order['order_state'] = '申请处理中'    
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})


    #确认订单
def order_enter(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            order.order_state = 4
            order.save()
            return HttpResponse("0")
        else:
            return HttpResponse("1")

    #申请关闭
def order_giveup(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            order.lock_state = 1
            order.save()
            return HttpResponse("0")
        else:
            return HttpResponse("1")

        
    #删除订单
def order_delete(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            order.delete()
            return HttpResponse("0")
        else:
            return HttpResponse("1")

    #去评价
def order_commit(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            a_order = {}
            a_order['order_id'] = order.order_id#获取订单id
            a_order['goods_id'] = order.goods_id#获取商品id    
            a_order['item_id'] = order.item_id#获取项目id
            a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        
            a_order['order_amount'] = order.order_amount
            ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
            a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
            album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
            album_id = album.album_id
            a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示    
            return render(request,'order_commit.html',{'order':a_order})
    #添加评价
def order_add_commit(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        order_id = request.POST['order_id']
        order = tb_order.objects.get(order_id=order_id)
        goods_id = order.goods_id
        user_name = order.buyer_name
        goods = tb_goods.objects.get(goods_id=goods_id)
        goods_name = goods.goods_name
        if order.buyer_id == user_id:
            if tb_goods_evaluation.objects.all().order_by('-goev_id'):
                goev_id = tb_goods_evaluation.objects.all().order_by('-goev_id')[0].goev_id + 1 #id自增
            else:
                goev_id = 0
            goev_desccredit = int(request.POST['complete'])
            goev_servicecredit = int(request.POST['service'])
            goev_content = request.POST['content']
            is_anonymous = int(request.POST['is_anonymous'])
            tb_goods_evaluation.objects.create(goev_id=goev_id,order_id=order_id,goods_id=goods_id,goods_name=goods_name,user_id=user_id,user_name=user_name,goev_desccredit=goev_desccredit,goev_servicecredit=goev_servicecredit,goev_content=goev_content,is_anonymous=is_anonymous)
            order.eval_state = 1
            order.save()
            return render(request,'commit_complete.html',{})

#评价管理

    #我的评价
def my_evaluate(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        a_evaluations = []
        evaluations = tb_goods_evaluation.objects.filter(user_id=user_id).order_by('-create_time')
        for evaluation in evaluations:
            a_evaluation = {}
            goods_id = evaluation.goods_id
            a_evaluation['goods_id'] = goods_id
            a_evaluation['goods_name'] = evaluation.goods_name
            a_evaluation['create_time'] = evaluation.create_time.strftime('%Y.%m.%d')
            a_evaluation['goev_desccredit'] = evaluation.goev_desccredit
            a_evaluation['goev_servicecredit'] = evaluation.goev_servicecredit
            a_evaluation['goev_content'] = evaluation.goev_content
            
            if evaluation.is_anonymous == 0:
                a_evaluation['is_anonymous'] = '不匿名'
            else:
                a_evaluation['is_anonymous'] = '匿名'
            item_id = tb_goods.objects.get(goods_id=goods_id).item_id
            album = tb_album.objects.filter(album_type=0,affiliation_id=item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
            album_id = album.album_id
            a_evaluation['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            a_evaluations.append(a_evaluation)
            
        return render(request,'my_evaluate.html',{'evaluations':a_evaluations})


    #评价统计
def statistics(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        all_orders = len(tb_order.objects.filter(buyer_id=user_id))
        all_commit = len(tb_goods_evaluation.objects.filter(user_id=user_id))
        not_commit = all_orders - all_commit
        desccredit_1 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=1))
        desccredit_2 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=2))
        desccredit_3 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=3))
        desccredit_4 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=4))
        desccredit_5 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=5))

        servicecredit_1 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=1))
        servicecredit_2 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=2))
        servicecredit_3 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=3))
        servicecredit_4 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=4))
        servicecredit_5 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=5))
        json.dumps('all_orders',all_orders)
        json.dumps('all_commit',all_commit)
        json.dumps('not_commit',not_commit)
        json.dumps('desccredit_1',desccredit_1)
        json.dumps('desccredit_2',desccredit_2)
        json.dumps('desccredit_3',desccredit_3)
        json.dumps('desccredit_4',desccredit_4)
        json.dumps('desccredit_5',desccredit_5)
        json.dumps('servicecredit_1',servicecredit_1)
        json.dumps('servicecredit_2',servicecredit_2)
        json.dumps('servicecredit_3',servicecredit_3)
        json.dumps('servicecredit_4',servicecredit_4)
        json.dumps('servicecredit_5',servicecredit_5)
        return render(request,'statistics.html',{'al_or':all_orders,'al_co':all_commit,'no_co':not_commit,'d1':desccredit_1,'d2':desccredit_2,'d3':desccredit_3,'d4':desccredit_4,'d5':desccredit_5,'s1':servicecredit_1,'s1':servicecredit_1,'s2':servicecredit_2,'s3':servicecredit_3,'s4':servicecredit_4,'s5':servicecredit_5})
        
        
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


def representations(request):
    return render(request,'representations.html',{})

def safe_center(request):
    return render(request,'safe_center.html',{})

def introduce(request):
    return render(request,'zhengzihui.html',{})

def trustedwebsite(request):
    return render(request,'trustedwebsite.html',{})

#个人注册by cyf
def g_register(request):
    errors = []
    user_name = None
    user_password = None
    user_password2 = None
    user_telephone = None
    user_email = None
    falg = False
    add = []
    if request.method == 'POST':
        if not request.POST.get('_username'):
            errors.append('请输用户名')
        else:
            user_name = request.POST.get('_username')
        if not request.POST.get('_email'):
            errors.append('请输入邮箱')
        else:
            user_email = request.POST.get('_email')
        if not request.POST.get('password'):
            errors.append('请输入密码')
        else:
            user_password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('请重复输入密码')
        else:
            user_password2 = request.POST.get('password2')
        if user_password is not None and user_password2 is not None:
            if user_password == user_password2:
                falg = True
            else:
                errors.append('两次密码输入不一致')
        if not request.POST.get('_telephone'):
            errors.append('请输入电话号码')
        else:
            user_telephone = request.POST.get('_telephone')

        if user_name is not None and user_password is not None and user_telephone is not None and user_email is not None and falg:
            '''自我评价：写的真特么蠢'''
            try:
                user = tb_user.objects.get(user_name = user_name)
                errors.append('用户名已存在')
                return render_to_response('g_register.html',{'errors':errors})
            except tb_user.DoesNotExist:
                pass
            add = tb_user()
            add.user_name = user_name
            
            add.user_password = user_password
            add.user_telephone = user_telephone
            add.user_email = user_email
            add.user_auth = 0
           
            add.save()
            user_id = add.user_id
            token = token_confirm.generate_validate_token(user_name)
            print(token)
            message = "\n".join([u'{0},欢迎注册政资汇'.format(user_name),u'请访问该链接，完成用户验证(链接1小时内有效):','/'.join(['127.0.0.1:8000','register2',token])])
            #message = '/'.join(['127.0.0.1:8000','register2',token])
            send_mail(u'注册用户验证信息', message, 'changyifan123@qq.com', [user_email])
            
            return render_to_response('register2.html')
    return render_to_response('g_register.html',{'errors':errors})
    
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
        
        return render_to_response('register3.html')
    return render_to_response('register2.html', {'errors': errors})    

#注册成功 暂时没用到
def register3(request):  
    username = '未定义'
    userid = '0'
    if 'user_name_r3' in request.GET:
        username = request.GET['user_name_r3']
    if 'user_name' in request.session:
        del request.session['user_name']
    request.session['user_name'] = username
    if 'user_id_r3' in request.GET:
        userid = request.GET['user_id_r3']
    
    request.session['user_id'] = userid
    print(request.session['user_id'])
    print(request.session['user_name_s'])
    if 'unregist_tobepay_goodsid' in request.session:
        goodsid =request.session['unregist_tobepay_goodsid']
        return HttpResponseRedirect('/selectpay')
    else:
        return render_to_response('denglu.html')  

        

#登陆 by cyf
def login(request):
    errors= []  
    user_name=None  
    password=None
    user = tb_user()
    if 'user_name' in request.COOKIES:
        response = render_to_response('index.html',{'user_name':request.COOKIES['user_name']})
        return response
        
    if request.method == 'POST' :  
        if not request.POST.get('_username'):  
            errors.append('请输入用户名')  
        else:
            user_name = request.POST.get('_username')  
        if not request.POST.get('password'):  
            errors.append('请输入登陆密码')  
        else:  
            password= request.POST.get('password')  
        if user_name is not None and password is not None:
            try:
                user = tb_user.objects.get(user_name = user_name)
            except tb_user.DoesNotExist:
                errors.append('用户名不存在')
            if user.user_auth == 0:
            	errors.append('请查看邮件完成用户认证')
            	return render_to_response('denglu.html', {'errors': errors})
            if password == user.user_password:
                
                response = render_to_response('index.html',{'user_name':user.user_name})
                
                response.set_cookie('user_name',user_name,3600)
                response.set_cookie('user_id',user.user_id,3600)
                
                
                if 'unregist_tobepay_goodsid' in request.COOKIES:
                    goodsid = request.COOKIES['unregist_tobepay_goodsid']
                    responsenotpay = HttpResponseRedirect('/service_details/?goodsid='+str(goodsid))
                    responsenotpay.set_cookie('user_name',user_name,3600)
                    responsenotpay.set_cookie('user_id',user.user_id,3600)
                    return responsenotpay
                return response
            else:
                errors.append('密码错误')
    return render_to_response('denglu.html', {'errors': errors})        
    
def logout(request):
        response = HttpResponseRedirect('/index/')
        response.delete_cookie('user_name')
        response.delete_cookie('user_id')
        return response
def selectpay(request):
	#用户已经登陆，跳到选择支付这一步时自动删除为支付的订单标志
    if 'user_id' in request.COOKIES:
        #goodsid 肯定存在的
        if request.GET['goodsid']:
            service_detail_goods_id = request.GET['goodsid']
            goods = tb_goods.objects.get(goods_id = service_detail_goods_id)
            response = render(request,'selectpay.html', {'goods':goods})
            if 'unregist_tobepay_goodsid' in request.COOKIES:
                response.delete_cookie('unregist_tobepay_goodsid') 
            return response
	#若未登陆，计入未支付的商品ID号，跳到注册
    else:
        if request.GET['goodsid']:
            service_detail_goods_id = request.GET['goodsid']
            goods = tb_goods.objects.get(goods_id = service_detail_goods_id)
            response =  HttpResponseRedirect("/g_register")
            if 'unregist_tobepay_goodsid' in request.COOKIES:
                response.delete_cookie('unregist_tobepay_goodsid') 
            response.set_cookie('unregist_tobepay_goodsid',goods.goods_id,3600)
            #print(request.COOKIES['unregist_tobepay_goodsid'])
        return response

        


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



#logout by cyf
#def logout(request):
    #return render_to_response('index.html',{})

#激活账户 by cyf
def active_user(request, token):
	errors=[]
	try:
		user_name = token_confirm.confirm_validate_token(token)
	except:
		errors.append('对不起，验证链接已经过期')
		return render_to_response('auth.html',{'errors':errors})
	try:
		user = tb_user.objects.get(user_name = user_name)
	except tb_user.DoesNotExist:
		errors.append('对不起，您所验证的用户不存在，请重新注册')
		return render_to_response('auth.html',{'errors':errors})
	user.user_auth = 1
	user.save()
	return HttpResponseRedirect('/login',{})
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	

