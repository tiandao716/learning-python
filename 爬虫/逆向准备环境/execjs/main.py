# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-30 7:50
"""
import execjs

# 创建node对象
node = execjs.get()

# 编译js文件返回上下文ctx对象
ctx = node.compile(open('test.js', 'r', encoding='utf-8').read())

# 执行
resuult = ctx.eval('getPwd("22323")')
print(resuult)
