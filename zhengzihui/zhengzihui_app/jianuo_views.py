# coding=utf-8

from views import *


def applyforjoin(request):
    add = []
    sp_type = ""

    if request.method == 'POST':
        flag = request.POST.get("flag")
        myflag = str(flag)
        # print myflag
        sp_name = request.POST.get("sp_name")
        con_name = request.POST.get("con_name")
        tel = request.POST.get("tel")
        email = request.POST.get("email")
        sp_type1 = request.POST.get("sp_type1", "")
        sp_type2 = request.POST.get("sp_type2", "")
        sp_type3 = request.POST.get("sp_type3", "")
        if myflag == "1":
            sp_type = sp_type1
        if myflag == "2":
            sp_type = sp_type1 + "+" + sp_type2
        if myflag == "3":
            sp_type = sp_type1 + "+" + sp_type3

        print sp_type

        add = tb_service_provider()

        add.tel = request.POST.get("tel")
        add.email = request.POST.get("email")
        add.sp_name = request.POST.get("sp_name")
        add.con_name = request.POST.get("con_name")
        add.sp_type = sp_type
        # add by yz



        sp_code = random.randint(0, 1000000)
        while (len(tb_service_provider.objects.filter(sp_code=sp_code)) == 1):
            sp_code = random.randint(0, 1000000)
        add.sp_code = sp_code
        add.psw = '000000'

        add.sp_auth = 0  # 默认值\
        add.master = '000'  # 默认值\
        add.sp_image1 = '000'
        add.sp_image2 = '000'
        add.sp_grade = 00  # 默认值\
        add.sp_sort = 00  # 默认值
        add.area_id = '00'
        add.Register_cap = 00
        add.staff_number = 00
        add.Annual_totals = 00
        add.organization_name = '00'
        add.organization_id = 00
        add.organization_assets = 00
        add.organization_profile = '000'
        add.is_recommend = 0

        add.save()
        return render_to_response("success.html", {})
    return render_to_response("applyforjoin.html", {})


def success(request):
    return render_to_response("success.html", {})


def bus_project_management(request):
    if 'sp_id' in request.COOKIES:

        sp_id = request.COOKIES['sp_id']
    else:

        sp_id = 1
    a_click_items = []
    click_items = tb_item_click.objects.order_by('-click_counter')[:4]
    for click_item in click_items:
        a_click_item = {}
        a_click_item['id'] = click_item.item_id  # 获取项目id
        a_click_item['item_code'] = tb_item.objects.get(item_id=click_item.item_id).item_code  # 获取项目编号
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
        a_click_item['item_url'] = tb_item.objects.get(item_id=click_item.item_id).item_url  # 获取原文链接
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

    return render_to_response("bus_project_management.html", {'a_click_items': a_click_items})


# 项目管理详情 by jianuo
def bpm_details(request):
    bpm_id = request.GET['id']
    a_click_items = []
    a_shoucang_items = []
    a_shoucang_goods = []
    a_fuwus = []
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    items = tb_item.objects.get(item_id=bpm_id)  # item表
    item_pa_id = items.item_pa_id
    item_pa = tb_item_pa.objects.get(ipa_id=item_pa_id)  # item_pa表
    s_lists = tb_shoucang_item.objects.filter(item_id=bpm_id)  # 客户收藏
    sb_lists = tb_shoucang_goods.objects.filter(goods_id=bpm_id)  # 客户申报
    fw_lists = tb_goods.objects.filter(item_id=bpm_id)  # 提供服务
    shoucang_items = tb_shoucang_item.objects.filter(item_id=bpm_id)[:4]
    for shoucang_item in shoucang_items:
        a_shoucang_item = {}
        a_shoucang_item['user_name'] = tb_user.objects.get(user_id=shoucang_item.user_id).user_name
        a_shoucang_item['company_address'] = tb_user_expand.objects.get(user_id=shoucang_item.user_id).company_address
        a_shoucang_item['companyUserContactName'] = tb_user_expand.objects.get(
            user_id=shoucang_item.user_id).companyUserContactName
        a_shoucang_item['companyUserPhone'] = tb_user_expand.objects.get(user_id=shoucang_item.user_id).companyUserPhone
        a_shoucang_items.append(a_shoucang_item)
    shoucang_goods = tb_shoucang_goods.objects.filter(goods_id=bpm_id)[:4]
    for shoucang_good in shoucang_goods:
        a_shoucang_good = {}
        a_shoucang_good['user_name'] = tb_user.objects.get(user_id=shoucang_good.user_id).user_name
        a_shoucang_good['company_address'] = tb_user_expand.objects.get(user_id=shoucang_good.user_id).company_address
        a_shoucang_good['companyUserContactName'] = tb_user_expand.objects.get(
            user_id=shoucang_good.user_id).companyUserContactName
        a_shoucang_good['companyUserPhone'] = tb_user_expand.objects.get(user_id=shoucang_good.user_id).companyUserPhone
        a_shoucang_goods.append(a_shoucang_good)
    fuwus = tb_goods.objects.filter(item_id=bpm_id)[:4]
    for fuwu in fuwus:
        a_fuwu = {}
        sps = tb_service_provider.objects.get(sp_id=fuwu.sp_id)
        sp_sp_id = sps.sp_id
        a_fuwu['sp_name'] = tb_service_provider.objects.get(sp_id=sp_sp_id).sp_name
        a_fuwu['area_id'] = tb_service_provider.objects.get(sp_id=sp_sp_id).area_id
        a_fuwu['con_name'] = tb_service_provider.objects.get(sp_id=sp_sp_id).con_name
        a_fuwu['tel'] = tb_service_provider.objects.get(sp_id=sp_sp_id).tel
        a_fuwus.append(a_fuwu)
    return render_to_response("bpm_details.html", {'items': items, 'size': len(s_lists), 'size1': len(sb_lists),
                                                   'a_shoucang_items': a_shoucang_items,
                                                   'a_shoucang_goods': a_shoucang_goods, 'a_fuwus': a_fuwus,
                                                   'item_pa': item_pa, 'size2': len(fw_lists)})


