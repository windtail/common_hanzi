# coding:utf-8

"""
常用汉字

GB2312字符集的区位分布表可以理解成是一个表格，对所收汉字进行了 “分区” 处理，每区含有94个汉字／符号。
 区号    字数    字符类别
    01      94    一般符号
    02      72    顺序号码
    03      94    拉丁字母
    04      83    日文假名
    05      86    Katakana
    06      48    希腊字母
    07      66    俄文字母
    08      63    汉语拼音符号
    09      76    图形符号
 10-15            备用区
 16-55    3755    一级汉字，以拼音为序
 56-87    3008    二级汉字，以笔划为序
 88-94            备用区

 编码=区+0xA0,区内偏移+0xA0
"""

import struct

__all__ = ["level1_chars", "level2_chars"]


def _char(region, offset):
    return struct.pack("2B", region + 0xA0, offset + 0xA0)


def _region_range_chars(first_region, last_region):
    for region in range(first_region, last_region + 1):
        for offset in range(1, 94 + 1):
            try:
                yield _char(region, offset).decode('gb2312')
            except UnicodeDecodeError:
                pass


def level1_chars():
    return _region_range_chars(16, 55)


def level2_chars():
    return _region_range_chars(56, 87)


if __name__ == '__main__':
    assert len(tuple(level1_chars())) == 3755
    assert len(tuple(level2_chars())) == 3008
