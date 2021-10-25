#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   search_common.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 17:45   zxd        1.0         None
"""
import time

from uiautomator2 import Device

from app.com_ss_android_ugc_aweme import constant
from utils import device_util


def check_params(params: str) -> str:
    return eval(params)['keyword']


def search_keyword(device: Device, find_id: str, input_id: str, keywords: str,
                   search_button_id: str, result_layout_id: str) -> bool:
    print('find keyword')
    device(resourceId=find_id).click(timeout=1)
    time.sleep(1)
    device(resourceId=input_id).set_text(keywords, timeout=1)
    time.sleep(1)
    device(resourceId=search_button_id).click(timeout=1)
    time.sleep(3)
    return device(resourceId=result_layout_id).exists


def search_user_result(device: Device, user_xpath: str, first_select_xpath: str) -> bool:
    print('find user')
    device.xpath(user_xpath).click(timeout=1)
    time.sleep(1)
    device.xpath(first_select_xpath).click(timeout=1)
    return device_util.top_activity(device).__eq__(constant.ACT_USER_PROFILE)


def search_live_result(device: Device, live_xpath: str, first_select_xpath: str) -> bool:
    print('find live')
    device.xpath(live_xpath).click(timeout=1)
    time.sleep(1)
    device.xpath(first_select_xpath).click(timeout=1)
    return device_util.top_activity(device).__eq__(constant.ACT_LIVE_DETAIL)