# 后台首页 by jianuo
def zzh_back_index(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    # 订单管理
    all_order = get_all_order_of_sp(sp_id)

    yiquxiao_order = []
    weizhifu_order = []
    yifukuan_order = []
    yixiadan_order = []
    yiwancheng_order = []

    for order in all_order:
        if order.order_state == 0:
            yiquxiao_order.append(order)
        elif order.order_state == 1:
            weizhifu_order.append(order)
        elif order.order_state == 2:
            yifukuan_order.append(order)
        elif order.order_state == 3:
            yixiadan_order.append(order)
        elif order.order_state == 4:
            yiwancheng_order.append(order)
        else:
            pass

    all_wfto_num = len(yiquxiao_order)
    all_dsh_num = len(weizhifu_order)
    all_clz_num = len(yifukuan_order)
    all_ywc_num = len(yixiadan_order)
    all_yi_num = len(yiwancheng_order)
    order_num_info = []
    order_num_info.append(all_wfto_num)
    order_num_info.append(all_dsh_num)
    order_num_info.append(all_ywc_num)
    order_num_info.append(all_clz_num)
    order_num_info.append(all_yi_num)

    # 客户结算
    allba = tb_balist.objects.all()

    kehuyixiadan_ba = []
    kequeren_ba = []
    kwancheng_ba = []

    for ba in allba:
        if ba.ba_sta == 0:
            kehuyixiadan_ba.append(ba)
        elif ba.ba_sta == 1:
            kequeren_ba.append(ba)
        elif ba.ba_sta == 3:
            kwancheng_ba.append(ba)
        else:
            pass

    all_wfto_banum = len(kehuyixiadan_ba)
    all_dsh_banum = len(kequeren_ba)
    all_clz_banum = len(kwancheng_ba)

    ba_num_info = []
    ba_num_info.append(all_wfto_banum)
    ba_num_info.append(all_dsh_banum)
    ba_num_info.append(all_clz_banum)

    # 商家结算
    allaba = tb_balist.objects.all()

    shangqueren_ba = []
    swancheng_ba = []

    for sba in allaba:
        if sba.ba_sta == 2:
            shangqueren_ba.append(sba)
        elif sba.ba_sta == 3:
            swancheng_ba.append(sba)
        else:
            pass

    all_sj_banum = len(shangqueren_ba)
    all_wc_banum = len(swancheng_ba)

    sh_num_info = []
    sh_num_info.append(all_sj_banum)
    sh_num_info.append(all_wc_banum)

    # 推送管理
    all_pushs = push_info.objects.all()
    items=tb_item.objects.all()
    push_items=[]
    for push in all_pushs:
        temp = tb_item.objects.get(item_id=push.push_item_id)
        push_items.append(temp)
    all_push_num=len(push_items)
    notpush_num=len(items)-all_push_num


    # 点评管理
    comment_list = tb_goods_evaluation.objects.all()
    eping_comment = []
    zhengchang_comment = []
    qitaping_comment = []

    for comment in comment_list:
        if comment.goev_status == 0:
            eping_comment.append(comment)
        elif comment.goev_status == 1:
            zhengchang_comment.append(comment)
        elif comment.goev_status == 2:
            qitaping_comment.append(comment)
        else:
            pass

    all_wfto_commentnum = len(eping_comment)
    all_dsh_commentnum = len(zhengchang_comment)
    all_clz_commentnum = len(qitaping_comment)

    comment_num_info = []
    comment_num_info.append(all_wfto_commentnum)
    comment_num_info.append(all_dsh_commentnum)
    comment_num_info.append(all_clz_commentnum)
    # 项目管理
    items = tb_item.objects.all()
    zhengchang_item = []
    jiezhi_item = []
    youwu_item = []

    for item in items:
        if item.item_status == 0:
            zhengchang_item.append(item)
        elif item.item_status == 1:
            jiezhi_item.append(item)
        elif item.item_status == 2:
            youwu_item.append(item)
        else:
            pass

    all_wfto_itemnum = len(zhengchang_item)
    all_dsh_itemnum = len(jiezhi_item)
    all_clz_itemnum = len(youwu_item)

    item_num_info = []
    item_num_info.append(all_wfto_itemnum)
    item_num_info.append(all_dsh_itemnum)
    item_num_info.append(all_clz_itemnum)

    # 产品管理
    # 客户管理
    users = tb_user.objects.all()
    tongguo_user = []
    wei_user = []
    for user in users:
        if user.user_auth == 0:
            wei_user.append(user)
        elif user.user_auth == 1:
            tongguo_user.append(user)
        else:
            pass
    all_tong_num = len(tongguo_user)
    all_wei_num = len(wei_user)
    user_num_info = []
    user_num_info.append(all_tong_num)
    user_num_info.append(all_wei_num)
    # 商家管理
    mers=tb_service_provider.objects.all()
    mtongguo = []
    weitongguo = []
    dengdai = []
    jinxing = []


    for mer in mers:
        if mer.sp_auth == 0:
            mtongguo.append(mer)
        elif mer.sp_auth == 1:
            weitongguo.append(mer)
        elif mer.sp_auth == 2:
            dengdai.append(mer)
        elif mer.sp_auth == 3:
            jinxing.append(mer)
        else:
            pass

    all_wfto_num = len(mtongguo)
    all_dsh_num = len(weitongguo)
    all_clz_num = len(dengdai)
    all_ywc_num = len(jinxing)

    mer_num_info = []
    mer_num_info.append(all_wfto_num)
    mer_num_info.append(all_dsh_num)
    mer_num_info.append(all_clz_num)
    mer_num_info.append(all_ywc_num)

    # 客服人员管理
    back_users=tb_back_user.objects.filter(user_type=2)
    yijihuo_back_user =[]
    weijihuo_back_user =[]
    for back_user in back_users:
        if back_user.user_auth ==1:
            yijihuo_back_user.append(back_user)
        elif back_user.user_auth == 0:
            weijihuo_back_user.append(back_user)
        else:
            pass
    all_jihuo_num=len(yijihuo_back_user)
    all_wei_num=len(weijihuo_back_user)
    back_user_num_info=[]
    back_user_num_info.append(all_jihuo_num)
    back_user_num_info.append(all_wei_num)
    # 审核人员管理
    check_users=tb_back_user.objects.filter(user_type=1)
    yijihuo_check_user=[]
    weijihuo_check_user=[]
    for check_user in check_users:
        if check_user.user_auth==1:
            yijihuo_check_user.append(check_user)
        elif check_user.user_auth==0:
            weijihuo_check_user.append(check_user)
        else:
            pass
    all_cjihuo_num=len(yijihuo_check_user)
    all_cweijihuo_num=len(weijihuo_check_user)
    check_user_num_info=[]
    check_user_num_info.append(all_cjihuo_num)
    check_user_num_info.append(all_cweijihuo_num)
    content = {'yiquxiao_order': yiquxiao_order, 'order_num_info': order_num_info, 'kehuyixiadan_ba': kehuyixiadan_ba,
               'ba_num_info': ba_num_info,

               'shangqueren_ba': shangqueren_ba, 'sh_num_info': sh_num_info, 'eping_comment': eping_comment,
               'comment_num_info': comment_num_info, 'zhengchang_item': zhengchang_item, 'item_num_info': item_num_info,
               'user_num_info': user_num_info,'back_user_num_info':back_user_num_info,"mtongguo":mtongguo,"mer_num_info"
               :mer_num_info,"yijihuo_check_user":yijihuo_check_user,"check_user_num_info":check_user_num_info,"all_push_num"
               :all_push_num,"notpush_num":notpush_num}
    return render_to_response("zzh_back_index.html", content)

