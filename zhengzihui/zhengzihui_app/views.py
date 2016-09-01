
# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse as HR
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from itertools import chain
import random

import random
import top.api
import sys
import datetime
import time
import json #用来将字典类型的数据序列化，然后传给模板以及js,不能序列化model实例
import jieba,p_alipay.alipay
from token import Token
from django.core.mail import send_mail
from django.core import serializers #用来序列化model 传给js
#from models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News,Tb_Notice,Tb_Notice_Class,Tb_Apage,Tb_Apage_Class,tb_album,tb_pic,tb_accessory,tb_Artificial_Representations,tb_Message,tb_MessageText,tb_SysMessage,tb_item,tb_item_pa,tb_item_class,tb_goods,tb_album,tb_pic,tb_article,tb_goods_evaluation,tb_goods_click,tb_goods_class,tb_order,tb_item_click,tb_area
from models import *
SECRET_KEY = '+a^0qwojpxsam*xa5*y_5o+#9fej#+w72m998sjc!e)oj9im*y'
token_confirm = Token(SECRET_KEY)
appkey='23297047'
secret='45af9457a7d64b7ff5d04162f01d804a'

reload(sys)
sys.setdefaultencoding('utf8')
# Create your views here.
def index(request):
    a_click_items=[]
    click_items = tb_item_click.objects.order_by('-click_counter')[:4]
    for click_item in click_items:
        a_click_item = {}    
        a_click_item['id'] = click_item.item_id#获取项目id
        a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_click_item['item_ga'] = tb_item.objects.get(item_id=click_item.item_id).item_ga#获取项目资助金额
        item=tb_item.objects.get(item_id=click_item.item_id)
        item_pa_id=item.item_pa_id
        a_click_item['ipa_name'] = tb_item_pa.objects.get(ipa_id=item_pa_id).ipa_name#获取项目管理单位名称
        
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_click_item['item_publish'] = tb_item.objects.get(item_id=click_item.item_id).item_publish.strftime('%Y.%m.%d')#获取项目开始时间
        a_click_item['item_deadtime'] = tb_item.objects.get(item_id=click_item.item_id).item_deadtime.strftime('%Y.%m.%d')#获取项目截止时间
        start_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_click_item['item_consume_time'] = 100
            a_click_item['item_key'] = "已结束"
        else:
            a_click_item['item_consume_time'] = int(consume_time)
        

        a_click_items.append(a_click_item)
    return render(request,'index.html',{'a_click_items':a_click_items})
    

    
	#request.session['bumen']='全部'
	#request.session['jibie']='全部'
	#request.session['zhuangtai']='全部'
	#print (123)



	#return render_to_response('index.html',{})


#xcz 搜索
#为了显示当前路径，袁志修改，现在还有一些BUG
def Searchgoods(request):
    allthebumen=['经济与信息化','发展与改革','财政','科技','教育','文化','卫计','体育','知识产权','农业','林业','畜牧','渔业','粮食','中医药','国土','住建','交通','水利','能源','环保','商务','投资促进','工商','税务','民政','人社','扶贫','旅游','人民银行','银监','证监','保监','质监','药监','安监']
    a_items = []
    selected = {}
    flag = False
    ads=[]
    items=[]
    
    if (request.method=="GET"):	
        typefsearch=request.GET.get("Typeforsearch")
        goodsname=request.GET.get("inputitem")

        #后面取值用YZ
        goodsnametmp = goodsname
        #用于显示网站路径YZ
        search_content = "全部"
        if goodsname is not None:
	#fenleisousuo	
            if  ((typefsearch.encode("utf-8") )=="发布部门"):
                selected['bumen'] = goodsname.encode("utf-8")
                request.session['bumen'] = goodsname.encode("utf-8")
                request.session['search_content'] = goodsname.encode("utf_8")
                return HttpResponseRedirect('/search_result/')

	#xiangmusousuo        
	#分词
            #一样更新session中的'bumen'值YZ
            request.session['search_content']=goodsname.encode("utf-8")
            
            seg_list = jieba.cut(goodsname,cut_all=False)
        #搜索
            for gname in seg_list:
                #filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
                ads+=tb_item.objects.filter(item_name__contains = gname)
        #去重复
            for i in ads: 
                if i not in items:
                    items.append(i)

            a_items = get_and_set_info(items)
            ''' request.session['yz_search_result_temp'] = items
            test1 = request.session['yz_search_result_temp']
            print type(test1)'''
            #这里考虑把所有的获取到的
    
    #YZ
    if goodsnametmp!='':
        search_content = goodsnametmp
        if 'search_content' in request.session:
            del request.session['search_content']

    #获得热门推荐的项目YZ
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    context = {'selected':selected,'flag':flag,'items':a_items,'search_content':search_content,'recommend':recommend,}
    
    response =  render(request,'search_result.html',context)
    if goodsname == '':
        goodsname = '全部'
    
    response.set_cookie('search_content',goodsname)
    return response

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
	

    allthebumen = ['经济与信息化','发展与改革','财政','科技','教育','文化','卫计','体育','知识产权','农业','林业','畜牧','渔业','粮食','中医药','国土','住建','交通','水利','能源','环保','商务','投资促进','工商','税务','民政','人社','扶贫','旅游','人民银行','银监','证监','保监','质监','药监','安监']
    allthejibie = ['县级财政资金','市级财政资金','省级财政资金','中央财政资金']
    allthezhuangtai = ['截止申报','正在申报']

    if  (selected['jibie'].encode("utf-8") != '全部'):

    	jibielist = (selected['jibie'].encode("utf-8")).split(',')

    	for i in jibielist:
    		middle_items = chain(middle_items,(tb_item.objects.filter(item_level = (allthejibie.index(i)+1))))#匹配数据库的级别这一栏的数值YZ
        middle_items = list(middle_items)
    else:
    	middle_items=tb_item.objects.all()
    
    if  (selected['zhuangtai'].encode("utf-8") != '全部'):

    	for i in middle_items:
            print allthezhuangtai.index(selected['zhuangtai'].encode("utf-8"))
            if allthezhuangtai.index(selected['zhuangtai'].encode("utf-8")) == i.item_status:
    			tmiddle_items.append(i)
    else:
    	tmiddle_items=middle_items

    if  (selected['bumen'].encode("utf-8") != '全部'):
    	bumenlist = (selected['bumen'].encode("utf-8")).split(',')
    	for i in tmiddle_items:
    		for j in bumenlist:
    			if j in (i.item_about).encode("utf-8"):
    				items.append(i) 		
    else:

    	items=tmiddle_items

    if (len(items)>10):
    	items = items[:10]#不够10条报错
    else:
        items = items
    a_items = get_and_set_info(items)
    #获得热门推荐的项目YZ
    recommend = []
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    response = render(request,'search_result.html',{'selected':selected,'flag':flag,'items':a_items,'recommend':recommend,})
    if request.session['bumen']:
        
        response.set_cookie('search_content',str(request.session['bumen']))
    return response

