#coding=utf-8

from views import *

#政资会首页部分
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

        request.session['bumen']='全部'
        request.session['jibie']='全部'
        request.session['zhuangtai']='全部'
    return render(request,'index.html',{'a_click_items':a_click_items})


#xcz 搜索ITEMS，直接搜索项目部分
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
            if  ((typefsearch.encode("utf-8") )=="所属行业"):
                selected['bumen'] = goodsname.encode("utf-8")
                request.session['bumen'] = goodsname.encode("utf-8")
                request.session['search_content'] = goodsname.encode("utf_8")
                return HttpResponseRedirect('/search_result/')

	#xiangmusousuo        
	#分词
            #一样更新session中的'bumen'值YZ
            request.session['search_content']=goodsname.encode("utf-8")
            selected['bumen'] = '来自xu搜索'
            request.session['bumen'] = '来自xu搜索'

            
            seg_list = jieba.cut(goodsname,cut_all=False)
        #搜索
            for gname in seg_list:
                #filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
                ads+=tb_item.objects.filter(item_name__contains = gname)
        #去重复
            for i in ads: 
                if i not in items:
                    items.append(i)
            #print items
            a_items = get_and_set_info(items)
            print a_items
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


#搜索ITEMS根据已输入字自动提示xcz	
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



#搜索后页面的分类显示
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
	
    #print(selected['bumen'])
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
        #待修改，只是根据item_status字段来判断的话会出错。因为一旦给值就固定了，需要根据截止时间来判断
        if selected['zhuangtai'] == '正在申报':
            for i in middle_items:
                #print allthezhuangtai.index(selected['zhuangtai'].encode("utf-8"))
                endtime = i.item_deadtime
                days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days
                print days_remain
                if days_remain>0:
    			    tmiddle_items.append(i)

        else:
            for i in middle_items:

                endtime = i.item_deadtime
                days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days
                if days_remain<=0:
    			    tmiddle_items.append(i)


    else:
    	tmiddle_items=middle_items




    list_temp2 = []
    if  (selected['bumen'].encode("utf-8") != '全部'):
        bumenlist = (selected['bumen'].encode("utf-8")).split(',')
        print bumenlist
        for bumen in bumenlist:
	    #print (bumen)
	    if ":" not in bumen:
		#print (bumen)
		for i in tmiddle_items:
			if bumen in (i.item_about).encode("utf-8"):
				items.append(i)
	    else:
            	list_temp1 = bumen.split(":",1)
            	if len(list_temp1)>1:
                	str_temp = list_temp1[1]
                	list_temp2 = str_temp.split("/")

           	if len(list_temp2)!=0:
                	for i in tmiddle_items:
                    		for j in list_temp2:
                        		if j in (i.item_about).encode("utf-8"):
                            			if i not in items:#去重复
                                			items.append(i)
	    
    else:
    	items=tmiddle_items
    #print(items)

    if (len(items)>10):
    	items = items[:10]#不够10条报错
    else:
        items = items
    #来自主页的检索需要置空此处，否则会多查询结果
    if selected['bumen'] == '来自xu搜索':
        items=[]

    a_items = get_and_set_info(items)
    #获得热门推荐的项目YZ
    recommend = []
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    response = render(request,'search_result.html',{'selected':selected,'flag':flag,'items':a_items,'recommend':recommend,})
    if request.session['bumen']:
        
        response.set_cookie('search_content',str(request.session['bumen']))
    return response






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


#xcz支付反馈    
def Payback(request):
	order_id=request.session['unpayedid']
	u = tb_order.objects.get(order_id=order_id)
	u['order_state']=2
	u.save()
	return HttpResponseRedirect('/zzh/user_center')

