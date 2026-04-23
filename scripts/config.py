import os
import json

# 绝对路径配置
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = "/root/aigc_det_attack"
RAW_IMAGE_DIR = os.path.join(BASE_DIR, "data", "raw_images")
PROCESSED_IMAGE_DIR = os.path.join(BASE_DIR, "data", "processed_images")
EXPERIENCE_DIR = os.path.join(BASE_DIR, "data", "experience")

# 确保目录存在
for directory in [RAW_IMAGE_DIR, PROCESSED_IMAGE_DIR, EXPERIENCE_DIR]:
    os.makedirs(directory, exist_ok=True)

def load_history(image_name):
    """加载单张图像的攻击历史"""
    history_path = os.path.join(EXPERIENCE_DIR, f"{image_name}_history.json")
    if os.path.exists(history_path):
        with open(history_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_history(image_name, history_data):
    """保存单张图像的攻击历史"""
    history_path = os.path.join(EXPERIENCE_DIR, f"{image_name}_history.json")
    with open(history_path, 'w', encoding='utf-8') as f:
        json.dump(history_data, f, indent=4, ensure_ascii=False)