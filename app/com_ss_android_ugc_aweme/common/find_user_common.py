#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   find_user_common.py    
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 17:45   zxd        1.0         None
"""
from uiautomator2 import Device


def find_user(device: Device, find_id: str, find_act: str, input_id: str, keywords: str):
    print('find user')