#xcz支付
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
#企业画报
def cmap(request):
    #ce shi shu ju mu qian xie si le 

    #request.COOKIES['user_id']="2016"
    if 'user_id' not in request.COOKIES:
        return HttpResponseRedirect('/regCompany/')
    if 'user_id' in request.COOKIES:
	if(tb_user.objects.get(user_id=request.COOKIES['user_id']).user_type)==0:
	    return HttpResponse("您不是企业用户，无法使用此功能")
        if(len(tb_customcompany.objects.filter(company_id=request.COOKIES['user_id'])))==0 :
            return  render_to_response("e_customization.html",{})
        else:
            if(tb_customcompany.objects.get(company_id=request.COOKIES['user_id'])).conclusion=="":
                return HttpResponse("等待处理")
            else:
                user_id=request.COOKIES['user_id']
                conc=tb_customcompany.objects.get(company_id=user_id).conclusion 
                #wu shu ju  xie si le de ce shi shui chan 
                #conc="水产"
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
    else:
        return HttpResponseRedirect('/regCompany/')

 
#画布或者自定义入口
def custom(request):
     #return render_to_response("e_customization.html",{})
    #ce shi shu ju mu qian xie si le 
    #request.COOKIES['user_id']="2016"
    if 'user_id' not in request.COOKIES:
        return HttpResponseRedirect('/regCompany/')
    if 'user_id' in request.COOKIES:
        if(len(tb_customcompany.objects.filter(company_id=request.COOKIES['user_id'])))==0:
          #print (123) 
          return render_to_response("e_customization.html",{})
        else:
            return HttpResponseRedirect('/custmap')       
           
        #else:
         #   return HttpResponse("map for e_man")
  #  else:
     #   return HttpResponseRedirect('/login',{})
    #return render_to_response("e_customization.html",{})

#用户自定义自身属性给后台验证选择推荐项目tb_customcompany
def savec(request):
    #ce shi shu ju mu qian xie si le 
    #request.COOKIES['user_id']="2016"
    if 'user_id' not in request.COOKIES:
        return HttpResponseRedirect('/regCompany/')
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

#发布服务待后台验证
def buspubservice(request):
	sp_id=1
	'''if 'sp_id' not in request.COOKIES:
		#sp_id=request.COOKIES['user_id']
		return HttpResponseRedirect('/merchant')'''
	if 'sp_id' in request.COOKIES:
		sp_id=request.COOKIES['sp_id']
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
	
#企业端，服务管理
def busmaservice(request):
	sp_id=1
	'''if request.COOKIES['sp_id'] is None:
		#sp_id=request.COOKIES['user_id']
		print 111
		return HttpResponseRedirect('/merchant')
	
	'''
	#if sp_id in request.COOKIES:
	sp_id=request.COOKIES['sp_id']
	#print (sp_id)
	goods = tb_goods.objects.filter(sp_id=sp_id)
	#print (goods)
	return render_to_response("busmaservice.html",{'goods_list':goods})
	


#企业端，服务的退回和修改	
def merge_service_details(request):
	sp_id=1
	if 'sp_id' in request.COOKIES:
		sp_id=request.COOKIES['sp_id']
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
		

#后台管理主页
def b_work_index(request):
    if 'back_id' in request.COOKIES:
	    return render_to_response("b_work_index.html",{})
    else:
        return HttpResponseRedirect('/zzh_back_login/')
            


#客户结算和商家结算
def baforguests(request):
	if 'kind' not in request.COOKIES:
		allba = tb_balist.objects.all()
	else:
		kind = request.COOKIES['kind']
		#print(kind)
		allba = tb_balist.objects.filter(ba_belong=kind)
	lis = []
	flis = []
	for i in allba:
		a_lis = {}
		a_lis['id']=i.ba_id
		a_lis['order_no']=i.order_no
		a_lis['sta']=i.ba_sta
		a_lis['kind']=i.ba_belong
		goodsid = tb_order.objects.get(order_no = i.order_no).goods_id
		a_lis['area']=tb_goods.objects.get(goods_id=goodsid).goods_area
		a_lis['price']=tb_goods.objects.get(goods_id=goodsid).goods_payahead + tb_goods.objects.get(goods_id=goodsid).goods_awardmid +tb_goods.objects.get(goods_id=goodsid).goods_awardafter
		#print (a_lis['price'])
		lis.append(a_lis)
	if 'sta' not in  request.COOKIES:
		flis = lis
	else:
		for i in lis:
			#print(i['sta'])
			a = int(request.COOKIES['sta'])
			if (i['sta']==a):
				#print(123)
				flis.append(i)
	return render_to_response("balforguests.html",{'lis':flis})