##############################
#排序部分
##############################
#By 袁志
#按资金级别排序，顺序为中央、省级、市级、县级或者反序

'''获取数据库的项目信息并完成序列化，可以输入到模板的横条项目框中
    输入项目对象列表；输出一个列表，包含所有序列化的项目
'''
def get_the_hotrecommend():
    recommenditem = tb_item.objects.filter(is_recommend=1)
    return recommenditem[:4]

def get_and_set_info(items):
    a_items = []
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
    return a_items
def getthe_filteditem(request):
    items=[]
    
    a_items = []
    middle_items=[]
    tmiddle_items=[]
    
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


    allthebumen = ['经济与信息化','发展与改革','财政','科技','教育','文化','卫计','体育','知识产权','农业','林业','畜牧','渔业','粮食','中医药','国土','住建','交通','水利','能源','环保','商务','投资促进','工商','税务','民政','人社','扶贫','旅游','人民银行','银监','证监','保监','质监','药监','安监']
    allthejibie = ['县级财政资金','市级财政资金','省级财政资金','中央财政资金']
    allthezhuangtai = ['截止申报','正在申报']

    if  (selected['jibie'].encode("utf-8") != '全部'):

    	jibielist = (selected['jibie'].encode("utf-8")).split(',')

    	for i in jibielist:
    		middle_items = chain(middle_items,(tb_item.objects.filter(item_level = (allthejibie.index(i)+1))))#匹配数据库的级别这一栏的数值YZ
        middle_items = list(middle_items)
    else:
    	middle_items=tb_item.objects.all()

    if  (selected['zhuangtai'].encode("utf-8") != '全部'):

    	for i in middle_items:
            print allthezhuangtai.index(selected['zhuangtai'].encode("utf-8"))
            if allthezhuangtai.index(selected['zhuangtai'].encode("utf-8")) == i.item_status:
    			tmiddle_items.append(i)
    else:
    	tmiddle_items=middle_items

    if  (selected['bumen'].encode("utf-8") != '全部'):
    	bumenlist = (selected['bumen'].encode("utf-8")).split(',')
    	for i in tmiddle_items:
    		for j in bumenlist:
    			if j in (i.item_about).encode("utf-8"):
    				items.append(i)
    else:

    	items=tmiddle_items

    if (len(items)>10):
    	items = items[:10]#不够10条报错
    else:
        items = items
    search_content = request.COOKIES['search_content']
    if  search_content!= request.session['bumen'] and search_content!= request.session['jibie'] and search_content!= request.session['zhuangtai']:
        items = []
        return items
    return items

sortbyLevelFlag = True
def item_sortbyLevel(request):
    a_items = []
    items = []
    filted_item = getthe_filteditem(request)
    print request.COOKIES['search_content']
    print len(filted_item)
    if len(filted_item) == 0:
            goodsname = ''
            ads = []
            print request.COOKIES['search_content']
            if 'search_content' in request.COOKIES:
                goodsname = request.COOKIES['search_content']

            seg_list = jieba.cut(goodsname,cut_all=False)
        #搜索
            for gname in seg_list:
                #filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
                ads+=tb_item.objects.filter(item_name__contains = gname)
        #去重复
            for i in ads: 
                if i not in items:
                    items.append(i)
            filted_item = items
              
          
    
    print len(filted_item)
    items = []
    itemstemp = []
    if (sortbyLevelFlag==True):
        itemstemp = tb_item.objects.order_by('item_level')
        for item in itemstemp:
            if item in filted_item:
                items.append(item)

        global sortbyLevelFlag
        sortbyLevelFlag= False
    else:
        itemstemp = tb_item.objects.order_by('-item_level')
        for item in itemstemp:
            if item in filted_item:
                items.append(item)
        global sortbyLevelFlag
        sortbyLevelFlag= True

    a_items = get_and_set_info(items)
    #获得热门推荐的项目
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    return render(request,'search_result.html',{'items':a_items,'recommend':recommend,})

#按截至时间 排序存在的问题估计是因为 瀑布流每次只能取得10个所以 当超过10个之后再取的8 个 就出现了 重新排序，但是还是按顺序排列

###服务商排序
sortflag1=True
def search_result_sort_deadtime(request):
    a_items = []
    items = []
    filted_item = getthe_filteditem(request)
    
    if len(filted_item) == 0:
            goodsname = ''
            ads = []
           
            if 'search_content' in request.COOKIES:
                goodsname = request.COOKIES['search_content']

            seg_list = jieba.cut(goodsname,cut_all=False)
        #搜索
            for gname in seg_list:
                #filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
                ads+=tb_item.objects.filter(item_name__contains = gname)
        #去重复
            for i in ads: 
                if i not in items:
                    items.append(i)

            
            
            filted_item = items
    items = []
    itemstemp = []
    if(sortflag1==True):
    	itemstemp = tb_item.objects.order_by('item_deadtime')
        for item in itemstemp:
            if item in filted_item:
                items.append(item)

        global sortflag1
        sortflag1=False
    else:
    	itemstemp = tb_item.objects.order_by('-item_deadtime')

        for item in itemstemp:
            if item in filted_item:
                items.append(item)
        global sortflag1
        sortflag1=True

    a_items = get_and_set_info(items)
    #获得热门推荐的项目
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    return render(request,'search_result.html',{'items':a_items,'recommend':recommend,})

