#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   live_commenting.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 17:43   zxd        1.0         None
"""
import sys

from uiautomator2 import Device
import uiautomator2 as u2

from app.com_ss_android_ugc_aweme import constant
from app.com_ss_android_ugc_aweme.common import live_common

sys.path.append('app/com_ss_android_ugc_aweme/180101')
from constant180101 import *


def main(device: Device, params: str):
    live_common.live_quit(device, live_quit_id)
    return constant.SUCCESS


if __name__ == '__main__':
    main(u2.connect(), None)
