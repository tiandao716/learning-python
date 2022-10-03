# -*- coding: utf-8 -*-
"""
 @Time : 2022/9/22 19:45
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : rename mail.py
 根据eml文件的MD5值改写文件名。
"""

from GetFileMd5 import GetFileMd5
import os
from concurrent.futures import ThreadPoolExecutor


def walk_dir(dir):
    """
    遍历文件夹，返回各个文件的路径
    :param dir:
    :return:
    """

    if not os.path.isdir(dir):
        print(f"{dir}不是一个目录")
        return -1
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


def RenameFileName(mail_file_path=''):
    """

    @param mail_file_path:
    @return:
    """
    if mail_file_path.endswith('.eml'):

        md5sum = GetFileMd5(mail_file_path)
        # 文件md5获取失败，则继续
        if md5sum is None:
            return
        print(mail_file_path, md5sum)

        new_file_name = md5sum + '.eml'
        new_file_path = os.path.join(os.path.dirname(mail_file_path), new_file_name)

        if not os.path.isfile(new_file_path):
            print('准备重命名文件')
            print(f'新的文件名（带路径）：{new_file_path}')
            try:
                os.renames(mail_file_path, new_file_path)
            except Exception as e:
                print("重命名过程中出错：", e)


if __name__ == '__main__':
    # RenameFileName(root_dir=r'F:\eml_new\2015-09')
    with ThreadPoolExecutor() as t:
        for i in walk_dir(r'F:\eml_new'):
            t.submit(RenameFileName, i)
