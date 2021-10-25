#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   find_user.py    
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 17:43   zxd        1.0         None
"""

import uiautomator2 as u2

from uiautomator2 import Device
from app.com_ss_android_ugc_aweme.common import find_user_common

main_find_button_id = 'com.ss.android.ugc.aweme:id/dg1'
SEARCH_ACT = 'com.ss.android.ugc.aweme.search.activity.SearchResultActivity'
search_input_edittext_id = ''


def main(device: Device, params: str):
    find_user_common.find_user(device, main_find_button_id, SEARCH_ACT, search_input_edittext_id, 'dyf53ql2bjy3')


if __name__ == '__main__':
    main(u2.connect(), None)
