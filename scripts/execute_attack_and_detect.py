import os
import json
import argparse
import random
from PIL import Image, ImageFilter
from config import PROCESSED_IMAGE_DIR, load_history, save_history

def execute_and_detect(image_name, image_path, attack_type, intensity):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"找不到源图像: {image_path}")

    # 1. 图像处理阶段
    name, ext = os.path.splitext(image_name)
    processed_name = f"{name}_{attack_type}_{intensity}{ext}"
    processed_path = os.path.join(PROCESSED_IMAGE_DIR, processed_name)

    img = Image.open(image_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # 根据强度 (1-100) 动态调整处理参数
    if attack_type == "JPEG":
        # intensity 越大，quality 越低 (100 -> 10, 1 -> 95)
        quality = max(10, int(100 - (intensity * 0.9)))
        img.save(processed_path, "JPEG", quality=quality)
    elif attack_type == "BLUR":
        # intensity 越大，模糊半径越大 (1 -> 0.5, 100 -> 5.0)
        radius = max(0.5, intensity * 0.05)
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=radius))
        blurred_img.save(processed_path)
    else:
        raise ValueError(f"不支持的攻击类型: {attack_type}")

    # 2. Dummy 检测阶段 (模拟逼真的置信度下降)
    # 假设初始 AI 生成概率为 0.99
    base_prob = 0.99 
    # 攻击越强，概率下降越多，加入少许随机波动
    drop_factor = (intensity / 100.0) * random.uniform(0.6, 1.1) 
    
    if attack_type == "JPEG":
        current_prob = max(0.01, base_prob - drop_factor * 0.6)
    else: # BLUR
        current_prob = max(0.01, base_prob - drop_factor * 0.8)

    is_aigc = bool(current_prob > 0.5)

    # 3. 记录经验并返回
    history = load_history(image_name)
    current_round = len(history) + 1
    
    round_result = {
        "round": current_round,
        "attack_type": attack_type,
        "intensity": intensity,
        "processed_image_path": processed_path,
        "aigc_probability": round(current_prob, 4),
        "is_aigc_prediction": is_aigc
    }
    
    history.append(round_result)
    save_history(image_name, history)

    return {
        "current_result": round_result,
        "full_history": history
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_name", type=str, required=True)
    parser.add_argument("--image_path", type=str, required=True)
    parser.add_argument("--attack_type", type=str, required=True, choices=["JPEG", "BLUR"])
    parser.add_argument("--intensity", type=int, required=True, help="1-100的整数")
    
    args = parser.parse_args()
    
    try:
        result = execute_and_detect(args.image_name, args.image_path, args.attack_type, args.intensity)
        print(json.dumps({"status": "success", "data": result}))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))