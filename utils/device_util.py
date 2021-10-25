#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   device_util.py    
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 10:23   zxd        1.0         None
"""

from adbutils import adb
import uiautomator2 as u2
from uiautomator2 import Device


def list_all_devices() -> []:
    """
    列出当前所有连接的设备
    Returns:
        已连接设备的序列号数组, 没有连接设备返回空数组
    """
    device_list = adb.device_list()
    if len(device_list) < 1:
        return []
    else:
        return [device.serial for device in device_list]


def connect(addr: str) -> Device:
    return u2.connect(addr)


def top_app(device: Device) -> str:
    return device.current_app()['package']


def top_activity(device: Device) -> str:
    return device.app_current()['package'] + device.app_current()['activity']


def activity_window(device: Device, activity: str) -> list:
    wins = device.shell("dumpsys window " + activity + " | grep \"Window #\"")
    return wins.output.strip().split('\n')


if __name__ == '__main__':
    print(list_all_devices())
