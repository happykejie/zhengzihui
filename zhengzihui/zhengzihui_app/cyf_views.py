#coding=utf-8
from views import *










# 个人注册by cyf
def g_register(request):
    errors = []
    user_name = None
    user_password = None
    user_password2 = None
    user_telephone = None
    user_email = None
    falg = False
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

            try:
                user = tb_user.objects.get(user_name=user_name)
                errors.append('用户名已存在')
                return render_to_response('g_register.html', {'errors': errors})
            except tb_user.DoesNotExist:
                pass
            add = tb_user()
            add2 = tb_user_expand()
            add.user_name = user_name
            add.user_password = user_password
            add.user_telephone = user_telephone
            add.user_email = user_email
            add.user_auth = 0
            add.expand = None
            add.save()
            user_id = add.user_id
            token = token_confirm.generate_validate_token(user_name)
            print(token)
            message = "\n".join([u'{0},欢迎注册政资汇'.format(user_name), u'请访问该链接，完成用户验证(链接1小时内有效):',
                                 '/'.join(['127.0.0.1:8000', 'register2', token])])
            # message = '/'.join(['127.0.0.1:8000','register2',token])
            send_mail(u'注册用户验证信息', message, 'changyifan123@qq.com', [user_email])

            return render_to_response('register2.html')
    return render_to_response('g_register.html', {'errors': errors})

#登陆
def login(request):
    a_click_items = []
    click_items = tb_item_click.objects.order_by('-click_counter')[:4]
    for click_item in click_items:
        a_click_item = {}
        a_click_item['id'] = click_item.item_id  # 获取项目id
        a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name  # 获取项目名字
        album = \
        tb_album.objects.filter(album_type=0, affiliation_id=click_item.item_id, is_default=1).order_by('-nacl_sort')[
            0]  # 获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[
                                  14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_click_item['item_ga'] = tb_item.objects.get(item_id=click_item.item_id).item_ga  # 获取项目资助金额
        item = tb_item.objects.get(item_id=click_item.item_id)
        item_pa_id = item.item_pa_id
        a_click_item['ipa_name'] = tb_item_pa.objects.get(ipa_id=item_pa_id).ipa_name  # 获取项目管理单位名称

        now_seconds = time.time() - 8 * 60 * 60  # 距离1970的秒数  将东八区转换为0时区
        a_click_item['item_publish'] = tb_item.objects.get(item_id=click_item.item_id).item_publish.strftime(
            '%Y.%m.%d')  # 获取项目开始时间
        a_click_item['item_deadtime'] = tb_item.objects.get(item_id=click_item.item_id).item_deadtime.strftime(
            '%Y.%m.%d')  # 获取项目截止时间
        start_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_publish.timetuple())  # utc 0时区
        end_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_deadtime.timetuple())
        consume_time = (now_seconds - start_seconds) / (end_seconds - start_seconds) * 100
        if consume_time > 100:
            a_click_item['item_consume_time'] = 100
            a_click_item['item_key'] = "已结束"
        else:
            a_click_item['item_consume_time'] = int(consume_time)

        a_click_items.append(a_click_item)
    print "testing..."
    print a_click_items
    errors = []
    user_name = None
    password = None
    user = tb_user()
    if 'user_name' in request.COOKIES:
        response = render_to_response('index.html', {'user_name': request.COOKIES['user_name']})
        return response
    if 'user_id' in request.COOKIES:
        userid = int(request.COOKIES['user_id'])
        user_name_getby_id = tb_user.objects.get(user_id=userid)
        response = render_to_response('index.html', {'user_name': user_name_getby_id})
        return response
    if request.method == 'POST':
        if not request.POST.get('_username'):
            errors.append('请输入用户名')
        else:
            user_name = request.POST.get('_username')
        if not request.POST.get('password'):
            errors.append('请输入登陆密码')
        else:
            password = request.POST.get('password')
        if user_name is not None and password is not None:
            try:
                user = tb_user.objects.get(user_name=user_name)
            except tb_user.DoesNotExist:
                errors.append('用户名不存在')
            if user.user_auth == 0:
                errors.append('请查看邮件完成用户认证')
                return render_to_response('denglu.html', {'errors': errors})
            if password == user.user_password:

                response = render_to_response('index.html',
                                              {'user_name': user.user_name, 'a_click_items': a_click_items})

                response.set_cookie('user_name', user_name)
                response.set_cookie('user_id', user.user_id)
                # print(user.expand.company_name)
                # YZ
                if 'unregist_tobepay_goodsid' in request.COOKIES:
                    goodsid = request.COOKIES['unregist_tobepay_goodsid']
                    responsenotpay = HttpResponseRedirect('/service_list/?itemid=' + str(goodsid))
                    responsenotpay.set_cookie('user_name', user_name)
                    responsenotpay.set_cookie('user_id', user.user_id)
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




