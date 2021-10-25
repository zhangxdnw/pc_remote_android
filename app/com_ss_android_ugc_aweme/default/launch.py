#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   launch.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 15:29   zxd        1.0         None
"""
import time

import uiautomator2 as u2
from uiautomator2 import Device

from app.com_ss_android_ugc_aweme import constant
from utils import device_util


def main(device: Device, params: str):
    device.app_start(constant.APP_PACKAGE, wait=True)
    current_app = device_util.top_app(device)
    if not current_app.__eq__(constant.APP_PACKAGE):
        return constant.LAUNCH_ERROR

    # 找到最上层activity
    top_activity = device_util.top_activity(device)
    if top_activity.__eq__(constant.ACT_MAIN):
        activity_windows = device_util.activity_window(device, top_activity)
        if len(activity_windows) == 1:
            return constant.SUCCESS
        else:
            # 有弹窗，尝试点掉
            return constant.LAUNCH_ERROR
    else:
        # 其他界面 尝试等待
        time.sleep(3)
        return constant.LAUNCH_ERROR


if __name__ == '__main__':
    main(u2.connect(), None)
