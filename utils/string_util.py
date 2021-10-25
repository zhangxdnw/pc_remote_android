#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   string_util.py    
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 10:57   zxd        1.0         None
"""


def replace_underline_to_dot(origin: str) -> str:
    """
    包名与路径名转换，替换 下划线 为 点
    Args:
        origin: 带下划线路径名

    Returns:Android应用包名

    """
    return origin.replace('_', '.')


def replace_dot_to_underline(origin: str) -> str:
    """
    包名与路径名转换，替换 点 为 下划线
    Args:
        origin: Android应用包名

    Returns:带下划线路径名

    """
    return origin.replace('.', '_')
