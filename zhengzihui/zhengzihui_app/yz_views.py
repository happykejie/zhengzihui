#coding=utf-8

from views import *

'''
用户中心
'''
##############################
# 排序部分
##############################
# By 袁志
# 按资金级别排序，顺序为中央、省级、市级、县级或者反序

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


def getthe_filteditem(request):
    items = []

    a_items = []
    middle_items = []
    tmiddle_items = []

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

    allthebumen = ['经济与信息化', '发展与改革', '财政', '科技', '教育', '文化', '卫计', '体育', '知识产权', '农业', '林业', '畜牧', '渔业', '粮食', '中医药',
                   '国土', '住建', '交通', '水利', '能源', '环保', '商务', '投资促进', '工商', '税务', '民政', '人社', '扶贫', '旅游', '人民银行', '银监',
                   '证监', '保监', '质监', '药监', '安监']
    allthejibie = ['县级财政资金', '市级财政资金', '省级财政资金', '中央财政资金']
    allthezhuangtai = ['截止申报', '正在申报']

    if (selected['jibie'].encode("utf-8") != '全部'):

        jibielist = (selected['jibie'].encode("utf-8")).split(',')

        for i in jibielist:
            middle_items = chain(middle_items,
                                 (tb_item.objects.filter(item_level=(allthejibie.index(i) + 1))))  # 匹配数据库的级别这一栏的数值YZ
        middle_items = list(middle_items)
    else:
        middle_items = tb_item.objects.all()

    if (selected['zhuangtai'].encode("utf-8") != '全部'):

        for i in middle_items:
            print allthezhuangtai.index(selected['zhuangtai'].encode("utf-8"))
            if allthezhuangtai.index(selected['zhuangtai'].encode("utf-8")) == i.item_status:
                tmiddle_items.append(i)
    else:
        tmiddle_items = middle_items

    if (selected['bumen'].encode("utf-8") != '全部'):
        bumenlist = (selected['bumen'].encode("utf-8")).split(',')
        for i in tmiddle_items:
            for j in bumenlist:
                if j in (i.item_about).encode("utf-8"):
                    items.append(i)
    else:

        items = tmiddle_items

    if (len(items) > 10):
        items = items[:10]  # 不够10条报错
    else:
        items = items
    search_content = request.COOKIES['search_content']
    if search_content != request.session['bumen'] and search_content != request.session['jibie'] and search_content != \
            request.session['zhuangtai']:
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

        seg_list = jieba.cut(goodsname, cut_all=False)
        # 搜索
        for gname in seg_list:
            # filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
            ads += tb_item.objects.filter(item_name__contains=gname)
            # 去重复
        for i in ads:
            if i not in items:
                items.append(i)
        filted_item = items

    print len(filted_item)
    items = []
    itemstemp = []
    if (sortbyLevelFlag == True):
        itemstemp = tb_item.objects.order_by('item_level')
        for item in itemstemp:
            if item in filted_item:
                items.append(item)

        global sortbyLevelFlag
        sortbyLevelFlag = False
    else:
        itemstemp = tb_item.objects.order_by('-item_level')
        for item in itemstemp:
            if item in filted_item:
                items.append(item)
        global sortbyLevelFlag
        sortbyLevelFlag = True

    a_items = get_and_set_info(items)
    # 获得热门推荐的项目
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    return render(request, 'search_result.html', {'items': a_items, 'recommend': recommend,})


# 按截至时间 排序存在的问题估计是因为 瀑布流每次只能取得10个所以 当超过10个之后再取的8 个 就出现了 重新排序，但是还是按顺序排列

###服务商排序
sortflag1 = True


