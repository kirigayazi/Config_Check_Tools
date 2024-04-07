import pandas as pd
import json

'''
从knight 表中，读取魂师ID 为1001至3033的魂师的对应的升星的buffid'
并且将对应的knight_id和buff_id去重
保存在skill_2.json中
'''
# 读取 Excel 文件，确保设置正确的 header 和指定中文列名
file_path = 'knight-魂师.xlsx'
sheet_name = 'knight_star_info'
df = pd.read_excel(file_path, sheet_name, header=5)

# 循环遍历 knight 列中 id 等于 1001 至 3032 的范围
result_list = []

for knight_id in range(1001, 3033):
    # 筛选符合条件的行（knight 列中 id 等于当前迭代的 knight_id）
    filtered_df = df[df['knight'] == knight_id]

    # 提取并合并 skill_passive_1、skill_passive_2 和 skill_passive_3 中的 id
    skills = list(set(filtered_df[['skill_passive_1', 'skill_passive_2', 'skill_passive_3', 'skill_passive_4', 'skill_passive_5']]
                  .stack().dropna().astype(int)))

    if skills:
        # 将结果存储到字典中
        result_dict = {'knight_id': knight_id, 'skills': skills}
        result_list.append(result_dict)

# 将结果保存到对应的 JSON 文件
json_file_path = 'skill.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(result_list, json_file, ensure_ascii=False, indent=2)

print(f"Skills data saved to {json_file_path}")

