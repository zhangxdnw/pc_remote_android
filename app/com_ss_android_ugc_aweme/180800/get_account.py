#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   get_account.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/12/03 00:33   zxd        1.0         None
"""
import uiautomator2 as u2

from uiautomator2 import Device

from app.com_ss_android_ugc_aweme import constant
from utils import device_util
from constant180800 import *

def main(device: Device, params: str):
    # 打开抖音
    device.app_start(constant.APP_PACKAGE, wait=True)
    current_app = device_util.top_app(device)
    if not current_app.__eq__(constant.APP_PACKAGE):
        return constant.LAUNCH_ERROR

    # 点击我
    device.xpath(main_tab_mine_xpath).click(timeout=1)

    # 获取帐号信息并打印
    account = device(resourceId=mine_account_id).get_text(timeout=1)
    print(account)

    device_util.stop_app(device, constant.APP_PACKAGE)

    return constant.SUCCESS


if __name__ == '__main__':
    main(u2.connect(), None)