def search_result_sort_deadtime(request):
    a_items = []
    items = []
    filted_item = getthe_filteditem(request)

    if len(filted_item) == 0:
        goodsname = ''
        ads = []

        if 'search_content' in request.COOKIES:
            goodsname = request.COOKIES['search_content']

        seg_list = jieba.cut(goodsname, cut_all=False)
        # 搜索
        for gname in seg_list:
            # filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
            ads += tb_item.objects.filter(item_name__contains=gname)
            # 去重复
        for i in ads:
            if i not in items:
                items.append(i)

        filted_item = items
    items = []
    itemstemp = []
    if (sortflag1 == True):
        itemstemp = tb_item.objects.order_by('item_deadtime')
        for item in itemstemp:
            if item in filted_item:
                items.append(item)

        global sortflag1
        sortflag1 = False
    else:
        itemstemp = tb_item.objects.order_by('-item_deadtime')

        for item in itemstemp:
            if item in filted_item:
                items.append(item)
        global sortflag1
        sortflag1 = True

    a_items = get_and_set_info(items)
    # 获得热门推荐的项目
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    return render(request, 'search_result.html', {'items': a_items, 'recommend': recommend,})


# 综合排序 现在仅靠点击率来排序
sortbyComprihensiveFlag = True


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
        seg_list = jieba.cut(goodsname, cut_all=False)
        # 搜索
        for gname in seg_list:
            # filter(someziduan__contains = something) 代表模糊过滤出包含something的所有objectYZ
            ads += tb_item.objects.filter(item_name__contains=gname)
            # 去重复
        for i in ads:
            if i not in items:
                items.append(i)

        filted_item = items
    items = []

    itemstemp = []
    if (sortbyComprihensiveFlag == True):

        itemsinclick = tb_item_click.objects.order_by('-click_counter')

        for thing in itemsinclick:
            willappend = tb_item.objects.get(item_id=thing.item.item_id)
            itemstemp.append(willappend)

        for item in itemstemp:
            if item in filted_item:
                items.append(item)
        global sortbyComprihensiveFlag
        sortbyComprihensiveFlag = False
    else:
        itemsinclick = tb_item_click.objects.order_by('click_counter')
        for thing in itemsinclick:
            willappend = tb_item.objects.get(item_id=thing.item.item_id)
            itemstemp.append(willappend)
        for item in itemstemp:
            if item in filted_item:
                items.append(item)

        global sortbyComprihensiveFlag
        sortbyComprihensiveFlag = True
    a_items = get_and_set_info(items)
    # 获得热门推荐的项目
    recommendtemp = get_the_hotrecommend()
    recommend = get_and_set_info(recommendtemp)
    return render(request, 'search_result.html', {'items': a_items, 'recommend': recommend,})


##############################
# 排序部分结束
##############################
# 项目项目详情加载YZ
def project_detail(request):
    project_detail_item_id = 1  # 取一个默认值
    if request.GET['id']:
        # 能保证取到吗
        project_detail_item_id = request.GET['id']

    addclick = tb_item_click.objects.get(item_id=project_detail_item_id)
    if addclick == None:
        addclick = tb_item_click(itcl_id=0, item_id=project_detail_item_id, click_counter=1)
        addclick.save()
    else:
        addclick.click_counter += 1
        addclick.save()
    item = tb_item.objects.get(item_id=project_detail_item_id)
    item.item_pa_name = (tb_item_pa.objects.get(ipa_id=item.item_pa_id)).ipa_name  # 扩展对象属性，直接填写即可YZ
    item.item_pa_address = (tb_item_pa.objects.get(ipa_id=item.item_pa_id)).ipa_address
    # print item.item_pa_name
    # print item.item_pa_name
    article = tb_article.objects.filter(affiliation_id=project_detail_item_id)

    a_pics = []
    # article2 = article[2]
    if (len(article) == 0):
        # 获取项目起止时间
        gettimeInstance = tb_item.objects.get(item_id=project_detail_item_id)
        # 获得热门推荐的项目
        recommendtemp = get_the_hotrecommend()
        recommend = get_and_set_info(recommendtemp)

        album = tb_album.objects.filter(album_type=0, affiliation_id=project_detail_item_id, is_default=1).order_by(
            '-nacl_sort')[0]  # 获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]  # 获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            # print a_pic
            a_pics.append(a_pic)
        if not a_pics:
            pic_url = '/static/zhengzihui_app/img_for_items/default.jpg'
            a_pics.append(pic_url)

        context = {'item': item, 'article': article, 'a_pics': a_pics, 'recommend': recommend,
                   'gettimeInstance': gettimeInstance,}
        # print item.item_pa_address

        return render(request, 'project_detail.html', context)

    else:

        album = tb_album.objects.filter(album_type=0, affiliation_id=project_detail_item_id, is_default=1).order_by(
            '-nacl_sort')[0]  # 获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]  # 获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            # print a_pic
            a_pics.append(a_pic)

        # 获取项目起止时间
        gettimeInstance = tb_item.objects.get(item_id=project_detail_item_id)

        # 获得热门推荐的项目
        recommendtemp = get_the_hotrecommend()
        recommend = get_and_set_info(recommendtemp)
        print "sdklfsdlflsdkflsdklksdlfksdlfksdkl"
        context = {'item': item, 'article': article[0], 'a_pics': a_pics, 'recommend': recommend,
                   'gettimeInstance': gettimeInstance,}
        return render(request, 'project_detail.html', context)


