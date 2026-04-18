import os
import json
from config import RAW_IMAGE_DIR

def get_target_images():
    supported_formats = ('.png', '.jpg', '.jpeg', '.webp')
    image_list = []
    for filename in os.listdir(RAW_IMAGE_DIR):
        if filename.lower().endswith(supported_formats):
            image_list.append({
                "image_name": filename,
                "image_path": os.path.join(RAW_IMAGE_DIR, filename)
            })
    return image_list

if __name__ == "__main__":
    try:
        images = get_target_images()
        # 标准化输出给 Agent
        print(json.dumps({"status": "success", "data": images}))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))