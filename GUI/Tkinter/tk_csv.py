# -*- coding: utf-8 -*-
"""
 @Time : 2024/5/7 20:57
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import tkinter as tk
from tkinter import filedialog
import csv


class CSVEditor:
    """

    """
    def __init__(self, master):
        self.master = master
        self.master.title("CSV Editor")
        # 创建控件
        self.btn_open = tk.Button(master, text="Open", command=self.open_csv)
        self.btn_save = tk.Button(master, text="Save", command=self.save_csv)
        self.btn_close = tk.Button(master, text="Close", command=self.close_csv)
        self.label = tk.Label(master, text="CSV Editor")
        self.text = tk.Text(master, width=40, height=40)
        # 布局控件
        self.label.grid(row=0, column=0, columnspan=3)
        self.btn_open.grid(row=1, column=0)
        self.btn_save.grid(row=1, column=1)
        self.btn_close.grid(row=1, column=2)
        self.text.grid(row=2, column=0, columnspan=3)
        # 初始化变量
        self.filename = None
        self.data = []

    def open_csv(self):
        # 打开 CSV 文件
        self.filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not self.filename:
            return
        # 读取 CSV 数据
        with open(self.filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            self.data = [row for row in reader]
            # 在 GUI 界面中[显示]数据
            self.text.delete("1.0", "end")
            for row in self.data:
                self.text.insert("end", ",".join(row) + "\n")

    def save_csv(self):
        # 如果没有打开 CSV 文件，则不执行保存操作
        if not self.filename:
            return
        # 从 GUI 界面中获取新数据
        new_data = [row.split(",") for row in self.text.get("1.0", "end").split("\n") if row]
        # 将新数据写入 CSV 文件
        with open(self.filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in new_data:
                writer.writerow(row)
            # 更新内存中的数据
            self.data = new_data

    def close_csv(self):
        # 关闭 CSV 文件
        self.filename = None
        self.data = []
        self.text.delete("1.0", "end")


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVEditor(root)
    root.mainloop()