def baforshopers(request):
	if 'kind' not in request.COOKIES:
		allba = tb_balist.objects.all()
	else:
		kind = request.COOKIES['kind']
		print(kind)
		allba = tb_balist.objects.filter(ba_belong=kind)
	lis = []
	flis = []
	for i in allba:
		a_lis = {}
		a_lis['id']=i.ba_id
		a_lis['order_no']=i.order_no
		a_lis['sta']=i.ba_sta
		a_lis['kind']=i.ba_belong
		goodsid = tb_order.objects.get(order_no = i.order_no).goods_id
		a_lis['area']=tb_goods.objects.get(goods_id=goodsid).goods_area
		a_lis['price']=tb_goods.objects.get(goods_id=goodsid).goods_payahead + tb_goods.objects.get(goods_id=goodsid).goods_awardmid +tb_goods.objects.get(goods_id=goodsid).goods_awardafter
		#print (a_lis['price'])
		lis.append(a_lis)
	if 'sta' not in  request.COOKIES:
		flis = lis
	else:
		for i in lis:
			#print(i['sta'])
			a = int(request.COOKIES['sta'])
			if (i['sta']==a):
				#print(123)
				flis.append(i)
	return render_to_response("balforshopers.html",{'lis':flis})

def bw_badetail(request):
	ba_id = request.GET.get('id')
	ba = tb_balist.objects.get(ba_id=ba_id)
	res = {}
	res['order_no'] = ba.order_no
	res['kind'] = ba.ba_belong
	goodsid = tb_order.objects.get(order_no = ba.order_no).goods_id
	guestid = tb_order.objects.get(order_no = ba.order_no).buyer_id
	res['name'] = tb_goods.objects.get(goods_id=goodsid).goods_name
	res['price'] = tb_goods.objects.get(goods_id=goodsid).goods_payahead + tb_goods.objects.get(goods_id=goodsid).goods_awardmid +tb_goods.objects.get(goods_id=goodsid).goods_awardafter
	res['guestname'] = tb_user.objects.get(user_id=guestid).user_name
	res['loc']=tb_user_expand.objects.get(user_id=guestid).company_address
	res['con']=tb_user_expand.objects.get(user_id=guestid).companyUserContactName
	res['otime']=tb_order.objects.get(order_no = ba.order_no).add_time
	res['ctime']=tb_order.objects.get(order_no = ba.order_no).final_time
	res['sta']=ba.ba_sta
	res['ftime']=ba.ba_time
	return render_to_response("badetail.html",{'res':res})

def bw_badetailfs(request):
	ba_id = request.GET.get('id')
	ba = tb_balist.objects.get(ba_id=ba_id)
	res = {}
	res['order_no'] = ba.order_no
	res['kind'] = ba.ba_belong
	goodsid = tb_order.objects.get(order_no = ba.order_no).goods_id
	guestid = tb_order.objects.get(order_no = ba.order_no).buyer_id
	res['name'] = tb_goods.objects.get(goods_id=goodsid).goods_name
	res['price'] = tb_goods.objects.get(goods_id=goodsid).goods_payahead + tb_goods.objects.get(goods_id=goodsid).goods_awardmid +tb_goods.objects.get(goods_id=goodsid).goods_awardafter
	res['loc']=tb_user_expand.objects.get(user_id=guestid).company_address
	shopid = tb_order.objects.get(order_no = ba.order_no).sp_id
	res['sname']=tb_service_provider.objects.get(sp_id=shopid).sp_name
	res['sloc']=tb_service_provider.objects.get(sp_id=shopid).sp_address
	res['con']=tb_service_provider.objects.get(sp_id=shopid).tel
	#res['otime']=tb_order.objects.get(order_no = ba.order_no).add_time
	res['fctime']=ba.ba_ftime
	res['sta']=ba.ba_sta
	res['ftime']=ba.ba_time

	return render_to_response("badetailfs.html",{'res':res})
	

