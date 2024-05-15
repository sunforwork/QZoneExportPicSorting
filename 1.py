import os
import shutil
import ijson
from collections import defaultdict

# 定义文件路径
json_file_path = r'C:\Users\Administrator\Desktop\down\666\Messages\2014.json'
img_source_dir = r'C:\Users\Administrator\Desktop\down\666\Messages\images'
img_dest_dir = r'C:\Users\Administrator\Desktop\down\2014img'

# 创建目标目录，如果不存在则创建
os.makedirs(img_dest_dir, exist_ok=True)

# 用于记录重命名时的文件计数
file_count = defaultdict(int)

# 使用ijson逐条读取JSON文件
with open(json_file_path, 'r', encoding='utf-8') as f:
    objects = ijson.items(f, 'item')
    for obj in objects:
        create_time = obj.get('custom_create_time', '')
        if 'pic' in obj:
            for pic in obj['pic']:
                filename = pic.get('custom_filename', '')
                if filename:
                    # 提取图片的扩展名
                    file_extension = os.path.splitext(filename)[1]
                    
                    # 构建新的文件名
                    new_filename = f"{create_time.replace(' ', '_').replace(':', '-')}{file_extension}"
                    
                    # 检查是否存在同名文件，如果有则增加计数后缀
                    file_count[new_filename] += 1
                    if file_count[new_filename] > 1:
                        base_name = os.path.splitext(new_filename)[0]
                        new_filename = f"{base_name}_{file_count[new_filename]}{file_extension}"
                    
                    # 构建源文件路径和目标文件路径
                    source_file = os.path.join(img_source_dir, filename)
                    dest_file = os.path.join(img_dest_dir, new_filename)
                    
                    # 移动并重命名文件
                    if os.path.exists(source_file):
                        shutil.move(source_file, dest_file)
                        print(f"Moved: {source_file} -> {dest_file}")
                    else:
                        print(f"File not found: {source_file}")

print("分拣完成")
