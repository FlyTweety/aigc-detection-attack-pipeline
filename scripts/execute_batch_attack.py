import argparse
import requests
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--attack_type", type=str, required=True, choices=["JPEG", "BLUR"])
    parser.add_argument("--intensity", type=int, required=True, help="1-100之间的整数")
    args = parser.parse_args()
    
    payload = {
        "attack_type": args.attack_type,
        "intensity": args.intensity
    }
    
    try:
        # 注意：真实GPU推理可能需要几十分钟甚至数小时。Timeout设置为 7200 秒 (2小时)
        response = requests.post("http://127.0.0.1:8000/batch_attack", json=payload, timeout=7200)
        print(json.dumps(response.json(), ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))