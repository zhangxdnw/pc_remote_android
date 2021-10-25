#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   main.py    
@Contact :   379327479@qq.com
@License :   MIT

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/10/25 10:23   zxd        1.0         None
"""

import argparse
import importlib
import os

from utils import device_util, string_util


def do_action(device: str, package: str, action: str, extras: str):
    """
    设置指定设备，对指定应用执行相应操作
    Args:
        device: 设备序列号
        package: 目标应用的包名
        action: 需要执行的操作，调用***.py文件
        extras: 执行参数，见***.py文件说明

    Returns:
        执行结果返回码
    """
    # 确定连接设备
    phone = device_util.connect(device)
    # 找到指定应用信息
    info = phone.app_info(package)
    print(info)
    # 根据action找到执行的脚本
    abs_path1 = os.path.join('app', string_util.replace_dot_to_underline(info['packageName']),
                             str(info['versionCode']), action)
    abs_path2 = os.path.join('app', string_util.replace_dot_to_underline(info['packageName']),
                             'default', action)
    path1, path2 = os.path.join(os.getcwd(), abs_path1) + '.py', os.path.join(os.getcwd(), abs_path2) + '.py'
    if not os.path.exists(path1):
        if not os.path.exists(path2):
            return 9
        else:
            default_file = importlib.import_module(abs_path2.replace(os.sep, '.'))
            return default_file.main(phone, extras)
    else:
        return 0


def main():
    """
    主运行程序，需要指定哪个设备，做什么动作，附带参数。参数使用json格式
    Returns:
    """
    parser = argparse.ArgumentParser(description='Main Execute')
    parser.add_argument('-d', '--device', help='Target Device', required=True)
    parser.add_argument('-p', '--package', help='Target Application Package Name', required=True)
    parser.add_argument('-a', '--action', help='Do Action', required=True)
    parser.add_argument('-x', '--extras', help='Extra Parameters')
    args = parser.parse_args()
    # 参数校验出错，直接返回错误码2
    print(args)
    do_action(args.device, args.package, args.action, args.extras)


if __name__ == '__main__':
    main()
