import os
import json
import argparse
from PIL import Image, ImageFilter
from config import PROCESSED_IMAGE_DIR

def process_images(image_paths, attack_type):
    processed_paths = []
    
    for img_path in image_paths:
        if not os.path.exists(img_path):
            continue
            
        try:
            filename = os.path.basename(img_path)
            name, ext = os.path.splitext(filename)
            img = Image.open(img_path)
            
            # 统一转换为RGB以防格式冲突（如PNG带Alpha通道转JPEG会报错）
            if img.mode in ("RGBA", "P"): 
                img = img.convert("RGB")
                
            if attack_type == "JPEG":
                # JPEG 压缩攻击 (降低质量)
                new_filename = f"{name}_attack_JPEG.jpg"
                save_path = os.path.join(PROCESSED_IMAGE_DIR, new_filename)
                img.save(save_path, "JPEG", quality=15) # quality越低压缩越狠
                
            elif attack_type == "BLUR":
                # 高斯模糊攻击
                new_filename = f"{name}_attack_BLUR{ext}"
                save_path = os.path.join(PROCESSED_IMAGE_DIR, new_filename)
                blurred_img = img.filter(ImageFilter.GaussianBlur(radius=3))
                blurred_img.save(save_path)
                
            else:
                raise ValueError(f"不支持的 attack_type: {attack_type}")
                
            processed_paths.append(save_path)
            
        except Exception as e:
            # 在实际工程中建议记录log，此处简单忽略处理失败的图像
            pass
            
    return processed_paths

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="处理图像以进行AIGC检测攻击")
    # 接收Agent传来的JSON字符串作为列表
    parser.add_argument("--image_path", type=str, required=True, help="JSON格式的图像路径列表")
    parser.add_argument("--attack_type", type=str, required=True, choices=["JPEG", "BLUR"], help="攻击类型")
    
    args = parser.parse_args()
    
    # 解析输入参数
    image_paths_list = json.loads(args.image_path)
    
    # 处理图像
    processed_files = process_images(image_paths_list, args.attack_type)
    
    # 输出参数1: processed_image_path (list[string])
    result = {"processed_image_path": processed_files}
    print(json.dumps(result))