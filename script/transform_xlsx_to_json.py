# -*- coding: UTF-8 -*-
"""
@Project ：rl-lab
@File    ：transform_xlsx_to_json.py
@Author  ：Yifu Yuan
@Date    ：2023/8/14
"""
import pandas as pd
import json

df = pd.read_excel("team_info.xlsx")

type_dict = {0: "faculty", 1: "Ph.D. Students", 2: "Graduate Students", 3: "Alumni"}

total_json = []
for type_index, type in type_dict.items():
    result = {"type": type, "item": []}
    for index, row in df.iterrows():
        if row["身份"] == type_index:
            img_path = f'assets/image/team/{row["姓名"]}.jpg'
            if row["个人主页链接"] == "(空)":
                link = ''
            else:
                link = row["个人主页链接"]
            item = {"name": row["姓名"], "desc": row["入学年份"], "img": img_path,
                    "link": link, "area": row["研究方向（英文）"]}
            result["item"].append(item)
    print(result)
    
    total_json.append(result)


json_str = json.dumps(total_json)
with open("../_data/team.json", "w") as f:
    f.write(json_str)

print("End")
