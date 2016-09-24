#-*- coding:utf-8 -*-

from fr_app.models import *
from data import *

def insert_test_data_for_sc_item():
    for i in sc_item_data:
        item = sc_item.objects.create(
            item_type=i['item_type'],
            price = i['price'],
            start_time = i['start_time'],
            end_time = i['end_time'],
            supplier = i['supplier'],
            item_name = i['item_name'],
            item_details = i['item_details']
        )

"""
def insert_teset_data_for_tb_pic():
    pass


def insert_test_data_form_tb_album():
    pass


def insert_data(data):
    for key,value in data.items():
        
"""