# 修复从搜索结果界面获得到 item_details/ url的bug,并没有写，但是出现了
def item_details(request):
    if request.GET['id']:
        project_detail_item_id = request.GET['id']

    item = tb_item.objects.get(item_id=project_detail_item_id)

    article = tb_article.objects.filter(affiliation_id=project_detail_item_id)
    article0 = None
    article1 = None
    a_pics = []
    if (len(article) >= 2):
        article0 = article[0]
        article1 = article[1]
    if (len(article) == 1):
        article0 = article[0]
        article1 = None
    if (len(article) == 0):
        pass
    # article2 = article[2]
    if ((article0 == None) and (article1 == None)):

        return render(request, 'project_detail.html',
                      {'item': item, 'article0': article0, 'article1': article1, 'a_pics': a_pics})
    else:

        album = tb_album.objects.filter(album_type=0, affiliation_id=project_detail_item_id, is_default=1).order_by(
            '-nacl_sort')[0]  # 获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0:4]  # 获取前四张图片
        for pic in pics:
            a_pic = pic.pic_object.url[14:]
            a_pics.append(a_pic)

        return render(request, 'project_detail.html',
                      {'item': item, 'article0': article0, 'article1': article1, 'a_pics': a_pics})


# 服务商列表展示 YZ
def service_list(request):
    service = 1
    noservice = 0
    noserviceinfo = "没有指定的服务商"
    id1 = request.GET['itemid']

    # 未完！！
    # 按项目点击率降序获得前最多前三个热门项目
    HotClick = tb_item_click.objects.all()[0:2]
    HotClickDis = HotClick
    # 得到相关的项目
    HotItemDis = []
    a_pics = []
    for hotclick in HotClickDis:
        album = \
        tb_album.objects.filter(album_type=0, affiliation_id=hotclick.item_id, is_default=1).order_by('-nacl_sort')[
            0]  # 获取项目对应的相册id
        album_id = album.album_id
        pics = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0]  # 获取第一张张图片
        a_pic = pics.pic_object.url[14:]
        a_pics.append(a_pic)

    if (id1 == ''):
        service = 0
        noservice = 1
        return render('request', 'goods_list.html', {'service': service, 'noservice': noservice,})
    else:
        # print id1
        id1 = int(id1)
        request.session['for_sort_itemid'] = id1
        tb_goods_list = tb_goods.objects.filter(item_id=id1)
        if len(tb_goods_list):
            service = 1
            noservice = 0
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
                finish_percentage = int((1 - (float(days_remain) / float(days_total))) * 100)
            goods.goods_remaintime = finish_percentage  # 完成百分比为对象添加的属性

        items = tb_item.objects.all()[:3]
        a_items = []
        for item in items:
            a_item = {}
            a_item['item_key'] = item.item_key
            album = \
            tb_album.objects.filter(album_type=0, affiliation_id=item.item_id, is_default=1).order_by('-nacl_sort')[
                0]  # 获取项目对应的相册id
            album_id = album.album_id
            a_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[
                                14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            a_items.append(a_item)


        else:
            return render(request, 'goods_list.html',
                          {'tb_goods_list': tb_goods_list, 'service': service, 'noservice': noservice,})


# YZ 服务商详情页面
def service_details(request):
    if request.GET['goodsid']:
        service_detail_goods_id = request.GET['goodsid']
    goods = tb_goods.objects.get(goods_id=service_detail_goods_id)  # 获得需要购买的项目的id对应的服务商
    if (len(tb_goods_click.objects.filter(goods_id=service_detail_goods_id))):
        addclick = tb_goods_click.objects.filter(goods_id=service_detail_goods_id)[0]
        addclick.gocl_num += 1
        addclick.save()
    else:
        addclick = tb_goods_click(goods_id=service_detail_goods_id, goods_name=goods.goods_name, gocl_id=0, gocl_num=1)
        addclick.save()

    # 计算日期百分比用于赋值进度条
    starttime = goods.goods_accept_starttime
    endtime = goods.goods_accept_endtime
    days_total = (endtime - starttime).days

    days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days

    if days_remain <= 0:
        finish_percentage = 100
    else:
        finish_percentage = int((1 - (float(days_remain) / float(days_total))) * 100)

    #
    # 取服务对应的图片，赋值相册空间暂时还没有写，
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

    # 用于推荐其他服务商
    allgoods_for_itemhere = tb_goods.objects.filter(item_id=goods.item_id).order_by(
        "-goods_evaluation_good_star")  # 获取提供该项目支持的服务商，并按照他们的升序降序排列 排除自身！！根据评价的星星数为准
    # 从推荐服务商排除自己
    goods_myself = tb_goods.objects.get(goods_id=goods.goods_id)
    allgoods_for_itemhere = list(allgoods_for_itemhere)
    for good in allgoods_for_itemhere:
        if good.goods_id == goods_myself.goods_id:
            allgoods_for_itemhere.remove(good)

    # 获得排序最高的4个服务商
    if len(allgoods_for_itemhere) > 4:
        goods_recommend_display = allgoods_for_itemhere[0:4]
    else:
        goods_recommend_display = allgoods_for_itemhere

    # 格式化日期
    publish_time_format = starttime.strftime("%Y-%m-%d %H:%I:%S")
    datetime_format = endtime.strftime("%Y-%m-%d %H:%I:%S")
    # 判断是否是来自未登录用户的支付浏览
    showDialogflag = 0

    if 'unregist_tobepay_goodsid' in request.COOKIES:
        showDialogflag = 1
        response = render(request, 'service_detail.html',
                          {'goods': goods, 'finish_percentage': finish_percentage, 'pics_url': pics_url,
                           'publish_time_format': publish_time_format, 'datetime_format': datetime_format,
                           'goods_recommend_display': goods_recommend_display, 'showDialogflag': showDialogflag})
        response.delete_cookie('unregist_tobepay_goodsid')
        return response

    # print showDialogflag
    return render(request, 'service_detail.html',
                  {'goods': goods, 'finish_percentage': finish_percentage, 'pics_url': pics_url,
                   'publish_time_format': publish_time_format, 'datetime_format': datetime_format,
                   'goods_recommend_display': goods_recommend_display, 'showDialogflag': showDialogflag})


def sortServByComp(request):
    tb_goods_list = []
    if request.session['for_sort_itemid']:
        itemid = request.session['for_sort_itemid']

        # print "在排序当中"
        tb_goods_listTemp = tb_goods.objects.filter(item_id=itemid)  # 我们默认goods_sort代表点击率
        goodsorderTemp = tb_goods_click.objects.order_by('-gocl_num')
        for goods in goodsorderTemp:
            tb_goods_list.append(tb_goods.objects.get(goods_id=goods.goods_id))
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
                finish_percentage = int((1 - (float(days_remain) / float(days_total))) * 100)
            goods.goods_remaintime = finish_percentage  # 完成百分比为对象添加的属性
        return render(request, 'goods_list.html',
                      {'tb_goods_list': tb_goods_list, 'service': True, 'noservice': False,})
    else:
        return HttpResponse("没有选择相应的项目")


def sortServBypayahead(request):
    if request.session['for_sort_itemid']:
        itemid = request.session['for_sort_itemid']

        tb_goods_list = tb_goods.objects.order_by('goods_payahead').filter(item_id=itemid)  # 我们默认goods_sort代表点击率

        for goods in tb_goods_list:
            starttime = goods.goods_accept_starttime
            endtime = goods.goods_accept_endtime
            days_total = (endtime - starttime).days

            days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days

            if days_remain <= 0:
                finish_percentage = 100
            else:
                finish_percentage = int((1 - (float(days_remain) / float(days_total))) * 100)
            goods.goods_remaintime = finish_percentage  # 完成百分比为对象添加的属性
        return render(request, 'goods_list.html',
                      {'tb_goods_list': tb_goods_list, 'service': True, 'noservice': False,})
    else:
        return HttpResponse("没有选择相应的项目")


def sortServByaward(request):
    if request.session['for_sort_itemid']:
        itemid = request.session['for_sort_itemid']

        tb_goods_list = tb_goods.objects.order_by('goods_awardafter').filter(item_id=itemid)  # 我们默认goods_sort代表点击率

        for goods in tb_goods_list:
            starttime = goods.goods_accept_starttime
            endtime = goods.goods_accept_endtime
            days_total = (endtime - starttime).days

            days_remain = (endtime.replace(tzinfo=None) - datetime.datetime.now()).days

            if days_remain <= 0:
                finish_percentage = 100
            else:
                finish_percentage = int((1 - (float(days_remain) / float(days_total))) * 100)
            goods.goods_remaintime = finish_percentage  # 完成百分比为对象添加的属性
        return render(request, 'goods_list.html',
                      {'tb_goods_list': tb_goods_list, 'service': True, 'noservice': False,})
    else:
        return HttpResponse("没有选择相应的项目")


# YZ 查看合同
def contact_details(request):
    goodsid = 0
    if request.GET['goodsid']:
        # contact_file = open("D:\Users\yuanzhi\zhengzihui\zhengzihui\zhengzihui_app\static\contact_file\contact.txt","r+")#这是一个绝对路径
        # contact_string = contact_file.read().decode("gbk")#需要解码一下~不知道为什么YZ

        # contact_file.close()
        goodsid = request.GET['goodsid']
        contact_string = '政资汇合同详情：等待完善'
        return render(request, 'contact_details.html', {'goodsid': goodsid, 'contact_string': contact_string})
    return HttpResponse("还没有选择项目")


# YZ
def order_details(request):
    goodsid = 0
    if request.GET['goodsid']:
        goodsid = int(request.GET['goodsid'])
        goods = tb_goods.objects.get(goods_id=goodsid)  # 取到服务对象
        item = tb_item.objects.get(item_id=goods.item_id)  # 取得对应的申报项目的对象
        item_spa = tb_item_pa(ipa_id=item.item_pa_id)  # 获得项目发布机构对象
        goods_spa = tb_service_provider(sp_id=goods.sp_id)  # 获得服务提供商的对象
        user_id = int(request.COOKIES['user_id'])
        buyer = tb_user.objects.get(user_id=user_id)  # 获取当前用户对象

        # 生成随机的0-1000000的数，并不与数据库中的数相同;给order_no赋值
        order_no = random.randint(0, 1000000)
        while (len(tb_order.objects.filter(order_no=order_no)) == 1):
            order_no = random.randint(0, 1000000)
        #print type(item.item_name)
        # add_time 用的是插入数据时便生成，即保存最后修改的时间错。
        allorder = tb_order.objects.all()
        lastid = allorder[len(allorder) - 1].order_id

        order = tb_order(order_id=lastid + 1, order_no=order_no, goods_id=goodsid, pay_no=order_no,
                         item_id=item.item_id, item_name=item.item_name, sp_id=goods_spa.sp_id, \
                         sp_name=goods_spa.sp_name, buyer_id=buyer.user_id, buyer_name=buyer.user_name,
                         buyer_email=buyer.user_email, \
                         payment_code=order_no, payment_time=None, final_time=None, good_amount=goods.goods_payahead, \
                         order_amount=goods.goods_payahead + goods.goods_awardafter, \
                         refund_amount=goods.goods_payahead, delay_time=None, order_from=1, express_id=1, express_no=1,
                         eval_state=0, order_state=3, refund_state=0, lock_state=0, express_state=0)
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
    return render(request, 'order_details.html', {'order': order, 'goods': goods, 'item': item,})

    ##     #订单详情


def order_detail(request):
    # request.session['user_id'] = 3#此处设置了个session值用来测试，等登录模块完成之后再修改
    user = []
    a_click_items = []
    a_recommend_items = []
    if 'user_id' in request.COOKIES:
        user_id = int(request.COOKIES['user_id'])
        user = tb_user.objects.get(user_id=user_id)
    else:
        return HttpResponse("请先登录账号;请返回到上级页面登录或者注册")

    click_items = tb_item_click.objects.order_by('-click_counter')[:15]  # 获取点击率前15的项目
    for click_item in click_items:
        a_click_item = {}
        a_click_item['id'] = click_item.item_id  # 获取项目id
        a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name  # 获取项目名字
        a_click_item['item_ga'] = tb_item.objects.get(item_id=click_item.item_id).item_ga  # 获取项目资助金额
        album = \
        tb_album.objects.filter(album_type=0, affiliation_id=click_item.item_id, is_default=1).order_by('-nacl_sort')[
            0]  # 获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[
                                  14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
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
    recommend_items = tb_item.objects.filter(is_recommend=1).order_by('-item_id')[:15]  # 获取推荐的前15的项目
    for recommend_item in recommend_items:
        a_recommend_item = {}
        a_recommend_item['id'] = recommend_item.item_id  # 获取项目id
        a_recommend_item['name'] = recommend_item.item_name  # 获取项目名字
        album = tb_album.objects.filter(album_type=0, affiliation_id=recommend_item.item_id, is_default=1).order_by(
            '-nacl_sort')[0]  # 获取项目对应的相册id
        album_id = album.album_id
        a_recommend_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[
                                      14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_recommend_items.append(a_recommend_item)

    order_details_order_id = 1  # 取一个默认值
    if request.GET['id']:
        # 能保证取到吗
        order_details_order_id = request.GET['id']
    order = tb_order.objects.get(order_id=order_details_order_id)
    order.goods_code = (tb_goods.objects.get(goods_id=order.goods_id)).goods_code
    order.goods_name = (tb_goods.objects.get(goods_id=order.goods_id)).goods_name
    order.buyer_name = (tb_user.objects.get(user_id=order.buyer_id)).user_name
    order.buyer_telephone = (tb_user.objects.get(user_id=order.buyer_id)).user_telephone
    order.buyer_email = (tb_user.objects.get(user_id=order.buyer_id)).user_email
    # dont know why
    '''if order.lock_state == 0:
        if order.order_state == 0:
            order['order_state'] = '已取消'
        if order.order_state == 1:
            order['order_state'] = '未付款'
        if order.order_state == 2:
            order['order_state'] = '已付款'
        if order.order_state == 3:
            order['order_state'] = '已发货'
        if order.order_state == 4:
            order['order_state'] = '已验收'
    else:
        order['order_state'] = '申请处理中'''
    return render(request, 'user_info.html',
                  {'user': user, 'a_click_items': a_click_items, 'a_recommend_items': a_recommend_items,
                   'order': order})


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


'''
商家后台部分

'''
def get_today_order(wt_order ):
    td_order = []
    td_order = wt_order
    for order in wt_order:
        #print type(order.add_time)
        #order.add_time.replace(tzinfo=None)
        if (order.add_time.replace(tzinfo=None) -datetime.datetime.now()).days == 0 :
            pass
        else:
            td_order.remove(order)

    return td_order

#YZ 这个views还需要改进，等待女生们
def busindex(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    all_order = get_all_order_of_sp(sp_id)

    weichuli_order = []
    chulizhong_order = []
    daishenghe_order = []
    yiwancheng_order = []

    for order in all_order:
        if order.order_state == 1:
            weichuli_order.append(order)
        elif order.order_state == 2:
            chulizhong_order.append(order)
        elif order.order_state == 3:
            yiwancheng_order.append(order)
        else:
            pass

    all_wfto_num = len(weichuli_order)
    all_dsh_num = len(daishenghe_order)
    all_clz_num = len(chulizhong_order)
    all_ywc_num = len(yiwancheng_order)
    order_num_info = []
    order_num_info.append(all_wfto_num)
    order_num_info.append(all_dsh_num)
    order_num_info.append(all_ywc_num)
    order_num_info.append(all_clz_num)
    #今日数据用的是所有的数据，怎么搞还要想想

    '''#get today order
    #today_wcl_order = get_today_order(temp_wcl)
    today_dsh_order = get_today_order(daishenghe_order)
    today_ywc_order = get_today_order(yiwancheng_order)
    today_clz_order = get_today_order(chulizhong_order)
    today_order_num =[]
    today_order_num.append(0)
    today_order_num.append(len(today_dsh_order))
    today_order_num.append(len(today_ywc_order))
    today_order_num.append(len(today_clz_order))
    '''

    #get 3 latest comment
    latest_comment=[]
    latest_comment= tb_goods_evaluation.objects.all()[:2]
    #latest_comment =latest_comment[:2]

    mine_comment = []
    for comment in latest_comment:
        temp_goods = tb_goods.objects.get(goods_id = comment.goods_id)
        temp_sp = tb_service_provider.objects.get(sp_id = temp_goods.sp_id)
        if temp_sp:
            mine_comment.append(comment)

    mine_notice = []
    #later WILL changge YZ 没有针对不同的商家推送不同的通知，获取的是全网的通知
    latest_notice = Tb_Notice.objects.all()[:2]

    mine_notice = latest_notice
    #以开始接单时间排序，最新发布的服务，这里是为了避免老徐改他的代码所以没有添加一个publish_time的字段，应该是要添加的
    mine_leatest_serv = tb_goods.objects.filter(sp_id = sp_id).order_by('-goods_accept_starttime')
    if len(mine_leatest_serv) == 0:
        pass
    elif len(mine_leatest_serv) == 1:
        pass
    else:
        mine_leatest_serv = mine_leatest_serv[0:1]

    #mine_info_short = tb_user.objects.get()   wait for other
    context = {'weichuli_order':weichuli_order, 'order_num_info':order_num_info,'mine_comment':mine_comment, 'mine_notice':mine_notice, 'mine_leatest_serv':mine_leatest_serv,
               'mine_info_short':None,'latest_serv':mine_leatest_serv,'today_order_num':None,}
    response = render(request,"bus_index.html",context)
    response.set_cookie('first_page',1)
    return response


def busindex_sub(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    all_order = get_all_order_of_sp(sp_id)

    weichuli_order = []
    chulizhong_order = []
    daishenghe_order = []
    yiwancheng_order = []

    for order in all_order:
        if order.order_state == 1:
            weichuli_order.append(order)
        elif order.order_state == 2:
            chulizhong_order.append(order)
        elif order.order_state == 3:
            yiwancheng_order.append(order)
        else:
            pass

    all_wfto_num = len(weichuli_order)
    all_dsh_num = len(daishenghe_order)
    all_clz_num = len(chulizhong_order)
    all_ywc_num = len(yiwancheng_order)
    order_num_info = []
    order_num_info.append(all_wfto_num)
    order_num_info.append(all_dsh_num)
    order_num_info.append(all_ywc_num)
    order_num_info.append(all_clz_num)
    #今日数据用的是所有的数据，怎么搞还要想想

    '''#get today order
    #today_wcl_order = get_today_order(temp_wcl)
    today_dsh_order = get_today_order(daishenghe_order)
    today_ywc_order = get_today_order(yiwancheng_order)
    today_clz_order = get_today_order(chulizhong_order)
    today_order_num =[]
    today_order_num.append(0)
    today_order_num.append(len(today_dsh_order))
    today_order_num.append(len(today_ywc_order))
    today_order_num.append(len(today_clz_order))
    '''

    #get 3 latest comment
    latest_comment=[]
    latest_comment= tb_goods_evaluation.objects.all()[:2]
    #latest_comment =latest_comment[:2]

    mine_comment = []
    for comment in latest_comment:
        temp_goods = tb_goods.objects.get(goods_id = comment.goods_id)
        temp_sp = tb_service_provider.objects.get(sp_id = temp_goods.sp_id)
        if temp_sp:
            mine_comment.append(comment)

    mine_notice = []
    #later WILL changge YZ 没有针对不同的商家推送不同的通知，获取的是全网的通知
    latest_notice = Tb_Notice.objects.all()[:2]

    mine_notice = latest_notice
    #以开始接单时间排序，最新发布的服务，这里是为了避免老徐改他的代码所以没有添加一个publish_time的字段，应该是要添加的
    mine_leatest_serv = tb_goods.objects.filter(sp_id = sp_id).order_by('-goods_accept_starttime')
    if len(mine_leatest_serv) == 0:
        pass
    elif len(mine_leatest_serv) == 1:
        pass
    else:
        mine_leatest_serv = mine_leatest_serv[0:1]
    #get my bussiness info
    mine_info = tb_service_provider.objects.get(sp_id =sp_id)
    #mine_info_short = tb_user.objects.get()   wait for other
    context = {'weichuli_order':weichuli_order, 'order_num_info':order_num_info,'mine_comment':mine_comment, 'mine_notice':mine_notice, 'mine_leatest_serv':mine_leatest_serv,
               'mine_info_short':None,'latest_serv':mine_leatest_serv,'today_order_num':None,'mine_info':mine_info,}
    response = render(request,"bus_index_sub.html",context)
    response.set_cookie('first_page',1)
    return response


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

        # 添加的三个属性
        order.goods_name = goods_name
        order.buyer_expand_address = str(buyer_expand_address)
        order.buyer_expand_contact = str(buyer_expand_contact)
    return all_order
def bus_order_manage(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
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
    return render(request,"bus_order_manage.html",{'all_order':all_order,'sp_id':sp_id})






def change_paper_send_state(request):
    if 'order_id' in request.GET:
        order_id = request.GET.get('order_id')
        temp_order = tb_order.objects.get(order_id=order_id)
        temp_order.paper_send = 1
        temp_order.save()
        # 很冗余的代码，就是为了取订单
        if 'sp_id' in request.COOKIES:
            sp_id = request.COOKIES['sp_id']
        else:
            sp_id = 1
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
        return render(request, "bus_order_manage.html", {'all_order': all_order})
    else:
        return HttpResponse("没有正确的订单号")


def bus_counter_manage(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1

    # 获取该商家获得的所有订单
    all_order = get_all_order_of_sp(sp_id=sp_id)
    # 为每个订单添加一个服务名称的属性
    for order in all_order:

        if order.has_pay == 1:
            order.str_has_pay = '订单已经申请结算,正在结算中'
        elif order.has_pay == 2:
            order.str_has_pay = "订单已经结算"
        else:
            order.str_has_pay = '未结算'
    # request.session['first_page'] = 0
    return render(request, "bus_counter_manage.html", {'all_order': all_order, 'sp_id': sp_id})


def change_has_pay_state(request):
    if 'order_id' in request.GET:
        order_id = request.GET.get('order_id')
        temp_order = tb_order.objects.get(order_id=order_id)
        temp_order.has_pay = 1  # 状态1表示申请结算
        temp_order.save()
        # 很冗余的代码，就是为了取订单
        if 'sp_id' in request.COOKIES:
            sp_id = request.COOKIES['sp_id']
        else:
            sp_id = 1

        # 获取该商家获得的所有订单
        all_order = get_all_order_of_sp(sp_id=sp_id)
        for order in all_order:

            if order.has_pay == 1:
                order.str_has_pay = '订单已经申请结算,正在结算中'
            else:
                order.str_has_pay = '未结算'
        # request.session['first_page'] = 0
        return render(request, "bus_counter_manage.html", {'all_order': all_order})
    else:
        return HttpResponse("没有正确的订单号")


def sort_has_pay(request):
    sp_id = request.GET.get('sp_id')
    flag = request.GET.get('flag')
    if flag == '1':
        all_order = tb_order.objects.filter(sp_id=sp_id).order_by('-has_pay')
    else:
        all_order = tb_order.objects.filter(sp_id=sp_id).order_by('has_pay')
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
        if order.has_pay == 1:
            order.str_has_pay = '订单已经申请结算,正在结算中'
        elif order.has_pay == 2:
            order.str_has_pay = "订单已经结算"
        else:
            order.str_has_pay = '未结算'
        # 添加的三个属性
        order.goods_name = goods_name
        order.buyer_expand_address = str(buyer_expand_address)
        order.buyer_expand_contact = str(buyer_expand_contact)
    # request.session['first_page'] = 0
    return render(request, "bus_counter_manage.html", {'all_order': all_order, 'sp_id': sp_id})


def sort_order_manage(request):
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
    return render(request, "bus_order_manage.html", {'all_order': all_order, 'sp_id': sp_id})