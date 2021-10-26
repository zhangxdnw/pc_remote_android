#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   live_common.py
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 17:45   zxd        1.0         None
"""
import time

from uiautomator2 import Device


def check_params(params: str) -> str:
    return eval(params)['comment']


def live_do_comment(device: Device, click_id: str, layout_id: str, comment: str, submit_id: str) -> bool:
    # 点击弹幕输入
    device(resourceId=click_id).click(timeout=1)
    time.sleep(1)
    # 找到输入框
    if not device(resourceId=layout_id).exists:
        return False
    editor = device(resourceId=layout_id).sibling(className='android.widget.EditText')
    if not editor.exists:
        return False
    # 输入文字
    editor.set_text(comment)
    time.sleep(1)
    # 提交
    device(resourceId=submit_id).click(1)
    return True


def live_do_like() -> bool:
    return False


def live_do_gift() -> bool:
    return False


def live_do_fans() -> bool:
    return False
