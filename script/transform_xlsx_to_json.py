# -*- coding: UTF-8 -*-
"""
@Project ：rl-lab
@File    ：transform_xlsx_to_json.py
@Author  ：Yifu Yuan
@Date    ：2023/8/14
"""
import pandas as pd
import json
import os


total_json = []

# ----------------------------FACULTY----------------------------------
df = pd.read_excel("faculty_info.xlsx")
result = {"type": "Faculty", "item": []}
for index, row in df.iterrows():
    img_path = f'/assets/image/team/{row["姓名"]}.jpg'
    if not os.path.exists("../" + img_path):
        img_path = f'/assets/image/team/{row["姓名"]}.png'
    link = row["个人主页"]
    item = {"name": row["姓名"],
            "desc": row["职位"], "img": img_path,
            "link": link, "area": "Research Area: " + row["研究方向"]}
    result["item"].append(item)
print(result)

total_json.append(result)

# ----------------------------STUDENTS----------------------------------
df = pd.read_excel("team_info.xlsx")
type_dict = {1: "Ph.D. Students", 2: "Graduate Students"}
year_dict = {1: "1st Year", 2: "2nd Year", 3: "3rd Year", 4: "4th Year"}
loc_dict = {1: " Ph.D.", 2: " Master"}
for type_index, type in type_dict.items():
    result = {"type": type, "item": []}
    for index, row in df.iterrows():
        if row["身份"] == type_index:
            img_path = f'/assets/image/team/{row["姓名"]}.jpg'
            if not os.path.exists("../" + img_path):
                img_path = f'/assets/image/team/{row["姓名"]}.png'
            if row["个人主页链接"] == "(空)":
                link = ''
            else:
                link = row["个人主页链接"]
            item = {"name": row["姓名"],
                    "desc": year_dict[2023 - row["入学年份"] + 1] + loc_dict[type_index] + "<br>"
                            + row["学院"], "img": img_path,
                    "link": link, "area": "Research Area: " + row["研究方向（英文）"]}
            result["item"].append(item)
    print(result)
    
    total_json.append(result)


# -----------------------------Alumni-----------------------------------
result = {"type": "Alumni (Ph.D.)", "item": []}
loc_dict = {1: "Master", 2: "Ph.D."}
df = pd.read_excel("alumni_info_phd.xlsx")
for index, row in df.iterrows():
    img_path = f'/assets/image/team/{row["姓名"]}.jpg'
    if not os.path.exists("../" + img_path):
        img_path = f'/assets/image/team/{row["姓名"]}.png'
    if row["个人主页链接"] == "(空)":
        link = ''
    else:
        link = row["个人主页链接"]
    item = {"name": row["姓名"], "desc": f"Graduated with a {loc_dict[row['身份']]} "
                                         f"degree in {row['毕业年份']}, {row['毕业去向']}", "img": img_path,
            "link": link, "area": "Research Area: " + row["研究方向（英文）"]}
    result["item"].append(item)
print(result)

total_json.append(result)


# -----------------------------Alumni-----------------------------------
result = {"type": "Alumni (Master)", "item": []}
loc_dict = {1: "Master", 2: "Ph.D."}
df = pd.read_excel("alumni_info.xlsx")
for index, row in df.iterrows():
    img_path = f'/assets/image/team/{row["姓名"]}.jpg'
    if not os.path.exists("../" + img_path):
        img_path = f'/assets/image/team/{row["姓名"]}.png'
    if row["个人主页链接"] == "(空)":
        link = ''
    else:
        link = row["个人主页链接"]
    item = {"name": row["姓名"], "desc": f"Graduated with a {loc_dict[row['身份']]} "
                                         f"degree in {row['毕业年份']}, working at {row['毕业去向']}", "img": img_path,
            "link": link, "area": "Research Area: " + row["研究方向（英文）"]}
    if row["姓名"] == "杨耀东":
        item = {"name": row["姓名"], "desc": f"Graduated with a {loc_dict[row['身份']]} "
                                             f"degree in {row['毕业年份']}, {row['毕业去向']}",
                "img": img_path,
                "link": link, "area": "Research Area: " + row["研究方向（英文）"]}
    if row["姓名"] == "张程伟":
        item = {"name": row["姓名"], "desc": f"Graduated with a {loc_dict[row['身份']]} "
                                             f"degree in {row['毕业年份']}, Associate Professor, {row['毕业去向']}",
                "img": img_path,
                "link": link, "area": "Research Area: " + row["研究方向（英文）"]}
    result["item"].append(item)
print(result)

total_json.append(result)


json_str = json.dumps(total_json)
with open("../_data/team.json", "w") as f:
    f.write(json_str)

print("End")
