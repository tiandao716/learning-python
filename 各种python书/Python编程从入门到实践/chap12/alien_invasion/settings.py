# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/13 7:51
"""


class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
<<<<<<< HEAD
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.5
=======
<<<<<<< HEAD

        # 子弹设置
        self.bullet_speed = 1.0
=======
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.5
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 为1 表示向右移，为-1表示向左移。
        self.fleet_direction = 1
<<<<<<< HEAD
=======
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
