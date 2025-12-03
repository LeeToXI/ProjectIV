import os

def get_mod_names(folder_path):
    mod_names = []
    # 遍历指定文件夹中的所有文件和子文件夹
    for file_name in os.listdir(folder_path):
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, file_name)
        # 如果是文件（排除文件夹），则将其名称添加到 mod 名称列表中
        if os.path.isfile(file_path):
            mod_names.append(file_name)
    return mod_names

# 指定要操作的文件夹路径
folder_path = "./"
# 调用函数获取 mod 名称列表
mod_name_list = get_mod_names(folder_path)
# 打印获取到的 mod 名称
for mod_name in mod_name_list:
    print(mod_name)