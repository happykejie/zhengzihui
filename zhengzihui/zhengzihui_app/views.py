# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import json #用来将字典类型的数据序列化，然后传给模板以及js,不能序列化model实例
import jieba
from django.core import serializers #用来序列化model 传给js
from models import tb_item,tb_item_class,tb_item_pa,tb_article,tb_album,tb_pic
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
    now = last + 5 #每次只取10条
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
