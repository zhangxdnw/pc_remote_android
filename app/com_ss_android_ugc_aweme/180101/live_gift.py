#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   live_gift.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 17:43   zxd        1.0         None
"""
import sys

import uiautomator2 as u2
from uiautomator2 import Device

from app.com_ss_android_ugc_aweme import constant
from app.com_ss_android_ugc_aweme.common import live_common

sys.path.append('app/com_ss_android_ugc_aweme/180101')
from constant180101 import *


def main(device: Device, params: str):
    gift_type, page, index = live_common.check_gift_params(params);
    if not live_common.live_do_gift(device, live_gift_click_id, "", page, "", "", ""):
        return constant.LIVE_ERROR
    else:
        return constant.SUCCESS


if __name__ == '__main__':
    main(u2.connect(), '{"type":0, "page":1, "index":2}')
