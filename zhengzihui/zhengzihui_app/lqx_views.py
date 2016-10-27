#coding=utf-8

from views import *
from django.http import JsonResponse
#lqx
#商家中心
def merchant_center(request):
    #request.session['user_id'] = 3#此处设置了个session值用来测试，等登录模块完成之后再修改
    sp = []
    if 'sp_id' in request.COOKIES:
        sp_id = int(request.COOKIES['sp_id'])
        sp = tb_service_provider.objects.get(sp_id=sp_id)
    else:
        return HttpResponse("请先登录账号;请返回到上级页面登录或者注册")

    return render(request,'shenbaohezuo.html',{'sp':sp,})

    
    #保存登录商家修改信息
def modify_merchant(request):
    sp = []
    sp_expand = []
    if request.COOKIES['sp_id']:
        sp_id = int(request.COOKIES['sp_id'])
        sp = tb_service_provider.objects.get(sp_id=sp_id)
    sp.sp_name = request.POST['name']
    sp.sp_email = request.POST['email']
    sp.sp_password = request.POST['password']
    sp.sp_telephone = request.POST['phonenumber']
    sptype = int(request.POST['sptype'])
    sp.sp_type = request.POST['sp_type']
    

    return HttpResponseRedirect('/zzh/merchant_center')

#未认证的商家能登录吗？？？？？YZ
def merchant(request):
    errors= []  
    sp_name=None  
    password=None
    sp = tb_service_provider()
    if 'sp_id' in request.COOKIES:
        sp_id = int(request.COOKIES['sp_id'])
        sp_type = tb_service_provider.objects.get(sp_id =sp_id).sp_type
        if '配套服务'in sp_type :

            response = render(request,'support_merchant.html',{})
        elif '项目申报' in sp_type:
            response = render(request,'bus_index.html',{})
        else:
            response = render(request,'financing_merchant.html',{})
        return response
        
    if request.method == 'POST' :  
        if not request.POST.get('_spname'):  
            errors.append('请输入用户名')  
        else:
            sp_name = request.POST.get('_spname')  
        if not request.POST.get('password'):  
            errors.append('请输入登陆密码')  
        else:  
            password= request.POST.get('password')  
        if sp_name is not None and password is not None:
            try:
                sp = tb_service_provider.objects.get(sp_name = sp_name)
            except tb_service_provider.DoesNotExist:
                errors.append('用户名不存在')
            
            	return render_to_response('merchant.html', {'errors': errors})
            if password == sp.psw:
                sp_type1=request.POST.get('sp_type1')
                #ms:print "testing..."
                #print sp_type
                response = HttpResponse()
                if sp_type1=="2" and ('配套服务'in sp.sp_type) :
                  if sp.sp_auth == 1:
                    response =  render(request,"support_merchant.html")
                  else:
                        return HttpResponse('请等待政资汇对您的认证！')
                elif sp_type1=="2" and ('配套服务'not in sp.sp_type):
                  return HttpResponse("您不是配套服务提供商！")
                if sp_type1=="3" and ('融资'in sp.sp_type) :
                  if sp.sp_auth == 1:
                    response = render(request,"financing_merchant.html")
                  else:
                        return HttpResponse('请等待政资汇对您的认证！')
                elif sp_type1=="3" and ('融资'not in sp.sp_type):
                  return HttpResponse("您不是融资服务提供商！")
                if sp_type1=='1'and (sp.sp_type=='项目申报' ) :
                    if sp.sp_auth == 1:
                        response = HttpResponseRedirect('/busindex/')#render(request,'bus_index.html',{})#HttpResponseRedirect('/busindex/')
                    else:
                        return HttpResponse('请等待政资汇对您的认证！')
                elif sp_type1=="1" and (sp.sp_type!='项目申报' ):
                    return HttpResponse("您不是申报服务提供商！")
                response.set_cookie('sp_name',sp_name,3600)
                response.set_cookie('sp_id',sp.sp_id,3600)
                #print(user.expand.company_name)
                return response
            else:
                errors.append('密码错误')
    return render_to_response('merchant.html', {'errors': errors})    
###商家退出
def merchantout(request):
        response = HttpResponseRedirect('/index/')
        response.delete_cookie('sp_name')
        response.delete_cookie('sp_id')
        return response    
        
        
