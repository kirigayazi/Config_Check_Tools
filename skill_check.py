import pandas as pd
import json

# 读取 Excel 文件
file_path = 'skill_技能效果.xlsx'
sheet_name = 'skill_effect_info'
skill_effect_info_df = pd.read_excel(file_path, sheet_name, header=5)

# 读取 JSON 文件
json_file_path = 'skill_number.json'
with open(json_file_path, 'r') as json_file:
    data_list = json.load(json_file)

# 创建一个 DataFrame 用于保存结果
result_df = pd.DataFrame(columns=['id', 'remark2', 'sort', 'range', 'effect', 'remark6', 'effect_num1'])

# 遍历每个字典
for item in data_list:
    for key, value in item.items():
        # 检查值是否为列表，如果不是则转换为列表
        if not isinstance(value, list):
            value = [value]

        # 遍历值，逐个检索 skill_effect_info 表并获取相关列的信息
        for id_value in value:
            # 检查 id_value 是否为数字字符串
            if str(id_value).isdigit():
                # 将 id_value 转换为整数
                id_value = int(id_value)
                # 使用 Pandas 进行检索
                result = skill_effect_info_df[skill_effect_info_df['id'] == id_value]
                if not result.empty:
                    # 提取相关列的信息
                    result_info = result[['id', 'remark2', 'sort', 'range', 'effect', 'remark6', 'effect_num1']].iloc[0]
                    # 将结果添加到 result_df 中
                    result_df = pd.concat([result_df, result_info.to_frame().T], ignore_index=True)
                    print(f"Result added for id_value: {id_value}")
                else:
                    print(f"No result found for id_value: {id_value}")
            else:
                print(f"Invalid id_value: {id_value}")

# 将结果保存到 skll_check.xlsx 文件
result_df.drop_duplicates(subset='id', keep='first', inplace=True)
result_df.to_excel('skll_check.xlsx', index=False)

print(result_df)
