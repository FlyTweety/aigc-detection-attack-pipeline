import os
import json
from config import EXPERIENCE_DIR

def calculate_stats():
    stats = {
        "total_images_tested": 0,
        "successful_bypasses": 0,
        "failed_bypasses": 0,
        "attack_type_performance": {},
        "average_rounds_to_success": 0
    }
    
    total_rounds_for_success = 0
    
    for filename in os.listdir(EXPERIENCE_DIR):
        if not filename.endswith("_history.json"):
            continue
            
        stats["total_images_tested"] += 1
        with open(os.path.join(EXPERIENCE_DIR, filename), 'r', encoding='utf-8') as f:
            history = json.load(f)
            
        if not history:
            continue
            
        last_round = history[-1]
        if last_round["aigc_probability"] < 0.5:
            stats["successful_bypasses"] += 1
            total_rounds_for_success += len(history)
            
            # 记录哪种攻击成功了，以及其强度
            atype = last_round["attack_type"]
            intensity = last_round["intensity"]
            if atype not in stats["attack_type_performance"]:
                stats["attack_type_performance"][atype] = {"success_count": 0, "avg_intensity_needed": []}
            
            stats["attack_type_performance"][atype]["success_count"] += 1
            stats["attack_type_performance"][atype]["avg_intensity_needed"].append(intensity)
        else:
            stats["failed_bypasses"] += 1

    # 计算平均值
    if stats["successful_bypasses"] > 0:
        stats["average_rounds_to_success"] = round(total_rounds_for_success / stats["successful_bypasses"], 2)
        
    for atype, data in stats["attack_type_performance"].items():
        if data["avg_intensity_needed"]:
            avg_int = sum(data["avg_intensity_needed"]) / len(data["avg_intensity_needed"])
            data["avg_intensity_needed"] = round(avg_int, 2)

    return stats

if __name__ == "__main__":
    try:
        stats = calculate_stats()
        print(json.dumps({"status": "success", "data": stats}))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))