def b_work_maguests(request):
	#if 'obc' in request.COOKIES:
	a_t_orders=tb_order.objects.filter(order_state__range=(2,3))
	adds=[]
	
	forsave=[]
	#取出order表里所有的用户名字
	for i in a_t_orders:
		if i.buyer_name not in adds:
			adds.append(i.buyer_name)
	#print adds
	for a in adds:
		#@print a
		mid={}
		order = tb_order.objects.filter(buyer_name=a)
		mid['name']=a
		mid['count']=len(order)
		atmoney=0
		#mid['money']=sum(i.)
		#print len(order)
		for b in order:
			c=tb_goods.objects.get(goods_id=b.goods_id)
			atmoney+=c.goods_payahead+c.goods_awardafter
			#print atmoney
		mid['trade']=atmoney
		mid['id']=tb_order.objects.filter(buyer_name=a)[0].buyer_id
		#print mid['id']
		guest=tb_user_expand.objects.get(user_id=mid['id'])
		mid['loc']=guest.company_address
		mid['contact']=guest.companyUserContactName
		mid['tel']=guest.company_tel
		forsave.append(mid)
	#print (forsave)
	if 'obm' in request.COOKIES:
		forsave.sort(key=lambda x:x['trade'],reverse=True)
		#response.delete_cookie("obm")
	if 'obc' in request.COOKIES:
		forsave.sort(key=lambda x:x['count'],reverse=True)
		#response.delete_cookie("obc")
	return render_to_response("b_work_maguests.html",{'lis':forsave})
			
	#b_work_maguests	

def bw_orderfromguest(request):
	gid =request.GET.get('id')
	name = tb_user.objects.get(expand_id=gid).user_name
	order = tb_order.objects.filter(buyer_id=gid)
	return render_to_response("b_work_guestorderlist.html",{'lis':order,'name':name})

def bw_orderdetail(request):
	oid =request.GET.get('id')
	#print (oid)
	order = tb_order.objects.get(order_id=oid)
	res={}
	res['buyername']=order.buyer_name
	bid = order.buyer_id
	buyer=tb_user_expand.objects.get(user_id=bid)
	res['buyerloc']=buyer.company_address
	res['buyercontact']=buyer.companyUserContactName
	res['buyertel']=buyer.company_tel
	spid=order.sp_id
	sp=tb_service_provider.objects.get(sp_id=spid)
	res['spname']=sp.sp_name
	res['spcon']=sp.con_name
	res['sploc']=sp.sp_address
	res['orderid']=order.order_no
	itemid=order.item_id
	goodsid=order.goods_id
	item=tb_item.objects.get(item_id=itemid)
	goods=tb_goods.objects.get(goods_id=goodsid)
	res['sertype']=item.item_about
	res['sername']=goods.goods_name
	res['serid']=goodsid
	res['serprice']=goods.goods_payahead+goods.goods_awardafter
	res['ordertime']=order.add_time
	res['per']=order.finish_percentage
	return render_to_response("bw_orderdetail.html",{'res':res})

def servicemanagement(request):
	#res = tb_goods_wfc.objects.all()
	return render_to_response("bw_servicemanagement.html",{})

def uncservicemanagement(request):
	res = tb_goods_wfc.objects.all()
	return render_to_response("bw_csman.html",{'res':res})

def cservicemanagement(request):
	checked='1'
	res = tb_goods.objects.all()
	return render_to_response("bw_csman.html",{'res':res,'checked':checked})

def managedetail(request):
	sid = request.GET.get("id")
	res=tb_goods.objects.get(goods_id = sid)
	return render_to_response("managedetail.html",{'goods':res})

def checkservice(request):
	sid = request.GET.get("id")
	#print (sid)
	res = tb_goods_wfc.objects.get(goods_id = sid)
	return render_to_response("checkservice.html",{'goods':res})

