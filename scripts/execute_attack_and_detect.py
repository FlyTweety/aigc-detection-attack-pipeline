import argparse
import requests
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_name", type=str, required=True)
    # 接收 image_path 以兼容 Skill.md，但实际不用传给服务器，因为服务器已经在本地找了
    parser.add_argument("--image_path", type=str, required=False) 
    parser.add_argument("--attack_type", type=str, required=True, choices=["JPEG", "BLUR"])
    parser.add_argument("--intensity", type=int, required=True)
    args = parser.parse_args()
    
    payload = {
        "image_name": args.image_name,
        "attack_type": args.attack_type,
        "intensity": args.intensity
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/attack_and_detect", json=payload, timeout=60)
        # 考虑到未来调用真实的 GPU 模型可能耗时，这里的 timeout 设长一点 (60秒)
        print(json.dumps(response.json()))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))