def bus_comment_manager(request):
    service_provider = 'cyf'
    comment_list = tb_goods_evaluation.objects.filter(service_provider=service_provider)
   # print(comment_list)
    #print service_provider
    return render_to_response("bus_comment_manager.html", {'comment_list':comment_list})



def service_provider_reply(request):
    if request.GET['id']:
        id = request.GET['id']
        goods = tb_goods_evaluation.objects.get(goods_id=id)
        user_name = goods.user_name
        if request.method == 'POST':
            goods.reply_content = request.POST.get("reply")
            goods.save()
            return HttpResponseRedirect('/busindex',{})
    return render_to_response('service_provider_reply.html', {'user_name':user_name})





def b_work_comment_manager(request):
    if 'area' not in request.COOKIES:
        comment_list = tb_goods_evaluation.objects.all()
    else:
        area = request.COOKIES['area']
        print(area)
        if area == '0':
            comment_list = tb_goods_evaluation.objects.filter(location = '成都')
        else:
            comment_list = tb_goods_evaluation.objects.exclude(location = '成都')
    return render_to_response("b_work_comment_manager.html", {'comment_list': comment_list})



#cyf 后台审核人员管理
def auditor_manager(request):
    return render_to_response('auditor_manager.html',{})

def support_staff_manager(request):
    list1 = []
    list2 = []
    add = tb_back_user()
    if 'kind' not in request.COOKIES:
        pass
    else:
        kind = request.COOKIES['kind']
        #查询
        if kind=='0':
            _name = request.POST.get('name')
            _tel =  request.POST.get('tel')
            if _name and not _tel:
                list1 = tb_back_user.objects.filter(user_name = _name)
            if _tel and not _name:
                list1 = tb_back_user.objects.filter(user_telephone=_tel)
            if _tel and _name:
                list1 = tb_back_user.objects.filter(user_name=_name)
                list2 = tb_back_user.objects.filter(user_telephone=_tel)
                if list1!=list2:
                    return render_to_response("support_staff_manager.html",{'message':'<script type="text/javascript">alert("您输入的姓名电话不匹配，请重新输入或使用单一查询条件！");</script>'})
            if not list1:
                return render_to_response("support_staff_manager.html", {'message': '<script type="text/javascript">alert("查无此人！");</script>'})
            return render_to_response('support_staff_manager.html',{'list':list1})
        else:
            _name = request.POST.get('name')
            _tel = request.POST.get('tel')
            if _name and _tel:
                add.user_name = _name
                add.user_type = 2
                add.user_telephone = _tel
                add.user_password = "123456"
                add.user_auth = 1
                add.save()
                list1 = tb_back_user.objects.filter(user_name=_name)
                return render_to_response('support_staff_manager.html', {'list': list1})
            else:
                return render_to_response("support_staff_manager.html", {'message': '<script type="text/javascript">alert("请将信息填写完整！");</script>'})
    return render_to_response('support_staff_manager.html',{})


#配套中心点评服务
def auxiliary_comment(request):
    return render_to_response("auxiliary_comment.html",{})