"""
Main entry point for the LLM Report System
"""

import os
from dotenv import load_dotenv
import argparse
from src.config.settings import settings
from src.recommender import recommender_func

TOP_N = int(settings.TOP_N)

if __name__ == "__main__":
    print(111)
    parser = argparse.ArgumentParser(description="Run KOL Recommendation")
    parser.add_argument("--性别", dest="gender", required=False, help="男、女")
    parser.add_argument("--年龄", dest="age", required=False, help="00后、90后、80后、70后、70前")
    parser.add_argument("--国籍", dest="national", required=False, help="中国、韩国、美国、日本、其他国家")
    parser.add_argument("--职业", dest="occupation", required=False, help="演员、歌手、模特、导演、主持人、网红、偶像、电竞选手、虚拟偶像、商界任务")
    parser.add_argument("--形象", dest="image", required=False, help="多才多艺、阳光活力...")
    parser.add_argument("--粉丝性别", dest="fans_gender", required=False, help="男、女")
    parser.add_argument("--粉丝年龄", dest="fans_age", required=False, help="0-17、18-24、25-29、30-34、35-39、40-49、50-59、60+")
    parser.add_argument("--粉丝城市级别", dest="fans_city", required=False, help="一线城市、二线城市、三线城市、四线城市、五线城市")
    parser.add_argument("--粉丝区域", dest="fans_region", required=False, help="华北、东北、华东、华中、西南、西北、华南")
    parser.add_argument("--粉丝省份", dest="fans_province" ,required=False, help="北京市、上海市、河北省、江苏省…")
    print(111)
    args = parser.parse_args()
    # Extract values
    gender = args.gender
    age = args.age
    national = args.national
    occupation = args.occupation
    image = args.image
    fans_gender = args.fans_gender
    fans_age = args.fans_age
    fans_city = args.fans_city
    fans_region = args.fans_region
    fans_province = args.fans_province

    l_attr_detailed = [gender,age,national,occupation,image,fans_gender,fans_age,fans_city,fans_region,fans_province]
    l_attr_str = ['性别', '年龄', '国籍', '职业', '形象', '粉丝性别', '粉丝年龄', '粉丝城市级别', '粉丝区域', '粉丝省份']
    l_attr_retain = []
    l_attr_detailed_modified = []
    for _str,_val in zip(l_attr_str,l_attr_detailed):
        if _val:
            l_attr_retain.append(_str)
            l_val = _val.split('、')
            l_val = [f'{_str}_{i}' for i in l_val]
            l_attr_detailed_modified+=l_val
    l_attr_retain = list(set(l_attr_retain))

    res = recommender_func(l_attr_retain,l_attr_detailed_modified,TOP_N)


# python main.py --性别 "男" --年龄 "00后" --国籍 "中国" --职业 "网红" --形象 "多才多艺" --粉丝性别 "女" --粉丝年龄 "25-29" --粉丝城市级别 "一线城市" --粉丝区域 "华东、华中" --粉丝省份 "北京市、上海市"
