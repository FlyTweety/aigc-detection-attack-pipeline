import argparse
import json
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--content", type=str, required=True, help="Markdown报告的完整内容")
    parser.add_argument("--filename", type=str, default="AIGC_Detection_Vulnerability_Report.md", help="保存的文件名")
    args = parser.parse_args()
    
    try:
        # 确保使用UTF-8写入，防止乱码
        with open(args.filename, "w", encoding="utf-8") as f:
            f.write(args.content)
        print(json.dumps({"status": "success", "message": f"报告已成功保存至当前目录下的 {args.filename}", "absolute_path": os.path.abspath(args.filename)}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))