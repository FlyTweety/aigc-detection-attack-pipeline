import os
import json
import argparse
import random
from config import RESULTS_JSON_PATH

def detect_aigc(processed_paths):
    """
    Dummy版本的AIGC图像检测器。
    随机生成检测结果来模拟真实的AI检测系统输出。
    """
    results = []
    
    for path in processed_paths:
        if not os.path.exists(path):
            continue
            
        # 模拟模型输出结果
        is_aigc_prob = round(random.uniform(0.1, 0.99), 4)
        is_aigc_pred = bool(is_aigc_prob > 0.5)
        
        result_dict = {
            "file_name": os.path.basename(path),
            "file_path": path,
            "is_aigc_prediction": is_aigc_pred,
            "aigc_probability": is_aigc_prob,
            "model_version": "dummy_v1.0"
        }
        results.append(result_dict)
        
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dummy AIGC 图像检测脚本")
    parser.add_argument("--processed_image_path", type=str, required=True, help="JSON格式的处理后图像路径列表")
    
    args = parser.parse_args()
    
    # 解析输入参数
    processed_paths_list = json.loads(args.processed_image_path)
    
    # 进行Dummy检测
    det_results = detect_aigc(processed_paths_list)
    
    # 将汇总结果保存到统一的全局JSON文件中
    with open(RESULTS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(det_results, f, indent=4, ensure_ascii=False)
    
    # 输出参数1: aigc_det_results (list[dict])
    result = {"aigc_det_results": det_results}
    print(json.dumps(result))