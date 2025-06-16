import os

# 初始化文件数量变量
total_files_count = 0

# 遍历所有以0到127命名的文件夹
for i in range(128):
    folder_name = str(i)
    final_story_path = os.path.join("./output/"+folder_name, 'final_story')

    # 检查final_story文件夹是否存在
    if os.path.exists(final_story_path) and os.path.isdir(final_story_path):
        # 遍历final_story文件夹中的所有文件
        for root, dirs, files in os.walk(final_story_path):
            # 累加文件数量
            total_files_count += len(files)

# 输出文件总数
print(f"所有final_story文件夹中的文件总数是: {total_files_count}")