#综合排序 现在仅靠点击率来排序
sortbyComprihensiveFlag=True
def item_sortbyComprihensive(request):
    a_items = []
    items = []
    filted_item = getthe_filteditem(request)
    
    if len(filted_item) == 0:
            goodsname = ''
            ads = []
           
            if 'search_content' in request.COOKIES:
                goodsname = request.COOKIES['search_content']
                print goodsname.encode("utf-8")
                print "Iam Herea"
            seg_list = jieba.cut(goodsname,cut_all=False)
        #搜索
            for gname in seg_list:
                #filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
                ads+=tb_item.objects.filter(item_name__contains = gname)
        #去重复
            for i in ads: 
                if i not in items:
                    items.append(i)

            
            
            filted_item = items
    items = []
    
    itemstemp = []
    if (sortbyComprihensiveFlag==True):

        itemsinclick = tb_item_click.objects.order_by('-click_counter')

        for thing in itemsinclick:
            willappend = tb_item.objects.get(item_id=thing.item.item_id)
            itemstemp.append(willappend)

        for item in itemstemp:
            if item in filted_item:
                items.append(item)
        global sortbyComprihensiveFlag
        sortbyComprihensiveFlag=False
    else:
        itemsinclick = tb_item_click.objects.order_by('click_counter')
        for thing in itemsinclick:
            willappend = tb_item.objects.get(item_id=thing.item.item_id)
            itemstemp.append(willappend)
        for item in itemstemp:
            if item in filted_item:
                items.append(item)

        global sortbyComprihensiveFlag
        sortbyComprihensiveFlag=True
    a_items = get_and_set_info(items)
    #获得热门推荐的项目
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    return render(request,'search_result.html',{'items':a_items,'recommend':recommend,})

