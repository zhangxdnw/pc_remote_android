#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   kill.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/26 9:49   zxd        1.0         None
"""
import uiautomator2 as u2
from uiautomator2 import Device

from app.com_ss_android_ugc_aweme import constant
from utils import device_util


def main(device: Device, params: str):
    device_util.stop_app(device, constant.APP_PACKAGE)


if __name__ == '__main__':
    main(u2.connect(), None)