##qiu
def all_orders_back(request):
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
        a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name#获取项目名字
        a_click_item['item_ga'] = tb_item.objects.get(item_id=click_item.item_id).item_ga#获取项目资助金额
        album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
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
    recommend_items = tb_item.objects.filter(is_recommend=1).order_by('-item_id')[:15]#获取推荐的前15的项目
    for recommend_item in recommend_items:
        a_recommend_item= {}
        a_recommend_item['id'] = recommend_item.item_id#获取项目id
        a_recommend_item['name'] = recommend_item.item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=recommend_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_recommend_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_recommend_items.append(a_recommend_item)
    
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['order_no'] = order.order_no#获取订单编号
        a_order['goods_id'] = order.goods_id#获取商品id     
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        a_order['add_time'] = order.add_time#获取起始时间
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
    return render(request,'order_back.html',{'user':user,'a_click_items':a_click_items,'a_recommend_items':a_recommend_items,'a_order_list':a_order_list})
    
def get_all_order_of_sp(sp_id):
    if not sp_id:
        return '请输入服务商id'
    # 获取该商家获得的所有订单
    all_order = tb_order.objects.filter(sp_id=sp_id)
    # 为每个订单添加一个服务名称的属性
    for order in all_order:
        # print order.goods_id
        temp_order = tb_goods.objects.get(goods_id=order.goods_id)
        temp_buyer = tb_user.objects.get(user_id=order.buyer_id)
        temp_sptype = tb_service_provider.objects.get(sp_id=order.sp_id).sp_type  ##服务类型
        # print temp_sptype
        if temp_buyer.expand_id:

            temp_buyer_expand = tb_user_expand.objects.get(user_id=order.buyer_id)
            buyer_expand_address = temp_buyer_expand.company_address
            # print buyer_expand_address

            if buyer_expand_address == '':
                buyer_expand_address == '该用户所在公司还未完善地址信息 '
            buyer_expand_contact = temp_buyer_expand.companyUserContactName
            if buyer_expand_contact == '':
                buyer_expand_contact = '该用户所在公司还未指定联系人'
        else:
            buyer_expand_address = "用户还未填写,请电话联系"
            buyer_expand_contact = temp_buyer.user_name
        goods_name = temp_order.goods_name
        goods_area = temp_order.goods_area

        # 添加的三个属性
        order.goods_name = goods_name
        order.goods_area = goods_area
        order.buyer_expand_address = str(buyer_expand_address)
        order.buyer_expand_contact = str(buyer_expand_contact)
        order.sptype = str(temp_sptype)
    return all_order


# 订单管理-查看详情  lqx
def bw_order_manage_detail(request):
    order_no = request.GET['id']
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    all_order = tb_order.objects.filter(sp_id=sp_id, order_no=order_no)  # 查看订单根据订单编号显示
    merchant = tb_service_provider.objects.filter(sp_id=sp_id)  # 查看订单商家

    for order in all_order:

        # print order.goods_id
        temp_order = tb_goods.objects.get(goods_id=order.goods_id)
        temp_buyer = tb_user.objects.get(user_id=order.buyer_id)
        temp_sptype = tb_service_provider.objects.get(sp_id=order.sp_id).sp_type  ##服务类型
        temp_stime = tb_balist.objects.get(order_no=order.order_no).ba_time
        # print temp_stime
        temp_ftime = tb_balist.objects.get(order_no=order.order_no).ba_ftime
        if temp_buyer.expand_id:

            temp_buyer_expand = tb_user_expand.objects.get(user_id=order.buyer_id)
            buyer_expand_address = temp_buyer_expand.company_address
            buyer_expand_tel = temp_buyer_expand.company_tel
            # print buyer_expand_address

            if buyer_expand_address == '':
                buyer_expand_address == '该用户所在公司还未完善地址信息 '
            buyer_expand_contact = temp_buyer_expand.companyUserContactName
            if buyer_expand_contact == '':
                buyer_expand_contact = '该用户所在公司还未指定联系人'
        else:
            buyer_expand_address = "用户还未填写,请电话联系"
            buyer_expand_contact = temp_buyer.user_name
        goods_name = temp_order.goods_name
        goods_code = temp_order.goods_code
        goods_pay = temp_order.goods_pay
        if order.efile_send:
            order.str_efile_send = '已经交付'
        else:
            order.str_efile_send = '未交付'
        if order.paper_send:
            order.str_paper_send = '已经送达'
        else:
            order.str_paper_send = '未送达'
        # 添加的三个属性
        order.goods_name = goods_name
        order.goods_code = goods_code  # 服务产品编号
        order.goods_pay = goods_pay  # 服务价格
        order.buyer_expand_address = str(buyer_expand_address)
        order.buyer_expand_contact = str(buyer_expand_contact)
        order.buyer_expand_tel = str(buyer_expand_tel)
        order.sptype = temp_sptype
        order.stime = temp_stime  # 商家交单时间
        order.ftime = temp_ftime  # 平台交单时间
        order.s_type = str(order.sptype)

    return render(request, "bw_order_manage_detail.html",
                  {'all_order': all_order, 'sp_id': sp_id, 'merchant': merchant})


