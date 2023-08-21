# -*- coding: UTF-8 -*-
"""
@Project ：rl-lab 
@File    ：compose_pic.py
@Author  ：Yifu Yuan
@Date    ：2023/8/21
"""
from PIL import Image
import os

folder_path = r"E:\rl-lab\assets\image\team"
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        try:
            image = Image.open(os.path.join(folder_path, filename))
    
            if os.path.getsize(os.path.join(folder_path, filename)) > 300 * 300:
                image = image.resize((int(image.size[0]*0.6), int(image.size[1]*0.6)))
                image.save(os.path.join(folder_path, filename))
        except:
            print(filename)

print("Finish")
