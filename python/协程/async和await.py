# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-01 15:56
"""
import asyncio


async def fun1():
    print(1)
    # 网络IO请求，下载一张图片
    await asyncio.sleep(2)
    print(2)


async def fun2():
    print(3)
    # 网络IO请求，下载一张图片
    await asyncio.sleep(2)
    print(4)


if __name__ == '__main__':
    tasks = [
        asyncio.ensure_future(fun1()),
        asyncio.ensure_future(fun2()),
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
