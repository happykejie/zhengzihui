#-*- coding:utf-8 -*-

from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from pages import Page
from forms import FRequireInfoForm
from error import Error
import random
import top.api
import pdb


####free require part##########################################################


#for SMS verification
appkey='23297047'
secret='45af9457a7d64b7ff5d04162f01d804a'


# Create your views here.

def _do_exception(func):
    def wrapper(request):
        try:
            return func(request)
        except Exception:
            return render(request,Page.require_error,{})

    return wrapper

#@_do_exception
def frame(request):
	form = FRequireInfoForm()
        return render(request,Page.frame,{'form':form})


def verification(request):
    if request.method=='POST':
        mobile_num = request.POST['mobile_num']
        vcode=_send_vcode(mobile_num)
        if vcode!='': #send verification
            #save this number at session
            request.session['vcode'] = str(vcode)
            request.session['mobile_num'] = mobile_num
            return HttpResponse('success')
    
    return HttpResponse('fail')


#@_do_exception
def require_finish(request):
    if request.method == 'POST':
        form = FRequireInfoForm(request.POST)
        err_msg = Error()
        if form.is_valid() and _check_vcode(request) and _check_mobile_num(request):
            del request.session['mobile_num']
            del request.session['vcode']
            form.save()
            #return HttpResponse('success to add this record.')
            return HttpResponseRedirect('/index/')
        elif not _check_vcode(request):
            err_msg.vcode = '无效验证码'
        elif not  _check_mobile_num(request):
            err_msg.mobile_num ='无效手机号码' 
        else:
            err_msg.other = '我们遭遇了一个未预料的错误，请联系管理员'

    else:
        form = FRequireInfoForm()

    return render(request,Page.frame,{'err_msg':err_msg,'form':form})


"""the following part is inner function"""
def _send_vcode(mobile_num):
    """send verification to mobile number.
    Args:
        mobile_num: mobile number.
    return:
        success: vcode string.
        fail: null string.
    """

    vcode=random.randint(1000, 9999)
    req=top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(appkey,secret))

    req.extend="123456"
    req.sms_type="normal"
    req.sms_free_sign_name="身份验证"
    req.sms_param='{"code":"%d","product":"雅峙"}'%(vcode)
    req.rec_num=mobile_num
    req.sms_template_code="SMS_4465526"

    try:
	    resp= req.getResponse()
	    return vcode
    except Exception,e:
	    print(e)
	    return ''


def _check_require_type(require_type):
    return True


def _check_vcode(request):
    vcode_s = request.session.get('vcode','invalid')
    vcode_p = request.POST.get('vcode','')
    if vcode_s!='invalid' and vcode_s==vcode_p:
        return True

    return False


def _check_mobile_num(request):
    mobile_num = request.session.get('mobile_num','invalid')
    if mobile_num!='invalid':
        return True

    return False



####supporting center part#####################################################
#这部分主要是摘抄自“服务列表页面”

from itertools import chain
from zhengzihui_app.models import *
import time
from models import *
from .test.test import insert_test_data_for_sc_item

def supporting_center_frame(request):
    if sc_item.objects.count()==0: # 自动添加测试数据,发布版中需要删掉
        insert_test_data_for_sc_item()

    a_items = []
    items=[]
    selected = {}
    flag = False
    if 'type' in request.session:
        value = request.session['type']
        selected['type'] = value
        flag = True
    else:
        request.session['type'] = '全部'
        selected['type'] = '全部'

    allthetype = ['工商代理','资质代办','知识产权','财务服务','其他']

    if  (selected['type'].encode("utf-8") != '全部') and (selected['type'].encode("utf-8") != ''):
    	typelist = (selected['type'].encode("utf-8")).split(',')
    	for i in typelist:
    		items = chain(items,(sc_item.objects.filter(item_type 
                        = (allthetype.index(i)+1))))#匹配数据库的级别这一栏的数值YZ
        items = list(items)
    else:
    	items=sc_item.objects.all()

    if (len(items)>10):
    	items = items[:10]#不够10条报错
    else:
        items = items

    a_items = get_and_set_info_for_sc(items)
    #获得热门推荐的项目YZ
    recommend = []
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    response = render(request,'sc_search_result.html',{'selected':selected
                        ,'flag':flag,'items':a_items,'recommend':recommend,})

    return response


