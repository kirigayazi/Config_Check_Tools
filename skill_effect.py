import json
import pandas as pd

'''
读取skill.json
通过字典key为result的value去定位，对应的skill_effect_info表的id，
绑定在skill_number key为result的value中
'''

# 读取 skill.json 文件
json_file_path = 'skill.json'
with open(json_file_path, 'r') as json_file:
    data_list = json.load(json_file)

# 假设 skill_effect 表格存储在 xlsx 文件中，且 skill_passive_info 是其中的一个页签
file_path = 'skill_技能效果.xlsx'
sheet_name = 'skill_passive_info'
skill_effect_df = pd.read_excel(file_path, sheet_name, header=5)

new_data_list = []

# 遍历每个字典
for item in data_list:
    # 检查字典中是否存在 'skills' 作为 key
    if 'skills' in item:
        # 获取 'skills' 对应的值
        skills_value = item['skills']
        # 如果 'skills' 的值不为空，则继续检索
        if skills_value:
            # 遍历值，逐个检索 skill_effect 表并输出 effect_1 列的值
            for value in skills_value:
                # 使用 Pandas 进行检索和输出
                result = skill_effect_df[skill_effect_df['id'] == value]['effect_1'].values
                if len(result) > 0:
                    result_value = str(result[0]).rstrip('0').rstrip('.')
                    # 创建新的字典
                    new_dict = {'id': value, 'result': result_value}
                    # 存储到新的字典列表中
                    new_data_list.append(new_dict)

# 存储新的字典列表到 skill_effect.json 文件
with open('skill_number.json', 'w') as json_file:
    json.dump(new_data_list, json_file, indent=2)

# 输出新的字典列表
print(new_data_list)