##############################
#排序部分结束
##############################
#项目项目详情加载YZ
def project_detail(request):
    project_detail_item_id = 1#取一个默认值
    if request.GET['id']:
        #能保证取到吗
        project_detail_item_id = request.GET['id']

    addclick = tb_item_click.objects.get(item_id = project_detail_item_id)
    if addclick==None:
        addclick = tb_item_click(itcl_id=0,item_id=project_detail_item_id,click_counter=1)
        addclick.save()
    else:
        addclick.click_counter += 1
        addclick.save()
    item = tb_item.objects.get(item_id = project_detail_item_id)
    item.item_pa_name = (tb_item_pa.objects.get(ipa_id=item.item_pa_id)).ipa_name #扩展对象属性，直接填写即可YZ
    item.item_pa_address = (tb_item_pa.objects.get(ipa_id=item.item_pa_id)).ipa_address
    #print item.item_pa_name
    #print item.item_pa_name
    article = tb_article.objects.filter(affiliation_id = project_detail_item_id)
    
    a_pics = []
    #article2 = article[2]
    if (len(article)==0):
        #获取项目起止时间
        gettimeInstance = tb_item.objects.get(item_id = project_detail_item_id)
        #获得热门推荐的项目
        recommendtemp = get_the_hotrecommend()
        recommend = get_and_set_info(recommendtemp)
        
        album = tb_album.objects.filter(album_type=0,affiliation_id=project_detail_item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            #print a_pic
            a_pics.append(a_pic)
        if not a_pics  :
            pic_url = '/static/zhengzihui_app/img_for_items/default.jpg'
            a_pics.append(pic_url)

        context = {'item':item,'article':article,'a_pics':a_pics,'recommend':recommend,'gettimeInstance':gettimeInstance,}
        #print item.item_pa_address

        return render(request,'project_detail.html',context)

    else:
        
        
        
        album = tb_album.objects.filter(album_type=0,affiliation_id=project_detail_item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            #print a_pic
            a_pics.append(a_pic)


        #获取项目起止时间
        gettimeInstance = tb_item.objects.get(item_id = project_detail_item_id)

        #获得热门推荐的项目
        recommendtemp = get_the_hotrecommend()
        recommend = get_and_set_info(recommendtemp)
        print "sdklfsdlflsdkflsdklksdlfksdlfksdkl"
        context = {'item':item,'article':article[0],'a_pics':a_pics,'recommend':recommend,'gettimeInstance':gettimeInstance,}
        return render(request,'project_detail.html',context)





#xcz项目信息滚动加载瀑布流
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
        middle_items = list(middle_items)            
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

    items = items[last:now]#YZ
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

        
#服务商列表展示 YZ
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
        return render('request','goods_list.html',{'service':service,'noservice':noservice,})
    else:
        #print id1
        id1 = int(id1)
        request.session['for_sort_itemid'] = id1
        tb_goods_list = tb_goods.objects.filter(item_id = id1)
        if len(tb_goods_list):
            service = 1
            noservice =0
        else:
            noservice = 1
            service = 0
        
        for goods in tb_goods_list:
            starttime = goods.goods_accept_starttime
            endtime = goods.goods_accept_endtime
            days_total = (endtime - starttime).days

            days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days
            print starttime
            print endtime
            print days_remain

            if days_remain <= 0:
                finish_percentage = 100
            else:
                finish_percentage = int((1-(float(days_remain)/float(days_total)))*100)
            goods.goods_remaintime = finish_percentage#完成百分比为对象添加的属性

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
            return render(request,'goods_list.html',{'tb_goods_list':tb_goods_list,'service':service,'noservice':noservice,})
        
        
#YZ 服务商详情页面
def service_details(request):

    if request.GET['goodsid']:
	    service_detail_goods_id = request.GET['goodsid']
    goods = tb_goods.objects.get(goods_id = service_detail_goods_id)#获得需要购买的项目的id对应的服务商
    if(len(tb_goods_click.objects.filter(goods_id =service_detail_goods_id ))):
        addclick = tb_goods_click.objects.filter(goods_id =service_detail_goods_id )[0]
        addclick.gocl_num +=1
        addclick.save()
    else:
        addclick = tb_goods_click(goods_id=service_detail_goods_id,goods_name = goods.goods_name,gocl_id =0,gocl_num =1)
        addclick.save()

    #计算日期百分比用于赋值进度条
    starttime = goods.goods_accept_starttime
    endtime = goods.goods_accept_endtime
    days_total = (endtime - starttime).days

    days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days

    if days_remain <= 0:
        finish_percentage = 100
    else:
        finish_percentage = int((1-(float(days_remain)/float(days_total)))*100)

    #
    #取服务对应的图片，赋值相册空间暂时还没有写，
    '''
    pics_url = []
    album = tb_album.objects.filter(affiliation_id=item.item_id)[0]#获取项目对应的相册id
    album_id = album.album_id
    pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片                                                               #切片14是去除前缀zhengzihui_app 否则图片不能显示
    for pic in pics:
        a_pic = pic.pic_object.url[14:] # 切片14是去除前缀zhengzihui_app 否则图片 ！！！部署时肯定还得修改
        pics_url.append(a_pic)
    '''
    pics_url = []
    pics_url.append('/static/zhengzihui_app/img_for_items/default.jpg')

    #用于推荐其他服务商
    allgoods_for_itemhere = tb_goods.objects.filter(item_id = goods.item_id).order_by("-goods_evaluation_good_star")#获取提供该项目支持的服务商，并按照他们的升序降序排列 排除自身！！根据评价的星星数为准
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
    publish_time_format = starttime.strftime("%Y-%m-%d %H:%I:%S")
    datetime_format = endtime.strftime("%Y-%m-%d %H:%I:%S")
    #判断是否是来自未登录用户的支付浏览
    showDialogflag = 0

    if 'unregist_tobepay_goodsid' in request.COOKIES:
        showDialogflag = 1
        response = render(request,'service_detail.html',{'goods':goods,'finish_percentage':finish_percentage,'pics_url':pics_url,'publish_time_format':publish_time_format,'datetime_format':datetime_format,'goods_recommend_display':goods_recommend_display,'showDialogflag':showDialogflag})
        response.delete_cookie('unregist_tobepay_goodsid')
        return response


    #print showDialogflag
    return render(request,'service_detail.html',{'goods':goods,'finish_percentage':finish_percentage,'pics_url':pics_url,'publish_time_format':publish_time_format,'datetime_format':datetime_format,'goods_recommend_display':goods_recommend_display,'showDialogflag':showDialogflag})

def sortServByComp(request):
    tb_goods_list = []
    if request.session['for_sort_itemid']:
        itemid = request.session['for_sort_itemid']

        #print "在排序当中"
        tb_goods_listTemp = tb_goods.objects.filter(item_id = itemid)#我们默认goods_sort代表点击率
        goodsorderTemp = tb_goods_click.objects.order_by('-gocl_num')
        for goods in goodsorderTemp:
            tb_goods_list.append(tb_goods.objects.get(goods_id = goods.goods_id))
        for goods in tb_goods_list:
            if goods not in tb_goods_listTemp:
                tb_goods_list.remove(goods)
                
            
        
        for goods in tb_goods_list:
            starttime = goods.goods_accept_starttime
            endtime = goods.goods_accept_endtime
            days_total = (endtime - starttime).days

            days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days


            if days_remain <= 0:
                finish_percentage = 100
            else:
                finish_percentage = int((1-(float(days_remain)/float(days_total)))*100)
            goods.goods_remaintime = finish_percentage#完成百分比为对象添加的属性
        return render(request,'goods_list.html',{'tb_goods_list':tb_goods_list,'service':True,'noservice':False,})
    else:
        return HttpResponse("没有选择相应的项目")



def sortServBypayahead(request):
    if request.session['for_sort_itemid']:
        itemid = request.session['for_sort_itemid']

        tb_goods_list = tb_goods.objects.order_by('goods_payahead').filter(item_id=itemid)#我们默认goods_sort代表点击率

        for goods in tb_goods_list:
            starttime = goods.goods_accept_starttime
            endtime = goods.goods_accept_endtime
            days_total = (endtime - starttime).days

            days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days


            if days_remain <= 0:
                finish_percentage = 100
            else:
                finish_percentage = int((1-(float(days_remain)/float(days_total)))*100)
            goods.goods_remaintime = finish_percentage#完成百分比为对象添加的属性
        return render(request,'goods_list.html',{'tb_goods_list':tb_goods_list,'service':True,'noservice':False,})
    else:
        return HttpResponse("没有选择相应的项目")

def sortServByaward(request):
    if request.session['for_sort_itemid']:
        itemid = request.session['for_sort_itemid']

        tb_goods_list = tb_goods.objects.order_by('goods_awardafter').filter(item_id=itemid)#我们默认goods_sort代表点击率

        for goods in tb_goods_list:
            starttime = goods.goods_accept_starttime
            endtime = goods.goods_accept_endtime
            days_total = (endtime - starttime).days

            days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days


            if days_remain <= 0:
                finish_percentage = 100
            else:
                finish_percentage = int((1-(float(days_remain)/float(days_total)))*100)
            goods.goods_remaintime = finish_percentage#完成百分比为对象添加的属性
        return render(request,'goods_list.html',{'tb_goods_list':tb_goods_list,'service':True,'noservice':False,})
    else:
        return HttpResponse("没有选择相应的项目")

    
    
#YZ 查看合同
def contact_details(request):
    goodsid = 0
    if request.GET['goodsid']:
        #contact_file = open("D:\Users\yuanzhi\zhengzihui\zhengzihui\zhengzihui_app\static\contact_file\contact.txt","r+")#这是一个绝对路径
        #contact_string = contact_file.read().decode("gbk")#需要解码一下~不知道为什么YZ

        #contact_file.close()
        goodsid = request.GET['goodsid']
        contact_string = '政资汇合同详情：等待完善'
        return render(request,'contact_details.html',{'goodsid':goodsid,'contact_string':contact_string})
    return HttpResponse("还没有选择项目")
#YZ
def order_details(request):
    goodsid = 0
    if request.GET['goodsid']:
        goodsid = int(request.GET['goodsid'])
        goods = tb_goods.objects.get(goods_id = goodsid)#取到服务对象
        item = tb_item.objects.get(item_id=goods.item_id)#取得对应的申报项目的对象
        item_spa = tb_item_pa(ipa_id=item.item_pa_id)#获得项目发布机构对象
        goods_spa = tb_service_provider(sp_id=goods.sp_id)#获得服务提供商的对象
        user_id = int(request.COOKIES['user_id'])
        buyer = tb_user.objects.get(user_id=user_id)#获取当前用户对象

        #生成随机的0-1000000的数，并不与数据库中的数相同;给order_no赋值
        order_no =random.randint(0,1000000)
        while( len(tb_order.objects.filter(order_no=order_no)) == 1 ):
            order_no =random.randint(0,1000000)
        print type(item.item_name)
        #add_time 用的是插入数据时便生成，即保存最后修改的时间错。
        allorder = tb_order.objects.all()
        lastid = allorder[len(allorder)-1].order_id

        order = tb_order(order_id=lastid+1,order_no=order_no,goods_id=goodsid,pay_no=order_no,item_id=item.item_id,item_name=item.item_name,sp_id=goods_spa.sp_id,\
                         sp_name=goods_spa.sp_name,buyer_id=buyer.user_id,buyer_name=buyer.user_name,buyer_email=buyer.user_email,\
                         payment_code=order_no,payment_time=None,final_time=None,good_amount=goods.goods_payahead,\
                         order_amount=goods.goods_payahead + goods.goods_awardafter,\
                         refund_amount=goods.goods_payahead,delay_time=None,order_from=1,express_id=1,express_no=1,eval_state=0,order_state=3,refund_state=0,lock_state=0,express_state=0)
        '''#order.order_no = order_no
        #order.goods_id = goodsid
        #order.pay_no = order_no #这里默认Pay_no与订单号一致
        order.item_id = item.item_id
        order.item_name = item.item_name
        order.sp_id = goods_spa.sp_id
        order.sp_name = goods_spa.sp_name
        order.buyer_id = buyer.user_id
        order.buyer_name = buyer.user_name
        order.buyer_email = buyer.user_email
        order.add_time = time.localtime()
        order.payment_code = order_no #暂时不知道什么用默认和订单号一致
        order.payment_time = None#暂时取值为Null,因为并没有支付，等待后续的线上支付或者线下支付
        order.final_time = None #当帮用户申报成功或者订单取消时取值
        order.good_amount = goods.goods_payahead # 收取的服务费用,首付费用
        order.order_amount = goods.goods_payahead + goods.goods_awardafter #订单的总金额是首付+奖金
        order.refund_amount = goods.goods_payahead
        order.delay_time = None #不知道干嘛的呀
        order.order_from = 1 #默认都是来之WEB端
        order.express_id =1 #默认值，应该是不会用到
        order.express_no= 1 #默认值，应该是不会用到
        order.eval_state = 0 #生成订单的时候肯定是没有评价的
        order.order_state = 3 #只是生成了订单后续的选择支付也没有选择完毕
        order.refund_state = 0 #生成订单时代表没有申请退款
        order.lock_state = 0 #正常，只有订单出现异常的时候才锁定
        order.express_state = 0 #是一个默认值，应该不会用到
        '''
        order.save()




    return render(request,'order_details.html',{'order':order,'goods':goods,'item':item,})
	
def order_completed(request):
    if request.GET['goodsid']:
        goodsid = request.GET['goodsid']
        return render(request,'order_completed.html',{'goodsid':goodsid,})

def shoucang_item(request):
    user_id = request.GET['user_id']
    item_id = request.GET['item_id']
    if len(tb_shoucang_item.objects.filter(user_id=user_id).filter(item_id=item_id)):
        return HttpResponse("您已经收藏过该项目")
    else:
        newOne = tb_shoucang_item(item_id=item_id,user_id=user_id)
        newOne.save()
        return HttpResponse("收藏项目成功")

def shoucang_goods(request):
    user_id = request.GET['user_id']
    goods_id = request.GET['goods_id']
    print(user_id)
    if len(tb_shoucang_goods.objects.filter(user_id=user_id).filter(goods_id=goods_id)):
        return HttpResponse("您已经收藏过该服务")
    else:
        newOne = tb_shoucang_goods(goods_id=goods_id,user_id=user_id)
        newOne.save()
        return HttpResponse("收藏服务成功")

#xcz    
def Payback(request):
	order_id=request.session['unpayedid']
	u = tb_order.objects.get(order_id=order_id)
	u['order_state']=2
	u.save()
	return HttpResponseRedirect('/zzh/user_center')
#xcz
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
    #a_recommend_items = []
    if 'user_id' in request.COOKIES:
        user_id = int(request.COOKIES['user_id'])
        user = tb_user.objects.get(user_id=user_id)
    else:
        return HttpResponse("请先登录账号;请返回到上级页面登录或者注册")
    if user.user_type == 0:
        click_items = tb_item_click.objects.order_by('-click_counter')[:15]#获取点击率前15的项目
        for click_item in click_items:
            a_click_item = {}
            a_click_item['id'] = click_item.item_id#获取项目id
            a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name#获取项目名字
            album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
            album_id = album.album_id
            a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            a_click_items.append(a_click_item)

    else:
        _industry = user.expand.company_industry
        click_items = tb_item.objects.filter(item_about__contains = _industry)
        for click_item in click_items:
            a_click_item = {}
            a_click_item['id'] = click_item.item_id  # 获取项目id
            a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name  # 获取项目名字
            album = tb_album.objects.filter(album_type=0, affiliation_id=click_item.item_id, is_default=1).order_by('-nacl_sort')[0]  # 获取项目对应的相册id
            album_id = album.album_id
            a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            a_click_items.append(a_click_item)
    '''recommend_items = tb_item.objects.filter(is_recommend=1).order_by('-item_id')[:15]#获取推荐的前15的项目
    for recommend_item in recommend_items:
        a_recommend_item= {}
        a_recommend_item['id'] = recommend_item.item_id#获取项目id
        a_recommend_item['name'] = recommend_item.item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=recommend_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_recommend_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_recommend_items.append(a_recommend_item)'''
    return render(request,'user.html',{'user':user,'a_click_items':a_click_items})


#总览 cyf
#def view_all(request):
   # return HttpResponse("hello world")




#用户信息 zss

    #我的信息
def my_info(request):
    user = []
    company = []
    usertype = False
    if request.COOKIES['user_id']:
        #print("2222")
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=3).order_by('-add_time')

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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            order.delete()
            return HttpResponse("0")
        else:
            return HttpResponse("1")

    #去评价
def order_commit(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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

#收藏管理
	#收藏的项目
def collects(request):
    userid = request.COOKIES['user_id']
    citems = tb_shoucang_item.objects.filter(user_id=userid)
    items = []
    a_items = []
    for item in citems:
        tmp = tb_item.objects.get(item_id=item.item_id)
        items.append(tmp)
    a_items = get_and_set_info(items)
    return render(request,'collects.html',{'items':a_items})
	#收藏的服务
def collect_serve(request):
    userid = request.COOKIES['user_id']
    cgoods = tb_shoucang_goods.objects.filter(user_id=userid)
    goods = []
    a_goods = []
    for good in cgoods:
        tmp = tb_goods.objects.get(goods_id=good.goods_id)
        goods.append(tmp)
    for good in goods:
            starttime = good.goods_accept_starttime
            endtime = good.goods_accept_endtime
            days_total = (endtime - starttime).days

            days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days
            print starttime
            print endtime
            print days_remain

            if days_remain <= 0:
                finish_percentage = 100
            else:
                finish_percentage = int((1-(float(days_remain)/float(days_total)))*100)
            good.goods_remaintime = finish_percentage#完成百分比为对象添加的属性
    return render(request,'collect_serve.html',{'goods':goods})
#评价管理

    #我的评价
def my_evaluate(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
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
            add2 = tb_user_expand()
            add.user_name = user_name
            add.user_password = user_password
            add.user_telephone = user_telephone
            add.user_email = user_email
            add.user_auth = 0
            '''add2.company_name = None
            add2.company_district = None
            add2.company_address = None
            add2.company_registered_capital = None
            add2.company_stuff_no = None
            add2.company_industry = None
            add2.company_nature = None
            add2.companyUserContactName = None
            add2.companyUserPhone = None
            add2.company_tel = None
            add2.company_email = None
            add2.save()
            expand = tb_user_expand.objects.order_by('-user_id')[:1]
            add.expand = expand'''
            add.expand=None
            add.save()
            user_id = add.user_id
            token = token_confirm.generate_validate_token(user_name)
            print(token)
            message = "\n".join([u'{0},欢迎注册政资汇'.format(user_name),u'请访问该链接，完成用户验证(链接1小时内有效):','/'.join(['127.0.0.1:8000','register2',token])])
            #message = '/'.join(['127.0.0.1:8000','register2',token])
            send_mail(u'注册用户验证信息', message, 'changyifan123@qq.com', [user_email])
            
            return render_to_response('register2.html')
    return render_to_response('g_register.html',{'errors':errors})
    



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
    #print(request.session['user_id'])
    #print(request.session['user_name_s'])
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
    if 'user_id' in request.COOKIES:
        userid = int(request.COOKIES['user_id'])
        user_name_getby_id = tb_user.objects.get(user_id = userid)
        response = render_to_response('index.html',{'user_name':user_name_getby_id})
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
                
                response.set_cookie('user_name',user_name)
                response.set_cookie('user_id',user.user_id)
                #print(user.expand.company_name)
                
                if 'unregist_tobepay_goodsid' in request.COOKIES:
                    goodsid = request.COOKIES['unregist_tobepay_goodsid']
                    responsenotpay = HttpResponseRedirect('/service_list/?itemid='+str(goodsid))
                    responsenotpay.set_cookie('user_name',user_name)
                    responsenotpay.set_cookie('user_id',user.user_id)
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
            response =  HttpResponseRedirect("/regCompany")
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
		
	

#自动提示xcz	
def  tag_autocomplete(request):  
        if request.GET.has_key("term"):
            tags = tb_item.objects.filter(item_name__icontains = request.GET["term"])[:10]
            results = [ x.item_name for x in tags ]
            es = json.dumps(results)
            #print(es)
           #i='\n'.join(tag.item_name for tag in tags)
            #j=i.encode("utf-8")
            #print(j)
            return  HR(es)
        return  HR()  
	
'''	#for test
def regCompany(request):
    return render_to_response("regCompany.html")'''
	
	
#正儿八经的企业注册 by cyf

def regCompany(request):
    add = []
    add2 = []
    if request.method == 'POST':
        companyUserName = request.POST.get("regName")
        companyUserPassword = request.POST.get("password")
        companyUserPassword2 = request.POST.get("password2")
        companyUserCompanyName = request.POST.get("companyName")
        companyUserCompanyLocation = request.POST.get("companyLocation")
        companyUserCompanyAddress = request.POST.get("companyAddress")
        companyUserCompanyCapital = request.POST.get("companyCapital")
        companyUserCompanyPeople = request.POST.get("companyPeople")
        companyUserCompanyIndustry = request.POST.get("companyIndustry")
        companyUserCompanyNature = request.POST.get("companyNature")
        companyUserContactName = request.POST.get("contactName")
        companyUserPhone = request.POST.get("phone")
        companyUserTelephone = request.POST.get("telphone")
        companyUserEmail = request.POST.get("email")
        securityCode = request.POST.get("securityCode")
        securityCode2 = request.POST.get("securityCode2")
        try:
            user1 = tb_user.objects.get(user_name = companyUserName)
            return render(request, 'regCompany.html', {'regName': companyUserName,
                                                       'password': companyUserPassword,
                                                       'password2': companyUserPassword2,
                                                       'companyName': companyUserCompanyName,
                                                       'companyLocation': companyUserCompanyLocation,
                                                       'companyAddress': companyUserCompanyAddress,
                                                       'companyCapital': companyUserCompanyCapital,
                                                       'companyPeople': companyUserCompanyPeople,
                                                       'companyIndustry': companyUserCompanyIndustry,
                                                       'companyNature': companyUserCompanyNature,
                                                       'contactName': companyUserContactName, 'phone': companyUserPhone,
                                                       'telphone': companyUserTelephone, 'email': companyUserEmail,
                                                       'securityCode2': securityCode,
                                                       'message': '<script type="text/javascript">alert("用户名重复！");</script>'})
        except tb_user.DoesNotExist:
            pass
        try:
            user2 = tb_user_expand.objects.get(company_name = companyUserCompanyName)
            return render(request, 'regCompany.html', {'regName': companyUserName,
                                                       'password': companyUserPassword,
                                                       'password2': companyUserPassword2,
                                                       'companyName': companyUserCompanyName,
                                                       'companyLocation': companyUserCompanyLocation,
                                                       'companyAddress': companyUserCompanyAddress,
                                                       'companyCapital': companyUserCompanyCapital,
                                                       'companyPeople': companyUserCompanyPeople,
                                                       'companyIndustry': companyUserCompanyIndustry,
                                                       'companyNature': companyUserCompanyNature,
                                                       'contactName': companyUserContactName, 'phone': companyUserPhone,
                                                       'telphone': companyUserTelephone, 'email': companyUserEmail,
                                                       'securityCode2': securityCode,
                                                       'message': '<script type="text/javascript">alert("该公司已被注册！");</script>'})
        except tb_user_expand.DoesNotExist:
            pass
        if securityCode != securityCode2:
            return render(request, 'regCompany.html', {'regName': companyUserName,
                                                       'password': companyUserPassword,
                                                       'password2': companyUserPassword2,
                                                       'companyName': companyUserCompanyName,
                                                       'companyLocation': companyUserCompanyLocation,
                                                       'companyAddress': companyUserCompanyAddress,
                                                       'companyCapital': companyUserCompanyCapital,
                                                       'companyPeople': companyUserCompanyPeople,
                                                       'companyIndustry': companyUserCompanyIndustry,
                                                       'companyNature': companyUserCompanyNature,
                                                       'contactName': companyUserContactName, 'phone': companyUserPhone,
                                                       'telphone': companyUserTelephone, 'email': companyUserEmail,
                                                       'securityCode2': securityCode,
                                                       'message': '<script type="text/javascript">alert("短信验证码错误！");</script>'})
        add = tb_user()
        add2 = tb_user_expand()
        add.user_name = request.POST.get("regName")
        add.user_password = request.POST.get("password")
        add.user_telephone = request.POST.get("telphone")
        add.user_email = request.POST.get("email")
        add.user_type = 1
        add.user_auth = 1
        add2.company_name = request.POST.get("companyName")
        add2.company_district = request.POST.get("companyLocation")
        add2.company_address = request.POST.get("companyAddress")
        add2.company_registered_capital = request.POST.get("companyCapital")
        add2.company_stuff_no = request.POST.get("companyPeople")
        add2.company_industry = request.POST.get("companyIndustry")
        add2.company_nature = request.POST.get("companyNature")
        add2.companyUserContactName = request.POST.get("contactName")
        add2.companyUserPhone = request.POST.get("phone")
        add2.company_tel = request.POST.get("telphone")
        add2.company_email = request.POST.get("email")
        add2.save()
        expand = tb_user_expand.objects.get(company_name = companyUserCompanyName)
        add.expand = expand
        add.save()
        return render_to_response("index.html", {})
    return render_to_response("regCompany.html")


#雅致的手机验证，for test，by cyf
def register_sms(request):
    companyUserName = request.POST.get("regName")
    companyUserPassword = request.POST.get("password")
    companyUserPassword2 = request.POST.get("password2")
    companyUserCompanyName = request.POST.get("companyName")
    companyUserCompanyLocation = request.POST.get("companyLocation")
    companyUserCompanyAddress = request.POST.get("companyAddress")
    companyUserCompanyCapital = request.POST.get("companyCapital")
    companyUserCompanyPeople = request.POST.get("companyPeople")
    companyUserCompanyIndustry = request.POST.get("companyIndustry")
    companyUserCompanyNature = request.POST.get("companyNature")
    companyUserContactName = request.POST.get("contactName")
    companyUserPhone = request.POST.get("phone")
    companyUserTelephone = request.POST.get("telphone")
    companyUserEmail = request.POST.get("email")
    securityCode=random.randint(1000, 9999)
    req=top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(appkey,secret))

    req.extend="123456"
    req.sms_type="normal"
    req.sms_free_sign_name="身份验证"
    req.sms_param='{"code":"%d","product":"雅峙"}'%(securityCode)
    req.rec_num=companyUserTelephone
    req.sms_template_code="SMS_4465526"
    try:
	    resp= req.getResponse()
	    print(resp)
    except Exception,e:
	    print(e)
	    return HttpResponse("sms error!")
    finally:
	    return render(request,'regCompany.html',{'regName':companyUserName, 'password':companyUserPassword, 'password2':companyUserPassword2, 'companyName':companyUserCompanyName, 'companyLocation':companyUserCompanyLocation, 'companyAddress':companyUserCompanyAddress, 'companyCapital':companyUserCompanyCapital, 'companyPeople':companyUserCompanyPeople, 'companyIndustry':companyUserCompanyIndustry, 'companyNature':companyUserCompanyNature, 'contactName':companyUserContactName, 'phone':companyUserPhone, 'telphone':companyUserTelephone, 'email':companyUserEmail, 'securityCode2':securityCode, 'message':'<script type="text/javascript">alert("验证码已发送！");</script>'})






def cmap(request):
    #ce shi shu ju mu qian xie si le 

    #request.COOKIES['user_id']="2016"
    if 'user_id' in request.COOKIES:
        if(len(tb_customcompany.objects.filter(company_id=request.COOKIES['user_id'])))==0 :
            return  render_to_response("e_customization.html",{})
        else:
            if(tb_customcompany.objects.get(company_id=request.COOKIES['user_id'])).conclusion=="":
                return HttpResponse("等待处理")
            else:
                user_id=request.COOKIES['user_id']
                #conc=tb_customcompany.objects.get(company_id=user_id).conclusion 
                #wu shu ju  xie si le de ce shi shui chan 
                conc="水产"
                A=tb_user.objects.get(user_id = user_id).user_name
                B=tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  1)
                C=tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  2)
                D=tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  3)
                E=tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  4)
                if (len(B)==0):
                    B=""
                else:
                    B=str(tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  1)[0].item_id)+"."+tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  1)[0].item_name
                if (len(C)==0):
                    C=""
                else:
                    C=str(tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  2)[0].item_id)+"."+tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  2)[0].item_name
                if (len(D)==0):
                    D=""
                else:
                    D=str(tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  3)[0].item_id)+"."+tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  3)[0].item_name
                if (len(E)==0):
                    E=""
                else:
                    E=str(tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  4)[0].item_id)+"."+tb_item.objects.filter(item_about__contains =  conc) .filter(item_level=  4)[0].item_name

                #A="100"
                #B="110"
                #C="120"
                #D="130"
                #E="140"
                return render_to_response("cust_map.html",{'A':A,'B':B,'C':C,'D':D,'E':E})

