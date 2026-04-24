import requests
import json

if __name__ == "__main__":
    try:
        response = requests.get("http://127.0.0.1:8000/exploration_history", timeout=10)
        print(json.dumps(response.json(), ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))