def supporting_center_iteminfo(request):
    """item information.
    """
    project_detail_item_id = 1#取一个默认值
    if request.GET['id']:
        #能保证取到吗
        project_detail_item_id = request.GET['id']

    addclick = sc_item_click.objects.filter(item_id = project_detail_item_id)
    if addclick.exists()==False:
        addclick = sc_item_click(itcl_id=0,item_id=project_detail_item_id
                    ,click_counter=1)
        addclick.save()
    else:
        addclick[0].click_counter += 1
        addclick[0].save()
    item = sc_item.objects.get(item_id = project_detail_item_id)
    # item.item_pa_name = (sc_item_pa.objects.get(ipa_id=item.item_pa_id)).ipa_name #扩展对象属性，直接填写即可YZ
    # item.item_pa_address = (sc_item_pa.objects.get(ipa_id=item.item_pa_id)).ipa_address
    article = sc_article.objects.filter(affiliation_id = project_detail_item_id)
    
    a_pics = []
    if (len(article)==0):
        #获取项目起止时间
        gettimeInstance = sc_item.objects.get(item_id = project_detail_item_id)
        #获得热门推荐的项目
        recommendtemp = get_the_hotrecommend()
        recommend = get_and_set_info(recommendtemp)
        
        albums = sc_album.objects.filter(album_type=0,affiliation_id=project_detail_item_id,is_default=1).order_by('-nacl_sort');
        if albums.exists(): #获取前四张图片
            pics = sc_pic.objects.filter(album_id=albums[0].album_id).order_by('-pic_id')[0:4]
            if pics.exists():
                for pic in pics:
                    a_pic = pic.pic_object.url[14:]
                    a_pics.append(a_pic)
            else:
                pic_url = '/static/zhengzihui_app/img_for_items/default.jpg'
                a_pics.append(pic_url)

        else:
            pic_url = '/static/zhengzihui_app/img_for_items/default.jpg'
            a_pics.append(pic_url)

        context = {'item':item,'article':article,'a_pics':a_pics,'recommend':recommend,'gettimeInstance':gettimeInstance,}

        return render(request,'sc_iteminfo.html',context)

    else:
        
        album = sc_album.objects.filter(album_type=0
                ,affiliation_id=project_detail_item_id
                ,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        pics = sc_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]#获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            a_pics.append(a_pic)

        if not a_pics  :
            pic_url = '/static/zhengzihui_app/img_for_items/default.jpg'
            a_pics.append(pic_url)

        #获取项目起止时间
        gettimeInstance = sc_item.objects.get(item_id = project_detail_item_id)

        #获得热门推荐的项目
        recommendtemp = get_the_hotrecommend()
        recommend = get_and_set_info(recommendtemp)
        print "sdklfsdlflsdkflsdklksdlfksdlfksdkl"
        context = {'item':item,'article':article[0],'a_pics':a_pics
                    ,'recommend':recommend,'gettimeInstance':gettimeInstance,}
        return render(request,'sc_iteminfo.html',context)


def supporting_center_filter_labels(request):
    keys = request.GET['filterkeys']
    if 'bumen' in request.GET:
        request.session['bumen'] = keys
    if 'jibie' in request.GET:
        request.session['jibie'] = keys
    if 'zhuangtai' in request.GET:
        request.session['zhuangtai'] = keys
    return HttpResponseRedirect('/free_require/supporting_center/frame/')


def supporting_center_shoucang_item(request):
    user_id = request.GET['user_id']
    item_id = request.GET['item_id']
    if len(tb_shoucang_item.objects.filter(user_id=user_id).filter(item_id=item_id)):
        return HttpResponse("您已经收藏过该项目")
    else:
        newOne = tb_shoucang_item(item_id=item_id,user_id=user_id)
        newOne.save()
        return HttpResponse("收藏项目成功")



def sc_search_result_load(request):
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

def get_and_set_info_for_sc(items):
    a_items = []
    for item in items:
        a_item = {}
        a_item['item_id'] = item.item_id # 获取项目id
        a_item['item_type'] = item.item_type
        a_item['item_name'] = item.item_name# 获取项目名字
        a_item['price'] = item.price 
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_item['start_time'] = item.start_time.strftime('%Y.%m.%d')
        a_item['end_time'] = item.end_time.strftime('%Y.%m.%d')
        start_seconds = time.mktime(item.start_time.timetuple())  #utc 0时区
        end_seconds = time.mktime(item.end_time.timetuple())
        delta = end_seconds-start_seconds if end_seconds-start_seconds>0 else 1
        consume_time = (now_seconds-start_seconds)/delta*100
        if consume_time >= 100:
            a_item['item_consume_time'] = 100
            a_item['item_key'] = "已结束"
        else:
            a_item['item_consume_time'] = int(consume_time)
            a_item['item_key'] = item.item_type
        a_item['supplier'] = item.supplier

        
        try:
            album = tb_album.objects.filter(album_type=1,affiliation_id=item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
            album_id = album.album_id
            a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        except:
            a_item['pic_url'] = "/static/zhengzihui_app/img_for_items/2016/05/06/a2.jpg"

        a_items.append(a_item)
    return a_items


def get_and_set_info(items):
    a_items = []
    for item in items:
        a_item = {}
        a_item['item_id'] = item.item_id  # 获取项目id
        a_item['item_name'] = item.item_name  # 获取项目名字
        a_item['item_ga'] = item.item_ga
        a_item['item_key'] = item.item_key
        a_item['item_about'] = item.item_about
        now_seconds = time.time() - 8 * 60 * 60  # 距离1970的秒数  将东八区转换为0时区
        a_item['item_publish'] = item.item_publish.strftime('%Y.%m.%d')
        a_item['item_deadtime'] = item.item_deadtime.strftime('%Y.%m.%d')
        start_seconds = time.mktime(item.item_publish.timetuple())  # utc 0时区
        end_seconds = time.mktime(item.item_deadtime.timetuple())
        consume_time = (now_seconds - start_seconds) / (end_seconds - start_seconds) * 100
        if consume_time > 100:
            a_item['item_consume_time'] = 100
            a_item['item_key'] = "已结束"
        else:
            a_item['item_consume_time'] = int(consume_time)
        a_item['pa'] = tb_item_pa.objects.get(ipa_id=item.item_pa_id).ipa_name
        album = tb_album.objects.filter(album_type=0, affiliation_id=item.item_id, is_default=1).order_by('-nacl_sort')[
            0]  # 获取项目对应的相册id
        album_id = album.album_id
        a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[
                            14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_item['order_num'] = len(tb_order.objects.filter(item_id=item.item_id))  # 获取项目对应订单的数量
        a_items.append(a_item)
    return a_items