def delwfc(request):
	sid = request.GET.get("id")
	i=tb_goods_wfc.objects.get(goods_id = sid)
	i.fea="请返回修改"
	i.save()
	return HttpResponseRedirect('/b_work_index/')

def delg(request):
	sid = request.GET.get("id")
	#print (sid)
	tb_goods.objects.get(goods_id = sid).delete()
	return HttpResponseRedirect('/b_work_index/')

def passwfc(request):
	sid = request.GET.get("id")
	i=tb_goods_wfc.objects.get(goods_id = sid)
	add = tb_goods()
	add.item_id =i.item_id
	add.goods_name=i.goods_name
	add.sp_id=i.sp_id
	add.goods_payahead=i.goods_payahead
	add.awardafter=i.goods_awardafter
	add.awardmid=i.goods_awardmid
	add.goods_market_price=i.goods_payahead
	add.goods_price=i.goods_payahead
	add.goods_price_discouint=i.goods_payahead
	add.goods_pay=1
	add.goods_guarantee=i.cont
	add.goods_sort=0
	add.goods_fanli=i.goods_fanli
	add.steps=i.steps
	add.smod =i.smod 
	add.exa=i.exa
	add.cont=i.cont
	add.goods_commend=1
	add.goods_evaluation_good_star=0
	add.goods_evaluation_count=0
	add.goods_show=1
	add.goods_status=1
	add.save()
	i.delete()
	return HttpResponseRedirect('/b_work_index/')

def custpicforshow(request):
	return render_to_response("custpicforshow.html",{})


def pauses(request):
	sid = request.GET.get("id")
	i =tb_goods.objects.get(goods_id = sid)
	i.goods_status=0
	i.save()
	return HttpResponseRedirect('/b_work_index/')

def starts(request):
	sid = request.GET.get("id")
	i =tb_goods.objects.get(goods_id = sid)
	i.goods_status=1
	i.save()
	return HttpResponseRedirect('/b_work_index/')

def pub_support(request):
	sp_id=1
	'''if 'sp_id' not in request.COOKIES:
		#sp_id=request.COOKIES['user_id']
		return HttpResponseRedirect('/merchant')'''
	if 'sp_id' in request.COOKIES:
		sp_id=request.COOKIES['sp_id']
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
	#return HttpResponse("morning")


def mana_support(request):
	sp_id=1
	'''if request.COOKIES['sp_id'] is None:
		#sp_id=request.COOKIES['user_id']
		print 111
		return HttpResponseRedirect('/merchant')
	
	'''
	#if sp_id in request.COOKIES:
	sp_id=request.COOKIES['sp_id']
	print (request.COOKIES['sp_id'])
	goods = tb_goods.objects.filter(sp_id=sp_id)
	return render_to_response("busmaservice.html",{'goods_list':goods,})
	#return HttpResponse("byebye")

def support_info_main(request):

    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
	print sp_id
        sp = tb_service_provider.objects.get(sp_id = sp_id)
	print sp
        all_area = sp_inservice_area.objects.filter(sp_id=sp_id)
        if 'flag' in request.GET:

            chargeman_name = request.GET['chargeman_name']
            chargeman_number = request.GET['chargeman_number']
            chargeman_email = request.GET['chargeman_email']
            con_email = request.GET['con_email']
            con_name = request.GET['con_name']
            con_number = request.GET['con_number']
            short_intro = request.GET['short_intro']

            temp_sp = tb_service_provider.objects.get(sp_id = sp_id)
            temp_sp.chargeman_name = chargeman_name
            temp_sp.chargeman_number = chargeman_number
            temp_sp.chargeman_email = chargeman_email
            temp_sp.con_name = con_name
            temp_sp.con_number = con_number
            temp_sp.con_email = con_email
            temp_sp.short_intro = short_intro
            temp_sp.save()

            return render(request,'yz_templates/info_main.html',{'sp':sp,'all_area':all_area})
        else:
            return render(request,'yz_templates/info_main.html',{'sp':sp,'all_area':all_area})
    else:
        #return HttpResponse('herer')
        return HttpResponseRedirect('/merchant/')


