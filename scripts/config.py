import os

# 定义全局路径变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 假设执行在根目录

RAW_IMAGE_DIR = os.path.join(BASE_DIR, "data", "raw_images")
PROCESSED_IMAGE_DIR = os.path.join(BASE_DIR, "data", "processed_images")
RESULTS_JSON_PATH = os.path.join(BASE_DIR, "data", "aigc_det_results.json")

# 确保目录存在
os.makedirs(RAW_IMAGE_DIR, exist_ok=True)
os.makedirs(PROCESSED_IMAGE_DIR, exist_ok=True)
os.makedirs(os.path.dirname(RESULTS_JSON_PATH), exist_ok=True)