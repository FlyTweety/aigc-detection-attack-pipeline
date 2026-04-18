import os
import json
from config import RAW_IMAGE_DIR

def get_image_paths():
    """获取原始文件夹下所有图像的完整路径"""
    supported_formats = ('.png', '.jpg', '.jpeg', '.webp', '.bmp')
    image_paths = []
    
    # 遍历目录读取图片文件
    for filename in os.listdir(RAW_IMAGE_DIR):
        if filename.lower().endswith(supported_formats):
            full_path = os.path.join(RAW_IMAGE_DIR, filename)
            image_paths.append(full_path)
            
    return image_paths

if __name__ == "__main__":
    # 无输入参数
    paths = get_image_paths()
    
    # 输出参数1: image_path (list[string])
    # 将结果转换为JSON字符串输出，以便Agent解析
    result = {"image_path": paths}
    print(json.dumps(result))