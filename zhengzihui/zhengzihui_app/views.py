# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json #用来将字典类型的数据序列化，然后传给模板以及js,不能序列化model实例
from django.core import serializers #用来序列化model 传给js
from models import tb_item,tb_item_class,tb_item_pa,tb_article,tb_album,tb_pic
# Create your views here.

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


#点击搜索的下一级
def ind(request):
	#创建一些数据库记录
    p1 = tb_item(
            item_id = 20151,
            item_code = "40%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/2.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 21,
            item_from = 0,
            is_recommend = 0,)
    p1.save()
    p2=tb_item(
            item_id = 20152,
            item_code = "2%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划精准医学研究等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/3.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 78,
            item_from = 0,
            is_recommend = 0,
            )
    p2.save()

    p3 = tb_item(
            item_id = 20153,
            item_code = "70%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/4.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 56,
            item_from = 0,
            is_recommend = 0,
            )
    p3.save()
    p4 = tb_item( item_id = 20154,
            item_code = "50%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/5.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 89,
            item_from = 0,
            is_recommend = 0,
            )
    p4.save()
    p5 = tb_item( item_id = 20155,
            item_code = "40%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/6.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 99,
            item_from = 0,
            is_recommend = 0,
            )
    p5.save()
    p6 = tb_item( item_id = 20156,
            item_code = "100%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a1.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 234,
            item_from = 0,
            is_recommend = 0,
            )
    p6.save()
    p7 = tb_item( item_id = 20157,
            item_code = "90%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a2.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 123,
            item_from = 0,
            is_recommend = 0,
            )
    p7.save()
    p8 = tb_item( item_id = 20158,
            item_code = "0%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a3.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 564,
            item_from = 0,
            is_recommend = 0,
            )
    p8.save()
    p9 = tb_item( item_id = 20159,
            item_code = "30%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a4.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 234,
            item_from = 0,
            is_recommend = 0,
            )
    p9.save()
    p10 = tb_item( item_id = 201510,
            item_code = "50%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a5.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 12,
            item_from = 0,
            is_recommend = 0,
            )
    p10.save()
    p11 = tb_item( item_id = 201511,
            item_code = "90%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a6.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 89,
            item_from = 0,
            is_recommend = 0,
            )
    p11.save()
    p12 = tb_item( item_id = 201512,
            item_code = "30%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a7.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 576,
            item_from = 0,
            is_recommend = 0,
            )
    p12.save()
    p13 = tb_item( item_id = 201513,
            item_code = "89%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/2.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 321,
            item_from = 0,
            is_recommend = 0,
            )
    p13.save()
    p14 = tb_item( item_id = 201514,
            item_code = "33%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/3.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 354,
            item_from = 0,
            is_recommend = 0,
            )
    p14.save()
    p15 = tb_item( item_id = 201515,
            item_code = "66%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/4.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 799,
            item_from = 0,
            is_recommend = 0,
            )
    p15.save()
    p16 = tb_item( item_id = 201516,
            item_code = "88%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/5.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 465,
            item_from = 0,
            is_recommend = 0,
            )
    p16.save()
    p17 = tb_item( item_id = 201517,
            item_code = "90%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/6.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 124,
            item_from = 0,
            is_recommend = 0,
            )
    p17.save()
    p18 = tb_item( item_id = 201518,
            item_code = "56%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a1.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 89,
            item_from = 0,
            is_recommend = 0,
            )
    p18.save()
    p19 = tb_item( item_id = 201519,
            item_code = "40%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a2.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 45,
            item_from = 0,
            is_recommend = 0,
            )
    p19.save()
    p20 = tb_item( item_id = 201520,
            item_code = "10%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a3.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 87,
            item_from = 0,
            is_recommend = 0,
            )
    p20.save()
    p21 = tb_item( item_id = 201521,
            item_code = "20%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a4.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 90,
            item_from = 0,
            is_recommend = 0,
            )
    p21.save()
    p22 = tb_item( item_id = 201522,
            item_code = "30%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a5.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 123,
            item_from = 0,
            is_recommend = 0,
            )
    p22.save()
    p23 = tb_item( item_id = 201523,
            item_code = "89%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a6.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 432,
            item_from = 0,
            is_recommend = 0,
            )
    p23.save()
    p24 = tb_item( item_id = 201524,
            item_code = "45%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/a7.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 21,
            item_from = 0,
            is_recommend = 0,
            )
    p24.save()
    p25 = tb_item( item_id = 201525,
            item_code = "78%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/2.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 78,
            item_from = 0,
            is_recommend = 0,
            )
    p25.save()
    p26 = tb_item( item_id = 201526,
            item_code = "40%",
            item_name = "四川省科学技术厅关于组织申报国家重点研发计划纳米科技等重点专项2016年度项目的通知",
            itcl_id = 2015,
            item_level = 1,
            item_ga = "四川省科技厅",
            item_pa_id = 3,
            item_publish = 3,
            item_deadtime = 3,
            item_about = "纳米项目",
            item_url = "../static/images/3.jpg",
            item_key = "高精尖",
            item_status = 0,
            is_hot = 45,
            item_from = 0,
            is_recommend = 0,
            )
    p26.save()

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