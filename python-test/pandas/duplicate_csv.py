# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-24 12:15

"""

import pandas as pd

# dataFrame = pd.read_csv(r'd:\shoujihao.csv', header=1,chunksize=10000,
#                         names=["PROD_INST_ID", "CUST_ID", "LATN", "BUSI_NBR", "USER_NAME", "CUST_NAME", "INSTALL_ADDR", "CERTIFICATES_NBR", "mod_time"], low_memory=False)


dataFrame = pd.concat((chunk for chunk in pd.read_csv(r'd:\shoujihao.csv',header=1,chunksize=5000,low_memory=False)))
print(type(dataFrame))
# 以哪几列进行分组
group = dataFrame.groupby(["PROD_INST_ID", "CUST_ID", "LATN", "BUSI_NBR", "USER_NAME", "CUST_NAME", "INSTALL_ADDR", "CERTIFICATES_NBR"])
# print(type(group))

# 分组后的条件选择
data = group.agg('max')

# 保存到csv文件中
data.to_csv('shoujihao_single.csv')