def custom(request):
     #return render_to_response("e_customization.html",{})
    #ce shi shu ju mu qian xie si le 
    #request.COOKIES['user_id']="2016"
    if 'user_id' in request.COOKIES:
        if(len(tb_customcompany.objects.filter(company_id=request.COOKIES['user_id'])))==0:
          #print (123) 
          return render_to_response("e_customization.html",{})
        else:
            return HttpResponse("等待处理")       
           
        #else:
         #   return HttpResponse("map for e_man")
  #  else:
     #   return HttpResponseRedirect('/login',{})
    #return render_to_response("e_customization.html",{})

def savec(request):
    #ce shi shu ju mu qian xie si le 
    #request.COOKIES['user_id']="2016"
    if (request.method=="POST"):
        company_id=request.COOKIES['user_id']
        hangye=request.POST.get("hangye")
        bumen=request.POST.get("bumen")
        jibie=request.POST.get("jibie")
        guquan=request.POST.get("guquan")
        zhaiquan=request.POST.get("zhaiquan")
        ziben=request.POST.get("ziben")
        zimiaoshu=request.POST.get("qiyejianjie")
        xiangmumiaoshu=request.POST.get("xiangmujianjie")

        zimiaoshutu=request.POST.get("jianjiefile")
        xiangmutu=request.POST.get("xiangmufile")
        #print(xiangmutu)
        add =   tb_customcompany()
        add.company_id=company_id
        add.custom_hangye=hangye
        add.custom_bumen=bumen
        add.custom_jiebie =jibie
        add.wanted_guquan=guquan
        add.wanted_rongzi =zhaiquan
        add.wanted_ziben=ziben
        add.self_des=zimiaoshu
        add.item_des=xiangmumiaoshu
        add.self_file= zimiaoshutu
        add.item_file= xiangmutu
        add.conclusion=""
        add.save()
        #print(111)
        return HttpResponseRedirect('/index',{})
    return render_to_response("e_customization.html",{})

