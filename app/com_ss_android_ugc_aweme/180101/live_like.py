#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   live_like.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 17:43   zxd        1.0         None
"""
import uiautomator2 as u2

from uiautomator2 import Device

from app.com_ss_android_ugc_aweme import constant


def main(device: Device, params: str):
    return constant.SUCCESS


if __name__ == '__main__':
    main(u2.connect(), None)
