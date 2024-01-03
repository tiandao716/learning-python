# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-02 7:41
"""
# 乱码解决
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

f = open('./test.js', encoding='utf-8')
r = execjs.compile(f.read())
result = r.call('fun1', 'alex_wsir_qiaofu_我是谁')
print(result)
