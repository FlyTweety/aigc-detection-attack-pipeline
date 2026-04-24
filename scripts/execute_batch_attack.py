import argparse
import requests
import json
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline", type=str, required=True, help='格式示例: \'[{"attack_type": "BLUR", "intensity": 30}, {"attack_type": "JPEG", "intensity": 60}]\'')
    # 新增模型选择器，保持向后兼容
    parser.add_argument("--target_model", type=str, default="MIRROR", help='指定后端执行推理的 AI 检测模型名称')
    args = parser.parse_args()
    
    try:
        pipeline_data = json.loads(args.pipeline)
        if not isinstance(pipeline_data, list) or len(pipeline_data) == 0:
            raise ValueError("Pipeline 必须是非空列表")
    except Exception as e:
        print(json.dumps({"status": "error", "message": f"Pipeline 参数解析失败，请确保使用合法的 JSON 字符串: {str(e)}"}))
        sys.exit(1)

    payload = {
        "pipeline": pipeline_data,
        "target_model": args.target_model
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/batch_attack", json=payload, timeout=600)
        print(json.dumps(response.json(), ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))