def busindex(request):
	return render_to_response("bus_index.html",{})


def buspubservice(request):
	sp_id=9
	#if 'user_id' in request.COOKIES:
	#	sp_id=request.COOKIES['user_id']
	if(request.method=="POST"):
		mod=""
		fea=""
		payt=0
		payth=0
		if(request.POST.get("modon")):
			mod+=request.POST.get("modon")
			pay=request.POST.get("paya")
		if(request.POST.get("modtw")):
			mod+=request.POST.get("modtw")
			payt=request.POST.get("payb")
		if(request.POST.get("modth")):
			mod+=request.POST.get("modth")
			payth=request.POST.get("payc")
		#print(mod)
		if(request.POST.get("feaon")):
			fea+=request.POST.get("feaon")
			fea+="  "
		if(request.POST.get("featw")):
			fea+=request.POST.get("featw")
			fea+="  "
		if(request.POST.get("feath")):
			fea+=request.POST.get("feath")
			fea+="  "
		if(request.POST.get("feafo")):
			fea+=request.POST.get("feafo")
			fea+="  "
		if(request.POST.get("feafi")):
			fea+=request.POST.get("feafi")
			fea+="  "
		#print(fea)
		
		sname=request.POST.get("sname")
		#payt=request.POST.get("payb")
		fuwuneirong=request.POST.get("fuwuneirong")
		fuwuliucheng=request.POST.get("fuwuliucheng")
		chenggonganli=request.POST.get("chenggonganli")
		fanli=request.POST.get("fanli")
		#print(fanli)
		add=tb_goods_wfc()
		add.goods_payahead=pay
		add.goods_awardmid=payt
		add.goods_awardafter=payth
		#add.goods_id
		add.goods_name=sname
		add.item_id=1
		add.sp_id=sp_id
		add.goods_fanli=fanli
		add.fea=fea
		add.cont=fuwuneirong
		add.steps=fuwuliucheng
		add.exa=chenggonganli
		add.smod=mod
		add.save()
        #print(111)
		return render_to_response("buswaitforchecked.html",{})
	else:
		return render_to_response("buspubservice.html",{})
	
