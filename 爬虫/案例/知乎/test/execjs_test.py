# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/21 21:48
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import execjs

with open('./demo1.js',encoding='utf-8') as fp:
    js_content = fp.read()

# print(js_content)
#
jj = execjs.compile(js_content)
print(jj.call('x1'))