def balfororders(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    all_order = get_all_order_of_sp(sp_id)
    filter_order=[]

    sp_type=request.GET.get('sp_type')
    sp_type1=None
    sp_type2=None
    sp_type3=None
    if sp_type=="项目申报":
        sp_type1=True
        
        #all_order=all_order[:3]
        
    elif sp_type=="配套服务":
        sp_type2=True
        #all_order=all_order[:2]
    else:
        sp_type3=True
        #all_order=all_order[:3]
    
    
    for order in all_order:

        if order.efile_send :
            order.str_efile_send = '已经交付'
        else:
            order.str_efile_send = '未交付'
        if order.paper_send:
            order.str_paper_send = '已经送达'
        else:
            order.str_paper_send = '未送达'

        order.s_type=str(order.sptype)
        
    #print sp_type
    order = []
    if sp_type=='项目申报':
        for order in all_order:
           print order.sptype
           if order.sptype=='项目申报':
              filter_order.append(order)
      
    print len(filter_order)
    
    return render(request,"balfororders.html",{'all_order':filter_order,'sp_id':sp_id,"sp_type1":sp_type1,"sp_type2":sp_type2,"sp_type3":sp_type3,"sp_type":sp_type,})
#lqx订单管理
def sort_order_time(request):
	if 'sp_id' in request.COOKIES:
		sp_id = request.COOKIES['sp_id']
	else:
		sp_id = 1
	#all_order = get_all_order_of_sp(sp_id)
	all_order = tb_order.objects.filter(sp_id=sp_id).order_by('-finish_percentage')

	for order in all_order:
		temp_order = tb_goods.objects.get(goods_id=order.goods_id)
		temp_sptype = tb_service_provider.objects.get(sp_id=order.sp_id).sp_type  ##服务类型
		order.sptype = temp_sptype
		goods_name = temp_order.goods_name
		goods_area = temp_order.goods_area
		# 添加地域和服务名城
		order.goods_name = goods_name
		order.goods_area = goods_area
		##lqx判断服务类型
		if order.sptype == '申报服务提供商':
			order.s_type = '项目申报'
		elif order.sptype == '项目申报配套服务':
			order.s_type = '配套服务'
		else:
			order.s_type = '融资服务'
		order.s_type = str(order.s_type)

	# print sp_type
	return render(request, "balfororders.html", {'all_order': all_order, 'sp_id': sp_id})

##商家管理lqx
def baformerchant(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    merchant = tb_service_provider.objects.all() # 查看订单商家
    adds = []
    forsave=[]
    for i in merchant:
        if i.sp_id not in adds:
            adds.append(i.sp_id)
    for a in adds:
        mid = {}
        order = tb_order.objects.filter(sp_id=a)
        mer=tb_service_provider.objects.get(sp_id=a)
        mid['sp_id'] = a
        mid['count'] = len(order)#用于计算订单次数
        mid['sp_name']=mer.sp_name
        mid['area_id']=mer.area_id
        mid['con_name']=mer.con_name
        mid['tel']=mer.tel
        atmoney = 0
        for b in order:
            atmoney += b.order_amount
        print atmoney
        mid['trade'] = atmoney#交易金额
        forsave.append(mid)

    if 'obm' in request.COOKIES:
        forsave.sort(key=lambda x: x['trade'], reverse=True)
    if 'obc' in request.COOKIES:
        forsave.sort(key=lambda x: x['count'], reverse=True)
    return render(request, "balformerchant.html", {'merchant': forsave})
#正在执行
def sjglordering(request):
	gid =request.GET.get('id')
	name = tb_service_provider.objects.get(sp_id=gid).sp_name
	order = tb_order.objects.filter(sp_id=gid)
	return render(request,"sjglordering.html",{'lis':order,'name':name})   
  
#配套商家dingdanguanli
def supporting_orders(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 2
    all_order = get_all_order_of_sp(sp_id)

    for order in all_order:

        if order.efile_send :
            order.str_efile_send = '已经交付'
        else:
            order.str_efile_send = '未交付'
        if order.paper_send:
            order.str_paper_send = '已经送达'
        else:
            order.str_paper_send = '未送达'

    #request.COOKIES['first_page'] = 0
    return render(request,"supporting_orders.html",{'all_order':all_order,'sp_id':sp_id})

def sort_order(request):
    sp_id = request.GET.get('sp_id')
    flag = request.GET.get('flag')
    if flag == '0':
        all_order = tb_order.objects.filter(sp_id=sp_id).order_by('-add_time')
    elif flag == '1':
        all_order = tb_order.objects.filter(sp_id=sp_id).order_by('promise_finish_time')

    else:
        all_order = tb_order.objects.filter(sp_id=sp_id).order_by('-finish_percentage')

    for order in all_order:
        # print order.goods_id
        temp_order = tb_goods.objects.get(goods_id=order.goods_id)
        temp_buyer = tb_user.objects.get(user_id=order.buyer_id)
        if temp_buyer.expand_id:

            temp_buyer_expand = tb_user_expand.objects.get(user_id=order.buyer_id)
            buyer_expand_address = temp_buyer_expand.company_address
            print buyer_expand_address

            if buyer_expand_address == '':
                buyer_expand_address == '该用户所在公司还未完善地址信息 '
            buyer_expand_contact = temp_buyer_expand.companyUserContactName
            if buyer_expand_contact == '':
                buyer_expand_contact = '该用户所在公司还未指定联系人'
        else:
            buyer_expand_address = "用户还未填写,请电话联系"
            buyer_expand_contact = temp_buyer.user_name
        goods_name = temp_order.goods_name
        if order.efile_send:
            order.str_efile_send = '已经交付'
        else:
            order.str_efile_send = '未交付'
        if order.paper_send:
            order.str_paper_send = '已经送达'
        else:
            order.str_paper_send = '未送达'
        # 添加的三个属性
        order.goods_name = goods_name
        order.buyer_expand_address = str(buyer_expand_address)
        order.buyer_expand_contact = str(buyer_expand_contact)
    # request.session['first_page'] = 0
    return render(request, "supporting_orders.html", {'all_order': all_order, 'sp_id': sp_id})
def change_paper_send_state2(request):
    if 'order_id' in request.GET:
        order_id = request.GET.get('order_id')
        temp_order = tb_order.objects.get(order_id=order_id)
        temp_order.paper_send = 1
        temp_order.save()
        # 很冗余的代码，就是为了取订单
        if 'sp_id' in request.COOKIES:
            sp_id = request.COOKIES['sp_id']
        else:
            sp_id = 2
        all_order = get_all_order_of_sp(sp_id)

        for order in all_order:
            # print order.goods_id

            if order.efile_send:
                order.str_efile_send = '已经交付'
            else:
                order.str_efile_send = '未交付'
            if order.paper_send:
                order.str_paper_send = '已经送达'
            else:
                order.str_paper_send = '未送达'
        # request.COOKIES['first_page'] = 0
        return render(request, "supporting_orders.html", {'all_order': all_order})
    else:
        return HttpResponse("没有正确的订单号")

#融资服务
def financing_orders(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 2
    all_order = get_all_order_of_sp(sp_id)

    for order in all_order:

        if order.efile_send :
            order.str_efile_send = '已经交付'
        else:
            order.str_efile_send = '未交付'
        if order.paper_send:
            order.str_paper_send = '已经送达'
        else:
            order.str_paper_send = '未送达'

    #request.COOKIES['first_page'] = 0
    return render(request,"financing_orders.html",{'all_order':all_order,'sp_id':sp_id})
