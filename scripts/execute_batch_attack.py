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
        # 批量处理几千张图耗时极长，必须设置较长的超时时间
        response = requests.post("http://127.0.0.1:8000/batch_attack", json=payload, timeout=3600)
        print(json.dumps(response.json(), ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))