def busmaservice(request):
	sp_id=1
	#if 'user_id' in request.COOKIES:
	#	sp_id=request.COOKIES['user_id']
	goods = tb_goods.objects.filter(sp_id=sp_id)
	return render_to_response("busmaservice.html",{'goods_list':goods})
	

	
def merge_service_details(request):
	sp_id=9
	#if 'user_id' in request.COOKIES:
	#	sp_id=request.COOKIES['user_id']
	if (request.method=="GET"):
		mid=request.GET.get("goodsid")
		#print (mid)
		goods=tb_goods.objects.get(goods_id=mid)
		return render_to_response("busmerservice.html",{'goods':goods})
	else:
		did=request.POST.get("deletegoodsid")
		dgoods=tb_goods.objects.get(goods_id=did)
		dgoods.goods_show=0
		dgoods.goods_status=0
		dgoods.save()
		mod=""
		fea=""
		payt=0
		payth=0
		pay=request.POST.get("pay")
		if(request.POST.get("modon")):
			mod+=request.POST.get("modon")
			pay=request.POST.get("paya")
		if(request.POST.get("modtw")):
			mod+=request.POST.get("modtw")
			payt=request.POST.get("payb")
		if(request.POST.get("modth")):
			mod+=request.POST.get("modth")
			payth=request.POST.get("payc")
		#print(mod)
		if(request.POST.get("feaon")):
			fea+=request.POST.get("feaon")
			fea+="  "
		if(request.POST.get("featw")):
			fea+=request.POST.get("featw")
			fea+="  "
		if(request.POST.get("feath")):
			fea+=request.POST.get("feath")
			fea+="  "
		if(request.POST.get("feafo")):
			fea+=request.POST.get("feafo")
			fea+="  "
		if(request.POST.get("feafi")):
			fea+=request.POST.get("feafi")
			fea+="  "
		#print(fea)
		pay=request.POST.get("paya")
		sname=request.POST.get("sname")
		#payt=request.POST.get("payb")
		fuwuneirong=request.POST.get("fuwuneirong")
		fuwuliucheng=request.POST.get("fuwuliucheng")
		chenggonganli=request.POST.get("chenggonganli")
		fanli=request.POST.get("fanli")
		#print(fanli)
		add=tb_goods_wfc()
		add.goods_payahead=pay
		add.goods_awardmid=payt
		add.goods_awardafter=payth
		#add.goods_id
		add.goods_name=sname
		add.item_id=1
		add.sp_id=sp_id
		add.goods_fanli=fanli
		add.fea=fea
		add.cont=fuwuneirong
		add.steps=fuwuliucheng
		add.exa=chenggonganli
		add.smod=mod
		add.save()
        #print(111)
		return render_to_response("buswaitforchecked.html",{})
		
	
	
	


