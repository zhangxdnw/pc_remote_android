#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   find_live.py
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
from app.com_ss_android_ugc_aweme.common import search_common

sys.path.append('app/com_ss_android_ugc_aweme/180101')
from constant180101 import *


def main(device: Device, params: str):
    keyword = search_common.check_params(params)
    if not keyword:
        return constant.ERROR_ACTION_PARAMS
    if search_common.search_keyword(device, main_find_button_id, search_input_edittext_id, keyword,
                                    search_search_button_id, search_horizontal_scroll_id):
        if search_common.search_live_result(device, search_live_xpath, search_live_first_select_xpath):
            return constant.SUCCESS
    else:
        return constant.SEARCH_ERROR


if __name__ == '__main__':
    main(u2.connect(), '{"keyword":"L7772221"}')
